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
    extractor = Extractor()
    storage = Storage()
    summary = None

    try:
        async with BrowserManager() as browser_manager:
            screenshot   = Screenshot(url)
            html_capture = HTMLCapture(url)
            monitor      = NetworkMonitor()
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
            
            # browser time limit
            for _ in range(120):
                await asyncio.sleep(1)
                if page.is_closed():
                    print(f"[Investigation] Browser closed — proceeding to save...")
                    break

            page_monitor.stop()

            final_html = ""
            try:
                print(f"[Investigation] Capturing final page state...")
                final_html = await page.content()
                await screenshot.capture_ss(page, page.url)
                await html_capture.capture_html(page, page.url)
            except Exception:
                print(f"[Investigation] Browser closed early — saving collected data...")

            captured = monitor.get_captured()
            print(f"\n[Debug] Total captured requests: {len(captured)}")
            for r in captured[:5]:
                print(f"  → {r.get('type')} | {r.get('url', '')[:80]}")

            summary = extractor.run(
                captured, final_html,
                initial_title, url, screenshot.output_dir
            )
            storage.save(summary)

    except Exception as e:
        print(f"[Investigation] Session ended: {e}")

    if summary:
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
    else:
        print(f"\n[Investigation] No data collected — session ended before capture.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        print("Example: python main.py https://www.airtel.in")
        sys.exit(1)

    url = sys.argv[1]
    asyncio.run(run_investigation(url))


if __name__ == "__main__":
    main()