🟡 B2B Lead Generator: YellowPages Scraper (Auto-Setup)
A high-performance B2B lead extraction tool engineered to harvest contact information from YellowPages. Leveraging Playwright for asynchronous navigation and Pandas for data structuring, this scraper ensures speed, reliability, and precision even on dynamic JavaScript-heavy pages.

🚀 Key Features
⚡ Auto-Setup Engine: The script autonomously detects missing libraries or browser binaries (Chromium) and installs them for you. Zero manual configuration required.

🔄 Asynchronous Scraping: Built with asyncio and Playwright to maximize hardware efficiency and minimize execution time.

🕵️ Anti-Detection Measures: Features manual User-Agent rotation to mimic authentic human browsing patterns.

📊 Structured Export: Automatically generates a clean extracted_leads.csv file, perfectly formatted for Cold Calling, Email Marketing, or CRM imports.

🛡️ Robust Error Handling: Advanced exception system to prevent crashes during network timeouts or DOM changes.

🛠️ Technical Requirements
Python 3.8+

Active internet connection (for the initial component download).

📦 Installation & Usage
Designed for "One-Click" deployment simplicity:

Clone the Repository:

Set Your Target: Open the script and locate the target variable. By default, it is set to: target = "https://www.yellowpages.com/search?search_terms=mechanic&geo_location=Miami%2C+FL" Simply change the URL to any YellowPages search results link of your choice.

Run the Script:

💡 Pro Tip: On the first run, the script will detect missing dependencies and install pandas, playwright, nest_asyncio, and Chromium. Once finished, just close the window and run it again to start scraping!

📂 Output Data Structure
The script exports a CSV file with the following high-value columns:

Business Name: Legal or trade name of the company.

Phone: Primary contact number.

Seamlessly import your data into CRMs like Salesforce, HubSpot, or Pipedrive.

🧠 Logic Flow & Architecture
Dependency Check: Verifies the Python environment integrity before importing core modules.

Browser Context: Launches a Headless browser instance to optimize RAM usage.

Dynamic Parsing: Scans for .v-card CSS selectors and securely extracts text data.

Data Processing: Utilizes Pandas DataFrames for temporary storage and final CSV conversion.

⚖️ License
Distributed under the MIT License. You are free to use, modify, and distribute this software, even for commercial purposes. See for more information.

⚠️ Disclaimer
This tool is strictly for educational and market research purposes. Using this script for massive scraping must comply with YellowPages' Terms of Service and local privacy laws (GDPR/CCPA). The author is not responsible for any misuse of this software.

Crafted with 🐍 and a passion for automation.

What's next, Karl?
Now that the README is in English and looks like a top-tier open-source project, you are ready to conquer Reddit.

Would you like me to write the Reddit post specifically for /r/Python or /r/webscraping? Each needs a slightly different hook to avoid being flagged as spam. Let's get those stars on GitHub! 📐💪🐍🎸
