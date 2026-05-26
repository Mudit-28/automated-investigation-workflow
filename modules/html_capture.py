import os
from datetime import datetime
from urllib.parse import urlparse


class HTMLCapture:

    def __init__(self, url, base_output_dir="output/html"):
        parsed = urlparse(url)
        website_name = parsed.netloc.replace(".", "_").replace("www_", "")
        session_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_folder = f"{website_name}_{session_timestamp}"

        self.output_dir = os.path.join(base_output_dir, session_folder)
        os.makedirs(self.output_dir, exist_ok=True)
        self.counter = 1
        print(f"[HTML Capture] Session folder: {self.output_dir}")

    async def capture_html(self, page, url):
        parsed = urlparse(url)
        website_name = parsed.netloc.replace(".", "_").replace("www_", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{website_name}_{timestamp}_{self.counter}.html"
        filepath = os.path.join(self.output_dir, filename)

        html_content = await page.content()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        self.counter += 1
        print(f"[HTML Capture] Saved: {filepath}")
        return filepath