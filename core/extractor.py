import re
from config.patterns import UPI_PATTERN, PAYMENT_GATEWAYS, PAYMENT_KEYWORDS


class Extractor:
    def __init__(self):
        self.results = []

    def _extract_upi(self, text):
        if not text:
            return []
        matches = UPI_PATTERN.findall(text)
        seen = set()
        unique = []
        for match in matches:
            if match not in seen:
                seen.add(match)
                unique.append(match)
        return unique

    def _extract_gateways(self, text):
        if not text:
            return []
        text_lower = text.lower()
        found = [g for g in PAYMENT_GATEWAYS if g in text_lower]
        return list(set(found))

    def _extract_from_requests(self, captured_requests):
        extracted = []
        for entry in captured_requests:
            url = entry.get("url", "")
            post_data = entry.get("post_data", "") or ""
            combined_text = url + " " + post_data
            upi_ids = self._extract_upi(combined_text)
            gateways = self._extract_gateways(combined_text)

            extracted.append({
                "source": "network",
                "url": url,
                "method": entry.get("method", ""),
                "upi_ids_found": upi_ids,
                "gateways_found": gateways or entry.get("gateways_detected", []),
                "post_data": post_data
            })
        return extracted

    def _extract_from_html(self, html_content):
        if not html_content:
            return {}
        upi_ids = self._extract_upi(html_content)
        gateways = self._extract_gateways(html_content)
        html_lower = html_content.lower()
        keywords_found = [k for k in PAYMENT_KEYWORDS if k in html_lower]
        return {
            "source": "html",
            "upi_ids_found": upi_ids,
            "gateways_found": gateways,
            "payment_keywords_found": keywords_found
        }

    def run(self, captured_requests, html_content, page_title, url, screenshot_path):
        network_findings = self._extract_from_requests(captured_requests)
        html_findings = self._extract_from_html(html_content)
        summary = {
            "url": url,
            "page_title": page_title,
            "screenshot_path": screenshot_path,
            "network_findings": network_findings,
            "html_findings": html_findings,
            "total_payment_requests": len(network_findings),
            "all_upi_ids": list(set(
                html_findings.get("upi_ids_found", []) +
                [uid for f in network_findings for uid in f.get("upi_ids_found", [])]
            )),
            "all_gateways": list(set(
                html_findings.get("gateways_found", []) +
                [g for f in network_findings for g in f.get("gateways_found", [])]
            ))
        }
        self.results.append(summary)
        return summary