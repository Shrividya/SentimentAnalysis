import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st


def plot_stock(data, ticker):
    plt.figure(figsize=(10, 5))

    # Get today's high, low, and current price
    today_high = data["High"].iloc[-1]
    today_low = data["Low"].iloc[-1]
    current_price = data["Close"].iloc[-1]

    # Plot current price as a horizontal line
    plt.hlines(
        current_price,
        xmin=data.index[0],
        xmax=data.index[-1],
        colors="red",
        linewidth=2,
        label=f"Current Price: {current_price:.2f}",
    )

    # Set y-axis limits to today's low/high with padding
    plt.ylim(today_low * 0.995, today_high * 1.005)

    # Format x-axis with ticks every 2 hours
    ax = plt.gca()

    # 2-hour interval
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    plt.xticks(rotation=45)

    # Annotate current price
    plt.text(
        data.index[len(data) // 2],
        current_price * 1.001,
        f"{current_price:.2f}",
        color="red",
        fontsize=12,
        ha="center",
    )

    plt.ylabel("Price")
    plt.xlabel("Time (Market Hours)")
    plt.title(f"{ticker} Price Today")
    plt.legend()
    st.pyplot(plt)


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
