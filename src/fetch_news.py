import requests
import os

import dotenv

dotenv.load_dotenv()


def fetch_news(query, page_size=10):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise RuntimeError("NEWS_API_KEY not found")

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "pageSize": page_size,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "publishedAt",
    }

    headers = {"User-Agent": "StockSentimentAnalyzer/1.0"}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    articles = response.json().get("articles", [])
    return [(a["title"], a.get("description", "")) for a in articles]
