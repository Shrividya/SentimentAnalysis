import matplotlib.pyplot as plt
import streamlit as st


def plot_sentiment_summary(sentiment_list):
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for s in sentiment_list:
        counts[s] += 1
    labels = counts.keys()
    values = counts.values()
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["green", "red", "gray"])
    ax.set_ylabel("Count")
    ax.set_title("News Sentiment Summary")
    st.pyplot(fig)
