# Task 3: Store Cleaned Data in PostgreSQL

## Project Overview
This task implements a relational PostgreSQL database to store cleaned and processed bank review data. The project demonstrates real-world data engineering workflows, including database creation, table design, data insertion, and verification.

## Database Details
- **Database Name:** `bank_reviews`
- **Tables:**
  1. **banks**
     - `bank_id` (PRIMARY KEY)
     - `bank_name`
     - `app_name`
  2. **reviews**
     - `review_id` (PRIMARY KEY)
     - `bank_id` (FOREIGN KEY referencing `banks.bank_id`)
     - `review_text`
     - `rating`
     - `review_date`
     - `sentiment_label`
     - `sentiment_score`
     - `source`
     - `nouns`
     - `identified_theme`
     - `noun_text`

## Data Insertion
- Python script `insert_reviews.py` is used to insert cleaned review data from `cleaned_reviews.csv`.
- Connection to PostgreSQL is established via `psycopg2`.
- Script ensures banks are inserted first, then reviews are linked via foreign keys.

Example from Python script:
```python
print("Connected to database successfully!")
print(f"{len(df)} reviews inserted.")
## Verification Queries
-- Check how many positive/negative/neutral
SELECT sentiment_label, COUNT(*) 
FROM reviews
GROUP BY sentiment_label;
-- Check average rating per bank
SELECT b.bank_name, AVG(r.rating) AS avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
-- Count how many reviews you inserted
SELECT COUNT(*) FROM reviews;
## Folder Structure
task3/
├── schema.sql            # SQL file containing table creation statements
├── insert_reviews.ipynb     # Python script to insert CSV data
└── README.md             # Task 3 documentation
Notes

PostgreSQL must be running locally (localhost:5432) with the database bank_reviews created.

Tables should be created before running the Python script.

This setup ensures that reviewers can replicate the database insertion and verification steps easily.

  


