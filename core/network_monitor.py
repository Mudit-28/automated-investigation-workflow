from config.patterns import PAYMENT_KEYWORDS, NOISE_KEYWORDS, PAYMENT_GATEWAYS, UPI_PATTERN


class NetworkMonitor:
    def __init__(self):
        self.captured_requests = []

    def _is_relevant(self, url):
        url_lower = url.lower()
        has_payment_keyword = any(k in url_lower for k in PAYMENT_KEYWORDS)
        has_noise = any(n in url_lower for n in NOISE_KEYWORDS)
        return has_payment_keyword and not has_noise

    def _detect_gateways(self, url):
        url_lower = url.lower()
        found = [g for g in PAYMENT_GATEWAYS if g in url_lower]
        return found if found else []

    def _on_request(self, request):
        url = request.url
        if not self._is_relevant(url):
            return
        entry = {
            "type": "request",
            "url": url,
            "method": request.method,
            "headers": dict(request.headers),
            "gateways_detected": self._detect_gateways(url),
            "post_data": request.post_data or None,
        }
        self.captured_requests.append(entry)
        print(f"[Network] Captured: {request.method} {url}")

    def _on_response(self, response):
        url = response.url
        if not self._is_relevant(url):
            return
        entry = {
            "type": "response",
            "url": url,
            "status": response.status,
            "gateways_detected": self._detect_gateways(url),
        }
        self.captured_requests.append(entry)

    def attach(self, page):
        page.on("request", self._on_request)
        page.on("response", self._on_response)
        print("[Network Monitor] Listening for payment-related requests...")

    def get_captured(self):
        return self.captured_requests