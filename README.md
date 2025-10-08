# AI Finance App

An evolving AI-powered finance web app built in 7 levels (from beginner to a full ecosystem). This repo is scaffolded for Level 1 with clear upgrade notes for Levels 2–7.

## Levels (Roadmap)
1. Basic Web App (Flask + finance API)
2. Data Science Integration (Pandas, indicators)
3. Machine Learning Forecast (Scikit-learn)
4. Deep Learning Enhancement (LSTM, PyTorch)
5. AI Assistant Integration (LangChain / OpenAI API)
6. Portfolio Optimization (CVXPY, RL)
7. Full Ecosystem (Cloud, Database, API Gateway)

## Project Structure (high-level)
```
frontend/          # Static frontend (HTML/CSS/JS) – Level 1 UI, later React
backend/           # Flask backend APIs – Level 1 routes, grows over levels
api/               # API docs/specs; routing notes
config/            # Environment variables & configuration
data/              # Sample datasets and preprocessing scripts
models/            # ML/DL models (stubs now)
notebooks/         # Jupyter notebooks for EDA/experiments
docs/              # Research notes, reports, design docs
tests/             # Unit/integration tests
requirements.txt   # Python dependencies
```

See `PROJECT_TRACKER.md` for detailed per-level TODOs and acceptance criteria.

## Quickstart (Level 1)

Prereqs: Python 3.10+ recommended.

1) Create and activate venv, then install deps

```powershell
python -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; pip install -r requirements.txt
```

2) Run the Flask server

```powershell
$env:FLASK_APP = "backend/app.py" ; $env:FLASK_ENV = "development" ; python backend/app.py
```

3) Open the UI
- Open `frontend/index.html` in your browser (or serve statically) and use the form to query a ticker (e.g., AAPL).

Notes:
- The frontend fetches `/api/quotes?ticker=...` from the Flask server running at `http://127.0.0.1:5000`.
- For cross-origin local testing, the backend enables CORS.

## What’s Implemented in Level 1
- Flask backend with:
	- `GET /api/health` – health check
	- `GET /api/quotes?ticker=SYMBOL` – returns OHLCV price data via yfinance
- Frontend with:
	- Simple form to input ticker
	- Fetches data and renders a basic candlestick chart (Plotly)

## Upgrade Notes (Levels 2–7)

Level 2 – Data Science Integration
- Add indicators (SMA/EMA/RSI), volatility, correlations
- Extend endpoints under `backend/api/indicators.py`
- Notebook-driven EDA in `notebooks/02_indicators.ipynb`

Level 3 – Machine Learning Forecast
- Add feature engineering and sklearn models in `models/ml/`
- New endpoints: `/api/forecast`
- Persist trained models under `models/artifacts/`

Level 4 – Deep Learning Enhancement
- Add LSTM/GRU models with PyTorch under `models/dl/`
- Training scripts and inference pipeline

Level 5 – AI Assistant Integration
- LLM tools via LangChain; endpoints under `backend/api/assistant.py`
- Keys configured in `config/.env` (see `.env.example`)

Level 6 – Portfolio Optimization & RL
- Optimizers with CVXPY in `models/portfolio/`
- RL env and agents under `models/rl/`

Level 7 – Full Ecosystem
- Add DB (PostgreSQL/MongoDB) connections in `backend/db/`
- Auth, background jobs, and API gateway docs in `api/`

---

## Security & Disclaimer
This project is for learning and research. Not financial advice. Manage API keys securely and respect rate limits.

## License
MIT