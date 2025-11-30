# Customer Experience Analytics for Fintech Apps — Task 1  
### 10 Academy: Artificial Intelligence Mastery — Week 2 Challenge

---

## 📌 Project Overview  
This project analyzes customer satisfaction with mobile banking apps by scraping and preprocessing Google Play Store reviews for three major Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

Task 1 focuses on **data collection** and **preprocessing** to prepare a clean dataset for NLP analysis and visualization in later tasks.

---

## 🎯 Task 1 Objectives  

- Scrape user reviews from the Google Play Store using `google-play-scraper`.
- Collect **400+ reviews per bank** (1,200 total recommended).
- Clean and preprocess the data:
  - Remove duplicates  
  - Handle missing values  
  - Standardize date format  
- Save the cleaned dataset as a CSV (kept locally, not uploaded to GitHub).
- Maintain a clean GitHub repository with `.gitignore`, `requirements.txt`, and a clear folder structure.

google-play-app-reviews-analysis/
│
├── data/ # (Hidden from GitHub using .gitignore)
│ ├── raw/ # Raw scraped review CSVs
│ └── processed/ # Cleaned final dataset
│
├── notebooks/
│ └── scraping.ipynb # Jupyter notebook for scraping + preprocessing
│
├── src/
│ └── scraping.py # (Optional) Python script version of scraping
│
├── .gitignore
├── requirements.txt
└── README.md


---

## 🛠 Tools & Libraries  

- Python 3.10+
- `google-play-scraper`
- `pandas`
- `numpy`
- Jupyter Notebook
- Git & GitHub

Install dependencies:

```bash
pip install -r requirements.txt

📘 Scraping Methodology
✔ App IDs Used
Bank	App ID
CBE	com.combanketh.mobilebanking
BOA	com.boa.boaMobileBanking
Dashen	com.dashen.dashensuperapp
✔ Scraping Function
def scrape_reviews(app_id, bank_name, n_reviews=400):
    reviews_list = []

    while len(reviews_list) < n_reviews:
        data, _ = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=None
        )
        reviews_list.extend(data)

    df = pd.DataFrame(data)[["content", "score", "at"]]
    df.columns = ["review", "rating", "date"]
    df["bank"] = bank_name
    df["source"] = "Google Play"

    return df

🧹 Preprocessing Steps

Converted review date → YYYY-MM-DD

Removed duplicate reviews

Removed rows with missing review text

Combined all banks into one dataframe

Saved final cleaned CSV to:

data/processed/ethiopian_banks_reviews.csv


(This folder is hidden in Git using .gitignore.)

📊 Output Summary

Total Reviews Scraped: ~500+ after cleaning

Final Columns:

review

rating

date

bank

source

Dataset is now prepared for sentiment analysis and theme extraction in Task 2.

🔒 Why the Data Folder Is Hidden

Large data files should not be pushed to GitHub.
.gitignore contains:

data/
*.csv


This keeps the repository clean and professional.

🌿 Git Branch Workflow

Branches used:

main → stable code

task-1 → development branch for Task 1

Example commit messages:

"Add scraping function for CBE, BOA, Dashen"

"Clean dataset and normalize dates"

"Hide data folder using .gitignore"

"Add Task 1 README"

## 📂 Project Structure  

