# Google Play Bank App Reviews Analysis

**Author:** Bezawit Assefa  
**Week:** 12  
**Project:** Google Play Bank App Reviews Analysis  
**Submission Date:** February 17, 2026  

![Python CI](https://github.com/Bezawit-cloud/google-play-app-reviews-analysis/actions/workflows/python-app.yml/badge.svg)

---

## Project Title
Google Play Bank App Reviews Analysis: An interactive dashboard and analytics system for BOA, CBE, and Dashen bank mobile app reviews.

---

## Business Problem
Banking apps in Ethiopia are critical for customer engagement and digital transactions. However, user experience issues—such as slow transactions, confusing UI, or poor support—can lead to customer dissatisfaction and churn. This project analyzes real Google Play Store reviews to identify **strengths, weaknesses, and key pain points** in BOA, CBE, and Dashen mobile apps.

---

## Solution Overview
The project collects, cleans, and processes bank app reviews, performs **sentiment and theme analysis**, and presents insights via an **interactive Streamlit dashboard**.  
Key features:
- Filter reviews by bank and rating
- View summary metrics: total reviews, average rating, median rating
- Visualize rating distributions and review word clouds
- Explore sentiment analysis and key themes

---

## Key Results
- **Interactive Dashboard:** Allows finance and product teams to explore review trends in real time
- **Sentiment Insights:** Identified which banks excel in UI, transactions, and support
- **Automated Testing & CI/CD:** Ensures code reliability and reproducibility for future updates

---

## Quick Start

###  Clone repository

```git clone https://github.com/Bezawit-cloud/google-play-app-reviews-analysis.git
cd google-play-app-reviews-analysis
```

###  Install dependencies
```
pip install -r requirements.txt
```

###  Run the Streamlit dashboard
```
streamlit run dashboard/app.py
```

# Project Structure

```
project-root/
├── src/              # Modular Python code: preprocessing, sentiment, theme analysis
├── dashboard/        # Streamlit dashboard
├── tests/            # Pytest unit tests
├── notebooks/        # Analysis & visualization notebooks
├── data/             # Full dataset CSV (ignored for GitHub)
├── sample_reviews.csv# Sample dataset for Streamlit demo
├── screenshots/      # Dashboard screenshots
├── .github/workflows/# CI/CD GitHub Actions
└── README.md         # Project overview & instructions
```

## Demo

The dashboard allows users to explore metrics, sentiment, and themes interactively.

### link[]https://app-play-app-reviews-analysis-cypek9vtvkpjw9gu8juxu3.streamlit.app/

##  Technical Details

- **Data Source**: Google Play Store reviews for BOA, CBE, and Dashen apps

- **Preprocessing**: Cleaning, standardizing text, extracting nouns

- **Sentiment Analysis**: Positive, Negative, Neutral labels

- **Theme Extraction**: UI, Transactions, Customer Support

- **Visualization**: Summary metrics, rating distribution, word clouds

- **Testing & CI/CD**: Automated pytest tests, GitHub Actions for workflow

- **Dashboard**: Streamlit app with filters and interactive plots

## Future Improvements

- Add topic modeling to discover emerging themes automatically

- Include time-based trends to track ratings and sentiment over months

- Enhance dashboard with predictive analytics (e.g., forecasting app ratings)

- Add more interactivity and export options for finance stakeholders

## Author

Bezawit Assefa

Linkedin[https://www.linkedin.com/in/bezawit-assefa-4964592aa/]






