from playwright.sync_api import sync_playwright
import os

OUTPUT_DIR = r"C:\Users\Инна\Desktop\projects\lumo-ai-agency\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pages = [
    ("http://localhost:5173/index.html",        "index-cta.png"),
    ("http://localhost:5173/about.html",         "about-cta.png"),
    ("http://localhost:5173/services/seo.html",  "seo-cta.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for url, filename in pages:
        page = browser.new_page(viewport={"width": 1280, "height": 1080})
        page.goto(url, wait_until="networkidle")
        output_path = os.path.join(OUTPUT_DIR, filename)
        page.screenshot(
            path=output_path,
            clip={"x": 0, "y": 0, "width": 1280, "height": 80},
        )
        print(f"Saved: {output_path}")
        page.close()
    browser.close()

print("All 3 navbar screenshots captured.")
