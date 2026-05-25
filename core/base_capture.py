import os
from datetime import datetime

class Capture:
    def __init__(self, output_dir):
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
    
    def build_filepath(self, website_name, extension):
        clean_name = self.clean_name(website_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{clean_name}_{timestamp}_{self.counter}{extension}"
        return os.path.join(self.output_dir, filename)
    