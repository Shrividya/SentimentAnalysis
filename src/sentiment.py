import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon", quiet=True)

_vader = SentimentIntensityAnalyzer()


def analyze_sentiment_tb(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


def analyze_sentiment_vader(text):
    polarity = _vader.polarity_scores(text)

    if polarity["compound"] >= 0.05:
        return "positive"
    elif polarity["compound"] <= -0.05:
        return "negative"
    else:
        return "neutral"


def analyze_sentiment(text):
    tb_result = analyze_sentiment_tb(text)

    vader_scores = _vader.polarity_scores(text)
    vader_result = analyze_sentiment_vader(text)

    # If both methods agree, return that sentiment
    if tb_result == vader_result:
        return tb_result

    # If they disagree, trust VADER when sentiment is strong
    if abs(vader_scores["compound"]) >= 0.3:
        return vader_result

    # Otherwise, neutral
    return "neutral"
