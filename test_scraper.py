from scraper import scrape_linkedin_page

try:
    # Replace "deepsolv" with the LinkedIn page ID you want to test
    data = scrape_linkedin_page("deepsolv")
    print("Scraped data:", data)
except Exception as e:
    print("Scraping failed:", str(e))