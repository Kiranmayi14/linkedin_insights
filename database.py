import mysql.connector

def get_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Kiran@14*",  # Replace with your MySQL password
            database="linkedin_insights"
        )
        print("Database connection successful!")
        return db
    except Exception as e:
        print("Database connection failed:", str(e))
        raise

    