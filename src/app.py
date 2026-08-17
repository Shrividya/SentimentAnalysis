import pandas as pd
import streamlit as st

from fetch_news import fetch_news
from fetch_stock import get_stock_data
from sentiment import analyze_sentiment
from visualization import plot_sentiment_summary

st.title("Real-Time Stock Sentiment Analyzer")


# Data mode selection
data_mode = st.radio("Select Data Mode:", ("Real-Time", "Sample Data"))


ticker = st.text_input("Enter Stock Ticker:", "AAPL")


if st.button("Fetch Data"):
    st.subheader("Stock Data")
    try:
        if data_mode == "Real-Time":
            data = get_stock_data(ticker)
            if data.empty:
                raise ValueError(f"No stock data returned for '{ticker}'")
        else:
            data = pd.read_csv(
                "data/sample_stock.csv",
                parse_dates=["Date"],
                index_col="Date",
            )
            data.columns = data.columns.str.strip()  # Remove any spaces
        st.line_chart(data["Close"])
    except Exception as e:
        st.warning(f"Cannot fetch stock data: {e}")

    st.subheader("Latest News Sentiment")
    sentiment_results = []
    try:
        articles = fetch_news(ticker)
        for title, desc in articles:
            sentiment = analyze_sentiment(title + " " + str(desc))
            sentiment_results.append(sentiment)
            st.write(f"**{title}** - Sentiment: {sentiment}")
        if sentiment_results:
            plot_sentiment_summary(sentiment_results)
    except Exception as e:
        st.warning(f"Cannot fetch real news: {e}")
