# dashboard/app.py
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Ethiopian Bank Reviews Dashboard", layout="wide")

st.title("Ethiopian Bank Mobile App Reviews Dashboard")
st.markdown(
    """
This dashboard shows **user reviews and sentiment analysis** for BOA, CBE, and Dashen bank mobile apps.
"""
)

# ----------------------
# Load Data
# ----------------------
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    # main CSV (not in repo)
    main_file = os.path.join(base_path, "../data/ethopian_bank_reviews.csv")
    # fallback sample CSV (must be in repo)
    sample_file = os.path.join(base_path, "sample_reviews.csv")

    if os.path.exists(main_file):
        df = pd.read_csv(main_file)
    elif os.path.exists(sample_file):
        df = pd.read_csv(sample_file)
        st.warning("Using sample CSV instead of full dataset.")
    else:
        st.error("No data file found. Please add CSV to `data/` folder.")
        return pd.DataFrame()  # empty DataFrame

    return df

df = load_data()

if df.empty:
    st.stop()

# ----------------------
# Sidebar Filters
# ----------------------
st.sidebar.header("Filters")
banks = df['bank'].unique().tolist()
selected_banks = st.sidebar.multiselect("Select Bank(s)", banks, default=banks)

ratings = sorted(df['rating'].unique().tolist())
selected_ratings = st.sidebar.multiselect("Select Rating(s)", ratings, default=ratings)

filtered_df = df[(df['bank'].isin(selected_banks)) & (df['rating'].isin(selected_ratings))]

# ----------------------
# Metrics
# ----------------------
st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(filtered_df))
col2.metric("Average Rating", round(filtered_df['rating'].mean(), 2))
col3.metric("Median Rating", filtered_df['rating'].median())

# ----------------------
# Rating Distribution
# ----------------------
st.subheader("Rating Distribution per Bank")
plt.figure(figsize=(8,4))
sns.countplot(data=filtered_df, x='rating', hue='bank')
plt.title("Rating Distribution")
st.pyplot(plt.gcf())
plt.clf()

# ----------------------
# Word Cloud (Optional)
# ----------------------
if st.checkbox("Show Reviews Word Cloud"):
    from wordcloud import WordCloud
    text = " ".join(filtered_df['review'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    st.image(wordcloud.to_array(), use_column_width=True)

# ----------------------
# Show Raw Data
# ----------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
