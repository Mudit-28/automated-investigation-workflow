from urllib.parse import unquote
from config.patterns import (
    UPI_PATTERN, UPI_PATTERN_LOOSE, PAYMENT_GATEWAYS,
    PAYMENT_KEYWORDS, IFSC_PATTERN, BANK_ACCOUNT_PATTERN
)


COMMON_EMAIL_DOMAINS = {
    "gmail", "yahoo", "hotmail", "outlook", "icloud",
    "rediffmail", "protonmail", "live", "msn"
}


class Extractor:
    def __init__(self):
        self.results = []

    def _extract_upi(self, text):
        if not text:
            return []
        decoded_text = unquote(text)
        strict = set(UPI_PATTERN.findall(decoded_text))
        loose = set(UPI_PATTERN_LOOSE.findall(decoded_text))
        filtered_loose = {
            m for m in loose
            if m.split("@")[-1].lower() not in COMMON_EMAIL_DOMAINS
            and m.split("@")[-1] == m.split("@")[-1].lower()
            and not m.split("@")[0][0].isupper()
        }
        return sorted(list(strict | filtered_loose))

    def _extract_upi_from_qr(self, qr_decoded):
        if not qr_decoded:
            return []
        try:
            if "pa=" in qr_decoded:
                pa_value = qr_decoded.split("pa=")[1].split("&")[0].strip()
                if pa_value and "@" in pa_value:
                    return [pa_value]
        except Exception:
            pass
        return self._extract_upi(qr_decoded)
    
    def _extract_bank_details(self, text):
        if not text:
            return {"ifsc_codes": [], "account_numbers": []}

        ifsc_codes = list(set(IFSC_PATTERN.findall(text)))

        account_numbers = []
        if ifsc_codes:
            for match in IFSC_PATTERN.finditer(text):
                start = max(0, match.start() - 300)
                end   = min(len(text), match.end() + 300)
                nearby_text = text[start:end]
                accounts = BANK_ACCOUNT_PATTERN.findall(nearby_text)
                account_numbers.extend(accounts)
            account_numbers = list(set(account_numbers))

        return {
            "ifsc_codes":      ifsc_codes,
            "account_numbers": account_numbers
        }

    def _extract_gateways(self, text):
        if not text:
            return []
        text_lower = text.lower()
        found = []
        for gateway_name, patterns in PAYMENT_GATEWAYS.items():
            if any(p in text_lower for p in patterns):
                found.append(gateway_name)
        return list(set(found))

    def _extract_from_requests(self, captured_requests):
        extracted = []
        for entry in captured_requests:
            url           = entry.get("url", "")
            post_data     = entry.get("post_data", "") or ""
            response_body = entry.get("response_body", "") or ""
            qr_decoded    = entry.get("qr_decoded", "") or ""
            combined_text = url + " " + post_data + " " + response_body + " " + qr_decoded

            upi_ids    = self._extract_upi(combined_text)
            qr_upi_ids = self._extract_upi_from_qr(qr_decoded)
            upi_ids    = sorted(list(set(upi_ids + qr_upi_ids)))

            gateways     = self._extract_gateways(combined_text)
            bank_details = self._extract_bank_details(combined_text)  

            extracted.append({
                "source": "network",
                "url": url,
                "method": entry.get("method", ""),
                "upi_ids_found": upi_ids,
                "gateways_found": gateways or entry.get("gateways_detected", []),
                "post_data": post_data,
                "response_body": response_body,
                "qr_decoded": qr_decoded,
                "ifsc_codes":      bank_details["ifsc_codes"],       
                "account_numbers": bank_details["account_numbers"],  
            })
        return extracted

    def _extract_from_html(self, html_content):
        if not html_content:
            return {}
        upi_ids      = self._extract_upi(html_content)
        gateways     = self._extract_gateways(html_content)
        bank_details = self._extract_bank_details(html_content)  
        html_lower   = html_content.lower()
        keywords_found = [k for k in PAYMENT_KEYWORDS if k in html_lower]
        return {
            "source": "html",
            "upi_ids_found": upi_ids,
            "gateways_found": gateways,
            "payment_keywords_found": keywords_found,
            "ifsc_codes":      bank_details["ifsc_codes"],       
            "account_numbers": bank_details["account_numbers"],  
        }

    def run(self, captured_requests, html_content, page_title, url, screenshot_path):
        network_findings = self._extract_from_requests(captured_requests)
        html_findings    = self._extract_from_html(html_content)
        summary = {
            "url": url,
            "page_title": page_title,
            "screenshot_path": screenshot_path,
            "network_findings": network_findings,
            "html_findings": html_findings,
            "total_payment_requests": len(network_findings),
            "all_upi_ids": sorted(list(set(
                html_findings.get("upi_ids_found", []) +
                [uid for f in network_findings for uid in f.get("upi_ids_found", [])]
            ))),
            "all_gateways": sorted(list(set(
                html_findings.get("gateways_found", []) +
                [g for f in network_findings for g in f.get("gateways_found", [])]
            ))),
            "all_ifsc_codes": sorted(list(set(     # ← add
                html_findings.get("ifsc_codes", []) +
                [i for f in network_findings for i in f.get("ifsc_codes", [])]
            ))),
            "all_account_numbers": sorted(list(set( # ← add
                html_findings.get("account_numbers", []) +
                [a for f in network_findings for a in f.get("account_numbers", [])]
            ))),
        }
        self.results.append(summary)
        return summary