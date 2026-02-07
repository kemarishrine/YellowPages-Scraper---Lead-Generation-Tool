import os
import subprocess
import sys


def install_dependencies():
    """Checks and installs missing dependencies automatically."""
    required_libraries = ["pandas", "playwright", "nest_asyncio"]
    missing = []

    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing.append(lib)

    if missing:
        print(f"--- Missing components detected: {missing} ---")
        print("Installing dependencies, please wait...")
        try:
            # Install python libraries
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

            # Special command for Playwright browser binaries
            if "playwright" in missing or True:
                print("Downloading browser engines (Chromium)...")
                subprocess.check_call(
                    [sys.executable, "-m", "playwright", "install", "chromium"]
                )

            print("\n" + "=" * 40)
            print("SUCCESS: All components installed.")
            print("Please CLOSE this window and RUN the script again.")
            print("=" * 40)
            input("Press ENTER to exit...")
            sys.exit()
        except Exception as e:
            print(f"Error during auto-installation: {e}")
            input("Please install manually or contact support. Press ENTER to exit...")
            sys.exit()


# Run the installer check before anything else
install_dependencies()

# --- ACTUAL SCRAPER CODE STARTS HERE ---
import asyncio

import nest_asyncio
import pandas as pd
from playwright.async_api import async_playwright

nest_asyncio.apply()


async def run_scraper(search_url):
    print("\n[1/3] Launching browser...")
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            print(f"[2/3] Extracting data from: {search_url}")
            await page.goto(search_url, wait_until="domcontentloaded", timeout=60000)

            leads = []
            cards = await page.query_selector_all(".v-card")

            for card in cards:
                name_el = await card.query_selector(".business-name span")
                phone_el = await card.query_selector(".phones.phone.primary")

                leads.append(
                    {
                        "Business Name": await name_el.inner_text()
                        if name_el
                        else "N/A",
                        "Phone": await phone_el.inner_text() if phone_el else "N/A",
                    }
                )

            await browser.close()
            return leads
        except Exception as e:
            print(f"Scraping Error: {e}")
            return None


async def main():
    print("========================================")
    print("   B2B LEAD GENERATOR - AUTO-SETUP   ")
    print("========================================")

    target = "https://www.yellowpages.com/search?search_terms=mechanic&geo_location=Miami%2C+FL"
    results = await run_scraper(target)

    if results:
        df = pd.DataFrame(results)
        df.to_csv("extracted_leads.csv", index=False)
        print(f"\n[3/3] SUCCESS: {len(df)} leads saved to 'extracted_leads.csv'")
    else:
        print("\n[!] No data found.")

    input("\nProcess finished. Press ENTER to close...")


if __name__ == "__main__":
    asyncio.run(main())
