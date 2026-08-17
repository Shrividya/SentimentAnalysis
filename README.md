# Real-Time Stock Sentiment Analyzer
This project fetches real-time stock prices and news headlines, performs sentiment analysis, and visualizes the results.


## Features
- Fetch real-time stock prices using yfinance
- Fetch news headlines using NewsAPI
- Sentiment analysis combining TextBlob and VADER (NLTK), falling back to VADER when the two disagree strongly
- Interactive dashboard with Streamlit
- Sample data mode for trying the app without API keys or a network connection
- Dockerized for easy deployment
- CI pipeline with GitHub Actions (black, flake8)
- Sentiment Summary: Displays a bar chart of positive, negative, and neutral news counts for quick insights.

## Usage
1. Create a `.env` file in the project root and add your NewsAPI key (only needed for **Real-Time** mode):
```
NEWS_API_KEY=your_news_api_key_here
```
2. Install dependencies: `pip install -r requirements.txt`
3. Run app: `streamlit run src/app.py`
4. Select between **Real-Time** or **Sample Data** mode.
   - **Real-Time** fetches live stock prices (yfinance) and news (NewsAPI) for the ticker you enter.
   - **Sample Data** uses the bundled `data/sample_stock.csv` for stock prices and still fetches live news, so it works without a NewsAPI key.
5. Enter stock ticker in the app and click **Fetch Data**.
6. Or run with Docker:
```
docker build -t stock-sentiment-app .
docker run -p 8501:8501 --env-file .env stock-sentiment-app
```


## Project Structure
- `src/` - Source code
  - `app.py` - Streamlit entry point
  - `fetch_stock.py` - Stock price retrieval via yfinance
  - `fetch_news.py` - News retrieval via NewsAPI
  - `sentiment.py` - TextBlob/VADER sentiment analysis
  - `visualization.py` - Chart rendering
- `data/` - Sample historical CSV used by Sample Data mode
- `Dockerfile` - Container setup
- `.github/workflows/` - CI pipeline
- `requirements.txt` - Dependencies
- `README.md` - Project overview