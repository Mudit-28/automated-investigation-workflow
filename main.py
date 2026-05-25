import asyncio
from core.browser import BrowserManager
from core.network_monitor import NetworkMonitor
from core.extractor import Extractor
from core.storage import Storage
from modules.screenshots import Screenshot
from modules.html_capture import HTMLCapture


async def main():
    url = "https://www.dream11.com"
    screenshot = Screenshot()
    html_capture = HTMLCapture()
    monitor = NetworkMonitor()
    extractor = Extractor()
    storage = Storage()

    try:
        async with BrowserManager() as browser_manager:
            page = await browser_manager.new_page()
            monitor.attach(page)

            await page.goto(url)
            await page.wait_for_load_state("networkidle")

            screenshot_path = await screenshot.capture_ss(page, url)
            html_content = await page.content()
            await html_capture.capture_html(page, url)
            page_title = await page.title()

            captured = monitor.get_captured()
            summary = extractor.run(
                captured, html_content,
                page_title, url, screenshot_path
            )

            storage.save(summary)

            print(f"\n[Extraction Summary]")
            print(f"  Page Title     : {summary['page_title']}")
            print(f"  Total Requests : {summary['total_payment_requests']}")
            print(f"  UPI IDs Found  : {summary['all_upi_ids']}")
            print(f"  Gateways Found : {summary['all_gateways']}")

            await asyncio.sleep(30)

    except Exception as e:
        print(f"An error occurred: {e}")


asyncio.run(main())