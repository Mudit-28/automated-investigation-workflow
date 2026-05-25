import asyncio
from core.browser import BrowserManager
from core.network_monitor import NetworkMonitor
from modules.screenshots import Screenshot
from modules.html_capture import HTMLCapture

async def main():
    url = "https://www.paytm.com"
    screenshot = Screenshot()
    html = HTMLCapture()
    monitor = NetworkMonitor()

    try:
        async with BrowserManager() as browser_manager:
            page = await browser_manager.new_page()
            
            monitor.attach(page)
            
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            
            await screenshot.capture_ss(page, url)
            print("[Main] Captured screenshot.")
            await html.capture_html(page, url)
            print("[Main] Captured HTML content.")
            
            captured = monitor.get_captured()
            print(f"\n[Summary] Total payment-related requests captured: {len(captured)}")
            for entry in captured:
                print(f"  → {entry['type'].upper()} | {entry['url']}")
            
            await asyncio.sleep(3)
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(main())