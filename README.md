# Google Play Bank App Reviews Analysis

**Author:** Bezawit Assefa  
**Week:** 2  
**Project:** Google Play Bank App Reviews Analysis  
**Submission Date:** December 2, 2025  

---

## Project Overview
This project analyzes user reviews from the Google Play Store for three Ethiopian banks’ mobile applications: **BOA, CBE, and Dashen**.  
The goal is to:  
- Clean and process review data  
- Store data in a PostgreSQL database  
- Perform sentiment and theme analysis  
- Derive insights, visualize results, and recommend app improvements  

The project demonstrates a complete data engineering and analysis workflow using Python, PostgreSQL, and data visualization tools.

---

## Folder Structure
project-root/
├── task1/ # Data collection & initial preprocessing
├── task2/ # Sentiment analysis & theme extraction
├── task3/ # PostgreSQL database setup and data insertion
├── task4/ # Insights, visualizations, and final report
└── README.md # Main project overview


---

## Task Summaries

### **Task 1: Data Collection & Preprocessing**
- Collected Google Play Store reviews for BOA, CBE, and Dashen apps
- Cleaned and standardized review text
- Stored data in CSV for further analysis

### **Task 2: Sentiment Analysis & Theme Extraction**
- Performed sentiment scoring (positive/negative) using NLP
- Extracted key themes (e.g., UI, Transactions, Customer Support)
- Added columns for nouns, identified themes, sentiment labels, and scores
- Stored processed CSV for Task 3 and 4

### **Task 3: Store Cleaned Data in PostgreSQL**
- Installed PostgreSQL and created a database `bank_reviews`
- Defined schema with **Banks** and **Reviews** tables
- Inserted cleaned CSV data using Python (`psycopg2`)
- Verified data integrity via SQL queries
- Documented schema for reproducibility

### **Task 4: Insights and Recommendations**
- Derived key insights, identifying **drivers (strengths)** and **pain points (weaknesses)** per bank
- Compared banks to highlight strengths and weaknesses
- Created visualizations: sentiment trends, rating distributions, keyword/theme charts
- Provided practical recommendations for app improvements
- Considered ethical aspects like review bias and sample size limitations

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone [your-repo-url]
cd [project-folder]


Install Python dependencies:

pip install -r requirements.txt


PostgreSQL Setup (Task 3):

Ensure PostgreSQL is running locally (localhost:5432)

Database: bank_reviews

Create tables using schema.sql

Insert CSV data using insert_reviews.ipynb

Run notebooks:

Task 2 & 4 notebooks for sentiment analysis and visualization

Data Source

Google Play Store reviews scraped for BOA, CBE, and Dashen bank apps

Notes

Ensure that Task 3 database is populated before running Task 4 notebooks

Visualizations and insights are derived from ~499 reviews inserted in Task 3

References

PostgreSQL Documentation

Python libraries: Pandas, Matplotlib, Seaborn, Psycopg2

Google Play Store review scraping tools


This README:  
- Gives a **clear overview** of the project  
- Summarizes **all tasks**  
- Includes **setup instructions** for someone to replicate your work  

If you want, I can also **draft a shorter, more “pull request-friendly” version** suitable for GitHub, keeping it under ~1 page while still covering all tasks.  

Do you want me to do that?



