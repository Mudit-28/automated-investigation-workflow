import asyncio
import io
import json
import base64
import re
import httpx
from config.patterns import (
    PAYMENT_KEYWORDS, NOISE_KEYWORDS, PAYMENT_GATEWAYS,
    UPI_PATTERN, UPI_COLLECT_PATTERNS, AGGREGATOR_PATTERNS
)

QR_IMAGE_URL_PATTERNS = ["/qr/", "qrcode", "qr-image", "generateqr", "getqr"]


class NetworkMonitor:
    def __init__(self):
        self.captured_requests = []

    def _is_relevant(self, url):
        url_lower = url.lower()
        has_noise = any(n in url_lower for n in NOISE_KEYWORDS)
        if has_noise:
            return False
        has_payment_keyword = any(k in url_lower for k in PAYMENT_KEYWORDS)
        is_known_gateway = bool(self._detect_gateways(url))
        return has_payment_keyword or is_known_gateway

    def _detect_gateways(self, url):
        url_lower = url.lower()
        found = []
        for gateway_name, patterns in PAYMENT_GATEWAYS.items():
            if any(p in url_lower for p in patterns):
                found.append(gateway_name)
        return found
    
    def _detect_aggregator(self, url):
        url_lower = url.lower()
        for name, patterns in AGGREGATOR_PATTERNS.items():
            if any(p in url_lower for p in patterns):
                return name
        return None

    def _is_collect_request(self, url, post_data=""):
        combined = (url + " " + (post_data or "")).lower()
        return any(p in combined for p in UPI_COLLECT_PATTERNS)

    async def _follow_redirect(self, url):
        try:
            async with httpx.AsyncClient(
                follow_redirects=True,
                timeout=5
            ) as client:
                r = await client.get(url)
                final_url = str(r.url)
                if final_url != url:
                    print(f"[Network] Short URL resolved: {url} → {final_url}")
                return final_url
        except Exception:
            pass
        return url


    def _decode_qr_bytes(self, raw_bytes):
        try:
            from pyzbar.pyzbar import decode as qr_decode
            from PIL import Image
            img = Image.open(io.BytesIO(raw_bytes))
            decoded = qr_decode(img)
            if decoded:
                return decoded[0].data.decode("utf-8")
        except Exception:
            pass
        return None

    async def _decode_qr_from_url(self, qr_url):
        try:
            import httpx
            async with httpx.AsyncClient(timeout=5) as client:
                r = await client.get(qr_url)
            if r.status_code == 200:
                result = self._decode_qr_bytes(r.content)
                if result:
                    return result
        except Exception:
            pass
        return None

    def _decode_qr_from_base64_html(self, html_content):
        try:
            matches = re.findall(
                r'data:image/(?:png|jpeg|jpg|gif);base64,([A-Za-z0-9+/=]+)',
                html_content
            )
            for match in matches:
                try:
                    img_data = base64.b64decode(match)
                    result = self._decode_qr_bytes(img_data)
                    if result and ("upi://" in result or "pa=" in result):
                        return result
                except Exception:
                    continue
        except Exception:
            pass
        return None

    async def _try_decode_qr(self, url, body_text, raw_bytes=None):
        qr_decoded = None

        is_qr_image_url = any(p in url.lower() for p in QR_IMAGE_URL_PATTERNS)
        if is_qr_image_url and raw_bytes:
            qr_decoded = self._decode_qr_bytes(raw_bytes)
            if qr_decoded:
                print(f"[Network] QR Decoded (image endpoint): {qr_decoded}")
                return qr_decoded

        if not body_text:
            return None

        if "qrImageLink" in body_text:
            try:
                data = json.loads(body_text)
                qr_url = (data.get("data") or {}).get("qrImageLink")
                if qr_url:
                    qr_decoded = await self._decode_qr_from_url(qr_url)
                    if qr_decoded:
                        print(f"[Network] QR Decoded (image link): {qr_decoded}")
                        return qr_decoded
            except Exception:
                pass

        if "data:image" in body_text:
            qr_decoded = self._decode_qr_from_base64_html(body_text)
            if qr_decoded:
                print(f"[Network] QR Decoded (base64 HTML): {qr_decoded}")
                return qr_decoded

        return None

    def _on_request(self, request):
        url = request.url
        if not self._is_relevant(url):
            return

        post_data   = request.post_data or None
        is_collect  = self._is_collect_request(url, post_data or "")
        aggregator  = self._detect_aggregator(url)

        if is_collect:
            print(f"[Network] UPI COLLECT REQUEST DETECTED: {request.method} {url}")
        if aggregator:
            print(f"[Network] AGGREGATOR HOSTED PAGE: {aggregator} — merchant UPI hidden, manual lookup required")

        entry = {
            "type": "request",
            "url": url,
            "method": request.method,
            "headers": dict(request.headers),
            "gateways_detected": self._detect_gateways(url),
            "post_data": post_data,
            "is_collect_request": is_collect,
            "aggregator": aggregator,
        }
        self.captured_requests.append(entry)
        print(f"[Network] Captured: {request.method} {url}")

    async def _on_response(self, response):
        url = response.url
        if not self._is_relevant(url):
            return

        body_text = None
        raw_bytes = None

        is_qr_image_url = any(p in url.lower() for p in QR_IMAGE_URL_PATTERNS)

        if is_qr_image_url:
            try:
                raw_bytes = await response.body()
            except Exception:
                pass
        else:
            try:
                body_text = await response.text()
            except Exception:
                pass

        qr_decoded = await self._try_decode_qr(url, body_text, raw_bytes)

        entry = {
        "type": "response",
        "url": url,
        "status": response.status,
        "gateways_detected": self._detect_gateways(url),
        "response_body": body_text,
        "qr_decoded": qr_decoded,
        "is_collect_request": self._is_collect_request(url),
        "aggregator": self._detect_aggregator(url),
        }
        self.captured_requests.append(entry)

    def attach(self, page):
        page.on("request", self._on_request)
        page.on("response", lambda response: asyncio.ensure_future(
            self._on_response(response)
        ))
        print("[Network Monitor] Listening for payment-related requests...")

    def get_captured(self):
        return self.captured_requests