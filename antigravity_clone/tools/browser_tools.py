"""
Browser automation tools using Playwright.
This gives the agent the ability to control a real browser.
"""
import base64
import subprocess
import time
from langchain_core.tools import tool

# Global browser state — shared across tool calls
_browser = None
_page = None
_pw = None


def _raise_browser_window():
    """Force the Playwright Chromium window to the front on Linux."""
    try:
        # Try xdotool (most common on Ubuntu/Debian)
        subprocess.Popen(
            ["xdotool", "search", "--name", "Chromium", "windowactivate", "--sync"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(0.3)
    except FileNotFoundError:
        pass
    try:
        # Try wmctrl as fallback
        subprocess.Popen(
            ["wmctrl", "-a", "Chromium"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        pass


def _get_page():
    """Lazy-init browser. Only starts when first browser tool is called."""
    global _browser, _page, _pw
    if _page is None:
        from playwright.sync_api import sync_playwright
        _pw = sync_playwright().start()
        _browser = _pw.chromium.launch(
            headless=False,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-blink-features=AutomationControlled",
                "--window-position=0,0",            # open at top-left corner of screen
                "--window-size=1280,800",           # fixed window size
            ]
        )
        context = _browser.new_context(
            viewport={"width": 1280, "height": 800},
            no_viewport=False,
        )
        _page = context.new_page()
        # Move window to front immediately after creation
        _page.bring_to_front()
        time.sleep(0.5)                            # give window manager time to show it
        _raise_browser_window()
    return _page


@tool
def open_url(url: str) -> str:
    """Open a URL in the browser. Use this to navigate to websites."""
    try:
        page = _get_page()
        page.bring_to_front()
        page.goto(url, timeout=15000)
        page.wait_for_load_state("domcontentloaded")
        page.bring_to_front()                      # force to front after page loads
        _raise_browser_window()                    # use OS-level window raise
        title = page.title()
        return f"✅ Opened: {url}\nPage title: {title}"
    except Exception as e:
        return f"❌ Failed to open {url}: {e}"



@tool
def click_element(selector: str) -> str:
    """Click an element on the page using a CSS selector.
    Examples: 'button#submit', 'a.nav-link', 'input[type=submit]', 'text=Sign In'"""
    try:
        page = _get_page()
        page.click(selector, timeout=5000)
        page.wait_for_load_state("domcontentloaded")
        return f"✅ Clicked: {selector}"
    except Exception as e:
        return f"❌ Could not click '{selector}': {e}"


@tool
def type_text(selector: str, text: str) -> str:
    """Type text into an input field. Use CSS selector to find the field.
    Examples: selector='input#email', text='user@example.com'"""
    try:
        page = _get_page()
        page.fill(selector, text, timeout=5000)
        return f"✅ Typed '{text}' into {selector}"
    except Exception as e:
        return f"❌ Could not type into '{selector}': {e}"


@tool
def screenshot() -> str:
    """Take a screenshot of the current browser page. Returns the file path."""
    try:
        import pathlib
        page = _get_page()
        screenshot_dir = pathlib.Path(__file__).parent.parent / "workspace" / "_screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        
        import time
        filename = f"screenshot_{int(time.time())}.png"
        filepath = screenshot_dir / filename
        page.screenshot(path=str(filepath))
        return f"✅ Screenshot saved: _screenshots/{filename}"
    except Exception as e:
        return f"❌ Screenshot failed: {e}"


@tool
def get_page_text() -> str:
    """Get the visible text content of the current browser page. 
    Useful for reading what's on screen."""
    try:
        page = _get_page()
        text = page.inner_text("body")
        # Truncate if too long
        if len(text) > 4000:
            text = text[:2000] + "\n\n... (truncated) ...\n\n" + text[-2000:]
        return f"Page text:\n{text}"
    except Exception as e:
        return f"❌ Could not get page text: {e}"
