import asyncio
from core.browser import BrowserManager


async def main():
    try:
        async with BrowserManager() as browser_manager:
            print("Browser Manager Initialized Successfully!")
            page = await browser_manager.new_page()
            print("New Page Created Successfully!")
            await page.goto("https://www.google.com")
            print("Navigated to Google Successfully!")
            await asyncio.sleep(3)
            print("Waiting for 3 seconds...")
            print("Browser Opened Successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
asyncio.run(main())