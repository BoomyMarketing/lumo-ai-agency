from playwright.sync_api import sync_playwright
import os

OUTPUT_DIR = r"C:\Users\Инна\Desktop\projects\lumo-ai-agency\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGES = [
    ("about", "http://localhost:5173/about.html"),
    ("services", "http://localhost:5173/services.html"),
    ("pricing", "http://localhost:5173/pricing.html"),
    ("contact", "http://localhost:5173/contact.html"),
    ("services-seo", "http://localhost:5173/services/seo.html"),
    ("services-geo", "http://localhost:5173/services/geo.html"),
]

def capture(page_obj, url, output_path, viewport_width=1280, viewport_height=900):
    page_obj.set_viewport_size({'width': viewport_width, 'height': viewport_height})
    page_obj.goto(url, wait_until='networkidle')
    page_obj.screenshot(path=output_path, full_page=False)

def capture_navbar_crop(page_obj, url, output_path, viewport_width=1280):
    """Capture only the top 200px navbar area using clip."""
    page_obj.set_viewport_size({'width': viewport_width, 'height': 900})
    page_obj.goto(url, wait_until='networkidle')
    page_obj.screenshot(path=output_path, clip={'x': 0, 'y': 0, 'width': viewport_width, 'height': 200})

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for slug, url in PAGES:
        # Full desktop screenshot (1280px)
        full_path = os.path.join(OUTPUT_DIR, f"{slug}-desktop-full.png")
        capture(page, url, full_path, viewport_width=1280, viewport_height=900)
        print(f"Saved full desktop: {full_path}")

        # Navbar crop (top 200px)
        nav_path = os.path.join(OUTPUT_DIR, f"{slug}-navbar.png")
        capture_navbar_crop(page, url, nav_path, viewport_width=1280)
        print(f"Saved navbar crop: {nav_path}")

    browser.close()
    print("All screenshots captured.")
