import os
from datetime import datetime

class Screenshot:
    def __init__(self, output_dir="output/screenshots"):
        self.output_dir = output_dir
        self.counter = 1
        os.makedirs(self.output_dir, exist_ok=True)

    def clean_name(self,website_name):
        name = website_name.lower()
        name = name.replace("https://", "").replace("http://", "")
        name = name.replace("www.", "")
        name = name.split("/")[0]        
        name = name.replace(".", "_")   
        return name
    
    async def capture_ss(self, page, website_name):
        clean_name = self.clean_name(website_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{clean_name}_{timestamp}_{self.counter}.png"
        filepath = os.path.join(self.output_dir, filename)

        await page.screenshot(path=filepath, full_page=True)

        print(f"[Screenshot] Saved: {filepath}")
        self.counter += 1
        return filepath