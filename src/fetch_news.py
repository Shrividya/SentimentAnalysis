import requests
import os

import dotenv

dotenv.load_dotenv()

def fetch_news(query, page_size=10):
    """Fetch latest news articles using NewsAPI"""
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        raise ValueError('Please set NEWS_API_KEY in .env file')
    url = f'https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return [(a['title'], a['description']) for a in articles]