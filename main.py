import asyncio
from core.browser import BrowserManager
from modules.screenshots import Screenshot
from modules.html_capture import HTMLCapture


async def main():
    url = "https://www.google.com"
    screenshot = Screenshot()
    html = HTMLCapture()

    try:
        async with BrowserManager() as browser_manager:
            page = await browser_manager.new_page()
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            await screenshot.capture_ss(page, url)
            await html.capture_html(page, url)
            await asyncio.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")


asyncio.run(main())