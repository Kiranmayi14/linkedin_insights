from fastapi import FastAPI, HTTPException
from database import get_db
from scraper import scrape_linkedin_page
from schemas import PageCreate, PageResponse
import mysql.connector

app = FastAPI()

@app.get("/page/{page_id}", response_model=PageResponse)
def get_page_details(page_id: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Page WHERE page_id = %s", (page_id,))
    page = cursor.fetchone()

    if not page:
        try:
            # Scrape data from LinkedIn
            scraped_data = scrape_linkedin_page(page_id)
            print("Scraped data:", scraped_data)

            # Insert scraped data into the database
            cursor.execute("""
                INSERT INTO Page (page_id, name, url, profile_picture_url, description, website, industry, total_followers)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                page_id,
                scraped_data["page_name"],
                scraped_data["url"],
                scraped_data["profile_picture"],
                scraped_data["description"],
                scraped_data["website"],
                scraped_data["industry"],
                scraped_data["followers"]
            ))
            db.commit()

            # Fetch the newly inserted page from the database
            cursor.execute("SELECT * FROM Page WHERE page_id = %s", (page_id,))
            page = cursor.fetchone()
        except Exception as e:
            print("Scraping or database insertion failed:", str(e))
            raise HTTPException(status_code=404, detail=f"Failed to fetch or save LinkedIn page: {str(e)}")

    return page


 

