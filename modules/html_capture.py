from core.base_capture import Capture

class HTMLCapture(Capture):
    def __init__(self):
        super().__init__("output/html")

    async def capture_html(self, page, website_name):
        filepath = self._build_filepath(website_name, ".html")
        content = await page.content()

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[HTML Capture] Saved: {filepath}")
        self.counter += 1
        return filepath