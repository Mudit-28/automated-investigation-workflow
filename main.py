import asyncio
import sys
from core.browser import BrowserManager
from core.network_monitor import NetworkMonitor
from core.extractor import Extractor
from core.storage import Storage
from modules.screenshots import Screenshot
from modules.html_capture import HTMLCapture

async def run_investigation(url):
    screenshot = Screenshot()
    html_capture = HTMLCapture()
    monitor = NetworkMonitor()
    extractor = Extractor()
    storage = Storage()

    try:
        async with BrowserManager() as browser_manager:
            page = await browser_manager.new_page()

            monitor.attach(page)

            print(f"\n[Investigation] Starting: {url}")
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            print(f"[Investigation] Page loaded")

            screenshot_path = await screenshot.capture_ss(page, url)
            print(f"[Main] Captured screenshot.")
            html_content = await page.content()
            await html_capture.capture_html(page, url)
            print(f"[Main] Captured HTML content.")
            page_title = await page.title()

            print(f"\n[Investigation] Manual exploration window — 30 seconds")
            print(f"[Investigation] Navigate to deposit/payment pages now...")
            await asyncio.sleep(30)

            await screenshot.capture_ss(page, url)

            captured = monitor.get_captured()
            summary = extractor.run(
                captured, html_content,
                page_title, url, screenshot_path
            )
            storage.save(summary)

            print(f"\n{'='*50}")
            print(f"[Summary] Investigation Complete")
            print(f"{'='*50}")
            print(f"  URL            : {summary['url']}")
            print(f"  Page Title     : {summary['page_title']}")
            print(f"  Total Requests : {summary['total_payment_requests']}")
            print(f"  UPI IDs Found  : {summary['all_upi_ids'] or 'None'}")
            print(f"  Gateways Found : {summary['all_gateways'] or 'None'}")
            print(f"  Screenshot     : {summary['screenshot_path']}")
            print(f"{'='*50}\n")

    except Exception as e:
        print(f"[Error] {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        print("Example: python main.py https://www.paytm.com")
        sys.exit(1)

    url = sys.argv[1]
    asyncio.run(run_investigation(url))


if __name__ == "__main__":
    main()