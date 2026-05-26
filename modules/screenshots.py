import os
from datetime import datetime
from urllib.parse import urlparse


class Screenshot:

    def __init__(self, url, base_output_dir="output/screenshots"):
        parsed = urlparse(url)
        website_name = parsed.netloc.replace(".", "_").replace("www_", "")
        session_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_folder = f"{website_name}_{session_timestamp}"

        self.output_dir = os.path.join(base_output_dir, session_folder)
        os.makedirs(self.output_dir, exist_ok=True)
        self.counter = 1
        print(f"[Screenshot] Session folder: {self.output_dir}")

    async def capture_ss(self, page, url):
        parsed = urlparse(url)
        website_name = parsed.netloc.replace(".", "_").replace("www_", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{website_name}_{timestamp}_{self.counter}.png"
        filepath = os.path.join(self.output_dir, filename)

        await page.screenshot(path=filepath, full_page=True)
        self.counter += 1
        print(f"[Screenshot] Saved: {filepath}")
        return filepath