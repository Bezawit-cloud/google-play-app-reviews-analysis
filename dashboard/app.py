import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Bank App Review Risk Monitor",
    layout="wide"
)

st.title("📊 Ethiopian Bank App Review Monitoring Dashboard")
st.markdown("""
This dashboard analyzes customer feedback from Google Play Store reviews
to identify operational risks, customer satisfaction trends, and improvement areas.
""")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir,"data" ,"ethopian_bank_reviews.csv")  # <-- CHANGE THIS
    df = pd.read_csv(file_path)
    return df

df = load_data()

# -----------------------------
# Sentiment Calculation
# -----------------------------
@st.cache_data
def add_sentiment(dataframe):

    def get_sentiment(text):
        score = TextBlob(str(text)).sentiment.polarity
        return "positive" if score > 0 else "negative"

    dataframe["sentiment_label"] = dataframe["review"].apply(get_sentiment)
    return dataframe

df = add_sentiment(df)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

selected_bank = st.sidebar.selectbox(
    "Select Bank",
    options=df["bank"].unique()
)

filtered_df = df[df["bank"] == selected_bank]

# -----------------------------
# Key Metrics
# -----------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

positive_pct = (filtered_df["sentiment_label"] == "positive").mean() * 100
negative_pct = (filtered_df["sentiment_label"] == "negative").mean() * 100
avg_rating = filtered_df["rating"].mean()

col1.metric("Positive Sentiment (%)", f"{positive_pct:.1f}%")
col2.metric("Negative Sentiment (%)", f"{negative_pct:.1f}%")
col3.metric("Average Rating", f"{avg_rating:.2f}")

# -----------------------------
# Rating Distribution
# -----------------------------
st.subheader("Rating Distribution")

fig, ax = plt.subplots()
filtered_df["rating"].hist(ax=ax)
ax.set_xlabel("Rating")
ax.set_ylabel("Count")
st.pyplot(fig)

# -----------------------------
# Sentiment Breakdown
# -----------------------------
st.subheader("Sentiment Breakdown")

sentiment_counts = filtered_df["sentiment_label"].value_counts()

fig2, ax2 = plt.subplots()
sentiment_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Sentiment")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# -----------------------------
# Business Risk Indicator
# -----------------------------
st.subheader("Business Risk Indicator")

if negative_pct > 50:
    st.error("⚠ High customer dissatisfaction detected. Immediate operational review recommended.")
elif negative_pct > 30:
    st.warning("Moderate dissatisfaction observed. Monitor customer complaints closely.")
else:
    st.success("Customer sentiment is relatively stable.")
