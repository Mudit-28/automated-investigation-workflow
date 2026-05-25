from core.base_capture import Capture


class Screenshot(Capture):
    def __init__(self):
        super().__init__("output/screenshots")

    async def capture_ss(self, page, website_name):
        filepath = self.build_filepath(website_name, ".png")

        await page.screenshot(path=filepath, full_page=True)

        print(f"[Screenshot] Saved: {filepath}")
        self.counter += 1
        return filepath