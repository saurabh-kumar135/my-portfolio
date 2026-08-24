import time
import sys
from playwright.sync_api import sync_playwright

def main():
    print("Launching Google Chrome to open Naukri.com...")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                executable_path="/usr/bin/google-chrome",
                args=[
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            context = browser.new_context(
                viewport={"width": 1280, "height": 800}
            )
            page = context.new_page()
            page.goto("https://www.naukri.com", timeout=60000)
            print("Successfully opened https://www.naukri.com!")
            
            # Keep the browser open until it's closed or manual exit
            while True:
                time.sleep(1)
                if page.is_closed():
                    break
    except KeyboardInterrupt:
        print("Script terminated by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
