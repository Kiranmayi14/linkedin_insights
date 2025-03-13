LinkedIn Insights Microservice
This is a FastAPI-based microservice that fetches and stores LinkedIn page insights (e.g., page details, posts, followers) into a MySQL database. The application scrapes LinkedIn pages for data and exposes RESTful APIs to retrieve the stored information.

Features
Scrape LinkedIn Pages: Fetch details like page name, profile picture, description, website, industry, followers, and more.
Store Data in MySQL: Save scraped data into a MySQL database with proper relationships.
RESTful APIs: Expose endpoints to retrieve LinkedIn page details, posts, and followers.
Error Handling: Gracefully handle errors like invalid page IDs or scraping failures.

Technologies Used
Python: Primary programming language.
FastAPI: Web framework for building APIs.
MySQL: Database for persistent storage.
BeautifulSoup: Library for web scraping.
Requests: Library for making HTTP requests.

Setup Instructions
1. Prerequisites
Python 3.9 or higher
MySQL Server
Git (optional)

2. Clone the Repository
git clone https://github.com/your-username/linkedin-insights.git
cd linkedin-insights

3. Install Dependencies
Install the required Python packages:
pip install -r requirements.txt

4. Set Up MySQL Database
Start your MySQL server.
Create a database named linkedin_insights:
CREATE DATABASE linkedin_insights;
Create the Page table:
USE linkedin_insights;
CREATE TABLE Page (
    id INT AUTO_INCREMENT PRIMARY KEY,
    page_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    url VARCHAR(255),
    profile_picture_url VARCHAR(255),
    description TEXT,
    website VARCHAR(255),
    industry VARCHAR(255),
    total_followers INT,
    head_count INT,
    specialities TEXT
);

5. Configure Database Connection
Update the database.py file with your MySQL credentials:
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="linkedin_insights"
    )
   
Running the Application
1. Start the FastAPI Server
Run the following command to start the server:
uvicorn main:app --reload
The server will start at http://127.0.0.1:8000.

2. Access the API Documentation
Open your browser and navigate to:
http://127.0.0.1:8000/docs
This will display the Swagger UI for interacting with the API.
