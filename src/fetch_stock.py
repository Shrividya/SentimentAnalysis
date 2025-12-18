import yfinance as yf


def get_stock_data(ticker, period="1d", interval="1m"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data
