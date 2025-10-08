"""
AI Finance App - Backend (Flask) - Level 1

Endpoints:
- GET /api/health           -> Health check
- GET /api/quotes?ticker=&range= -> OHLCV for a ticker using yfinance

Upgrade Notes:
- Level 2: Add /api/indicators (SMA, EMA, RSI), volatility, correlations
- Level 3: Add /api/forecast (sklearn models)
- Level 4: Add /api/dl-forecast (LSTM/GRU)
- Level 5: Add /api/assistant (LLM Q&A with LangChain)
- Level 6: Add /api/optimize and /api/rl-sim
- Level 7: Add DB integration, auth, background tasks
"""

from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

try:
    import yfinance as yf
except ImportError:
    yf = None

app = Flask(__name__)
CORS(app)


def as_json(df):
    """Convert yfinance DataFrame into JSON arrays for frontend plotting."""
    if df is None or df.empty:
        return {"dates": [], "open": [], "high": [], "low": [], "close": [], "volume": []}

    df = df.reset_index()
    dates = [d.strftime('%Y-%m-%d') if isinstance(d, datetime) else str(d) for d in df['Date']]
    return {
        "dates": dates,
        "open": df['Open'].round(4).tolist(),
        "high": df['High'].round(4).tolist(),
        "low": df['Low'].round(4).tolist(),
        "close": df['Close'].round(4).tolist(),
        "volume": df['Volume'].astype(int).tolist(),
    }


@app.get('/api/health')
def health():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat() + 'Z'})


@app.get('/api/quotes')
def quotes():
    """
    Level 1: Fetch financial data from API and return OHLCV
    Query params:
      - ticker: e.g., AAPL, TSLA, BTC-USD
      - range: e.g., 1mo, 3mo, 6mo, 1y (defaults to 1mo)
    """
    if yf is None:
        return jsonify({"error": "yfinance not installed. Run 'pip install yfinance'"}), 500

    ticker = (request.args.get('ticker') or '').upper().strip()
    period = request.args.get('range', '1mo')

    if not ticker:
        return jsonify({"error": "Missing 'ticker' query parameter"}), 400

    try:
        data = yf.Ticker(ticker).history(period=period)
        if data.empty:
            return jsonify({"error": f"No data returned for ticker {ticker}"}), 404
        return jsonify(as_json(data))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
