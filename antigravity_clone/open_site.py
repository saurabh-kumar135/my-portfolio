import time
import sys
from playwright.sync_api import sync_playwright

def main():
    print("Launching Google Chrome with the Antigravity Browser Extension...")
    ext_path = "/home/saurabh-kumar123/.config/google-chrome/Default/Extensions/eeijfnjmjelapkebgockoeaadonbchdd/1.11.3_0"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                executable_path="/usr/bin/google-chrome",
                args=[
                    f"--disable-extensions-except={ext_path}",
                    f"--load-extension={ext_path}",
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            context = browser.new_context(
                viewport={"width": 1280, "height": 800}
            )
            page = context.new_page()
            
            print("Navigating to http://localhost:3009/ ...")
            page.goto("http://localhost:3009/", timeout=60000)
            print("Successfully opened http://localhost:3009/!")
            
            # Keep the browser open until closed
            while True:
                time.sleep(1)
                if page.is_closed():
                    break
    except KeyboardInterrupt:
        print("Script terminated.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
