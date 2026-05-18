import os
from playwright.sync_api import sync_playwright

# Use os.getcwd() to avoid encoding issues with Cyrillic path
SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")

def capture_footer_element(url, output_path, viewport_width=1920, viewport_height=1080):
    """Capture the footer element via element.screenshot()."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': viewport_width, 'height': viewport_height})
        page.goto(url, wait_until='networkidle')

        footer = page.query_selector('footer')
        if footer:
            box = footer.bounding_box()
            print(f"Footer bounding box: {box}")
            footer.screenshot(path=output_path)
        else:
            print("No <footer> found — scrolling to bottom and screenshotting viewport")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(600)
            page.screenshot(path=output_path, full_page=False)

        browser.close()
        print(f"Saved footer element screenshot: {output_path}")


def capture_scrolled_bottom(url, output_path, viewport_width=1920, viewport_height=1080):
    """Scroll to the bottom and capture what's in the viewport."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': viewport_width, 'height': viewport_height})
        page.goto(url, wait_until='networkidle')
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(800)
        page.screenshot(path=output_path, full_page=False)
        browser.close()
        print(f"Saved viewport-at-bottom screenshot: {output_path}")


if __name__ == '__main__':
    url = "http://localhost:5173/services.html"

    out_element = os.path.join(SCREENSHOTS_DIR, "services-footer-element.png")
    out_viewport = os.path.join(SCREENSHOTS_DIR, "services-footer-viewport.png")

    capture_footer_element(url, out_element)
    capture_scrolled_bottom(url, out_viewport)
