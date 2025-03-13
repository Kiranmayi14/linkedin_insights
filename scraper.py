import requests
from bs4 import BeautifulSoup

def scrape_linkedin_page(page_id):
    url = f"https://www.linkedin.com/company/{page_id}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch LinkedIn page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')

    # Debugging: Print the entire HTML to inspect the structure
    # print(soup.prettify())

    # Extract data here
    try:
        page_name = soup.find("h1").text.strip()
    except AttributeError:
        page_name = "N/A"

    try:
        profile_picture = soup.find("img", class_="org-top-card-primary-content__logo")["src"]
    except (AttributeError, TypeError):
        profile_picture = "N/A"

    try:
        description = soup.find("p", class_="org-about-us-organization-description__text").text.strip()
    except AttributeError:
        description = "N/A"

    try:
        website = soup.find("a", class_="org-about-us-company-module__website")["href"]
    except (AttributeError, TypeError):
        website = "N/A"

    try:
        industry = soup.find("dd", class_="org-page-details__definition-text").text.strip()
    except AttributeError:
        industry = "N/A"

    try:
        followers_text = soup.find("div", class_="org-top-card-summary-info-list__info-item").text.strip()
        followers = int(followers_text.replace(",", ""))
    except (AttributeError, ValueError):
        followers = 0

    return {
        "page_name": page_name,
        "profile_picture": profile_picture,
        "description": description,
        "website": website,
        "industry": industry,
        "followers": followers
    }