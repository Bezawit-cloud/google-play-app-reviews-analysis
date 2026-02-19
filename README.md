# Google Play Bank App Reviews Analysis

**Author:** Bezawit Assefa  
**Week:** 12  
**Project:** Google Play Bank App Reviews Analysis  
**Submission Date:** February 17, 2026  

![Python CI](https://github.com/Bezawit-cloud/google-play-app-reviews-analysis/actions/workflows/python-app.yml/badge.svg)  

---

## Project Overview
This project analyzes user reviews from the Google Play Store for three Ethiopian banks’ mobile applications: **BOA, CBE, and Dashen**.  

The goal is to:  
- Clean and process review data  
- Perform sentiment and theme analysis  
- Derive insights, visualize results, and recommend app improvements  

**New Week 12 Improvements:**  
- Modularized code in `src/` for better organization  
- Added automated **pytest tests** for preprocessing, sentiment, and theme analysis  
- Set up **CI/CD workflow** so tests run automatically on every push  
- Ensures **reliability and professionalism** — perfect for finance-sector portfolios  

---

## Folder Structure
project-root/
├── src/ # Modular Python code (preprocessing, sentiment, theme analysis)
├── tests/ # Automated pytest tests
├── notebooks/ # Jupyter notebooks for analysis and visualizations
├── data/ # Cleaned CSV datasets
├── .github/
│ └── workflows/ # CI/CD workflow for automated testing
└── README.md # Project overview

---

## Task Summaries

### **Task 1: Data Collection & Preprocessing**
- Collected Google Play Store reviews for BOA, CBE, and Dashen apps  
- Cleaned and standardized review text  
- Stored data in CSV for further analysis  

### **Task 2: Sentiment Analysis & Theme Extraction**
- Performed sentiment scoring (positive/negative/neutral) using NLP  
- Extracted key themes (e.g., UI, Transactions, Customer Support)  
- Added columns for nouns, identified themes, sentiment labels, and scores  
- Ensured tests cover all key functions  

### **Task 3: Store Cleaned Data in PostgreSQL**
- Created a database `bank_reviews` with **Banks** and **Reviews** tables  
- Inserted cleaned CSV data using Python (`psycopg2`)  
- Verified data integrity via SQL queries  

### **Task 4: Insights and Recommendations**
- Derived insights highlighting strengths (drivers) and weaknesses (pain points) per bank  
- Visualized sentiment trends, rating distributions, and keyword/theme charts  
- Recommended app improvements based on findings  

---

## Week 12 Improvements – Why They Matter
- **Modular Code:** Easier to maintain and reuse functions  
- **Automated Testing:** Ensures preprocessing, sentiment, and theme analysis work correctly  
- **CI/CD Workflow:** Automatically runs tests on GitHub every time code is updated  
- **Portfolio Impact:** Shows recruiters your project is **reliable, professional, and ready for finance applications**  

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/Bezawit-cloud/google-play-app-reviews-analysis.git
cd google-play-app-reviews-analysis
Install Python dependencies:

pip install -r requirements.txt


Run Tests (optional but recommended):

python -m pytest


Run Notebooks:

Task 2 & 4 notebooks for sentiment analysis and visualization

PostgreSQL Setup (Task 3, optional):

Ensure PostgreSQL is running locally (localhost:5432)

Database: bank_reviews

Create tables using schema.sql

Insert CSV data using insert_reviews.ipynb

Data Source

Google Play Store reviews scraped for BOA, CBE, and Dashen bank apps (~499 reviews).

References

Python libraries: Pandas, Matplotlib, Seaborn, Psycopg2, TextBlob, Spacy, Scikit-learn

PostgreSQL Documentation

Google Play Store review scraping tools




