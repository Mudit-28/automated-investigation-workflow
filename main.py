import asyncio
import sys
from core.browser import BrowserManager
from core.network_monitor import NetworkMonitor
from core.extractor import Extractor
from core.storage import Storage
from modules.screenshots import Screenshot
from modules.html_capture import HTMLCapture
from modules.page_monitor import PageMonitor


async def run_investigation(url):
    screenshot = Screenshot(url)
    html_capture = HTMLCapture(url)
    monitor = NetworkMonitor()
    page_monitor = PageMonitor(monitor, screenshot, html_capture)
    extractor = Extractor()
    storage = Storage()

    try:
        async with BrowserManager() as browser_manager:
            screenshot = Screenshot(url)
            html_capture = HTMLCapture(url)
            monitor = NetworkMonitor()
            page_monitor = PageMonitor(monitor, screenshot, html_capture)

            page = await browser_manager.new_page()

            monitor.attach(page)
            page_monitor.attach(page, url)
            page_monitor.attach_context(browser_manager.context, url)

            print(f"\n[Investigation] Starting: {url}")
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            print(f"[Investigation] Page loaded")

            initial_title = await page.title()

            await screenshot.capture_ss(page, url)
            print(f"[Main] Captured screenshot.")
            await html_capture.capture_html(page, url)
            print(f"[Main] Captured HTML content.")

            print(f"\n[Investigation] Manual exploration window — 60 seconds")
            print(f"[Investigation] Navigate to deposit/payment pages now...")

            await asyncio.sleep(60)
            page_monitor.stop()

            print(f"[Investigation] Capturing final page state...")
            final_html = await page.content()
            final_screenshot_path = await screenshot.capture_ss(page, page.url)
            await html_capture.capture_html(page, page.url)

            captured = monitor.get_captured()
            print(f"\n[Debug] Total captured requests: {len(captured)}")
            for r in captured[:5]:
                print(f"  → {r.get('type')} | {r.get('url', '')[:80]}")

            summary = extractor.run(
            captured, final_html,
            initial_title, url, screenshot.output_dir
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
            print(f"  Screenshot Dir : {summary['screenshot_path']}")
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