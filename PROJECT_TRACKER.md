# AI Finance App – Project Tracker

Owner: You  
Repo: AI-Finance-app  
Date initialized: 2025-10-08  
Workflow: Step-by-step; no code changes unless explicitly requested. I’ll keep this file updated based on your prompts.

---

## Quick Status
- Overall phase: Planning
- Current focus: Awaiting your go-ahead to start Level 1 scope and tasks
- Next action (when you say): Confirm stack (Flask vs Streamlit vs FastAPI) and data source (Yahoo Finance vs AlphaVantage)

---

## Table of Contents
- Level 1 – Basic Web App (Hello Data!)
- Level 2 – Data Science Integration
- Level 3 – Machine Learning Forecast
- Level 4 – Deep Learning Enhancement
- Level 5 – AI Assistant Integration
- Level 6 – Portfolio Optimization & Reinforcement Learning
- Level 7 – AI Finance Ecosystem
- Backlog & Ideas
- Decision Log
- Changelog

---

## Level 1 – Basic Web App (Hello Data!)
Goal: Build your first web app that shows real financial data.

Learn:
- HTML, CSS, JavaScript
- Python (Flask / Streamlit / FastAPI)
- Financial data APIs (Yahoo Finance, AlphaVantage)

Features:
- User inputs a stock/asset symbol (e.g., AAPL, TSLA, BTC-USD)
- Display price, volume, basic candlestick chart

Outputs / Deliverables:
- Functional financial web app
- Understand flow: data → backend → frontend
- Portfolio project: “Basic Stock Visualization App”

Acceptance Criteria:
- [ ] Input form accepts common tickers and basic validation
- [ ] Live/daily data fetched from a reliable source
- [ ] Candlestick chart renders for selected date range
- [ ] Graceful errors for invalid symbols / API limits

Task Checklist (to refine together):
- [ ] Choose framework: Flask / Streamlit / FastAPI
- [ ] Choose data source: Yahoo Finance (yfinance) / AlphaVantage
- [ ] Create minimal project structure & env
- [ ] Implement ticker input + basic routing
- [ ] Fetch OHLCV data for a selectable period
- [ ] Render candlestick + volume
- [ ] Basic styling and responsiveness
- [ ] Optional: Deploy preview (Render/Cloud/Local)

Status: Not started  
Notes: Pending your stack choice; we’ll scaffold after confirmation.

---

## Level 2 – Data Science Integration
Goal: Add financial analytics and data insights.

Learn:
- Pandas, NumPy, Matplotlib
- Exploratory Data Analysis (EDA)
- Technical indicators (SMA, EMA, RSI, etc.)

Features:
- Show indicators, volatility, correlations
- Mini dashboard for technical metrics

Outputs / Deliverables:
- Insightful analytics dashboard
- Mini research project: “Statistical Analysis of Stock Volatility”

Acceptance Criteria:
- [ ] At least 3 indicators (SMA/EMA/RSI) with configurable windows
- [ ] Daily/weekly volatility metric and plot
- [ ] Correlation heatmap for user-selected tickers

Task Checklist:
- [ ] Add indicators module (vectorized where possible)
- [ ] Compute rolling stats and volatility
- [ ] Multi-asset correlation view
- [ ] Charts with clear legends/tooltips

Status: Planned  
Notes: Depends on Level 1 data pipeline.

---

## Level 3 – Machine Learning Forecast
Goal: Add ML models to predict prices or trends.

Learn:
- Scikit-learn (Linear Regression, Random Forest, XGBoost)
- Time series feature engineering
- Model evaluation (MAE, RMSE, R²)

Features:
- 7-day price forecast
- Confidence intervals visualization
- Compare multiple ML models

Outputs / Deliverables:
- App includes “Forecast” module
- ML report (suitable for research/class submission)

Acceptance Criteria:
- [ ] Train/test split honoring time order
- [ ] Baseline vs at least 2 models compared
- [ ] Forecast plot with CI bands
- [ ] Metrics table (MAE, RMSE, R²)

Task Checklist:
- [ ] Feature engineering (lags, returns, rolling stats)
- [ ] Model selection + cross-validation
- [ ] Evaluation + visualization
- [ ] Caching for speed

Status: Planned  
Notes: Keep compute light; ensure reproducibility.

---

## Level 4 – Deep Learning Enhancement
Goal: Use Deep Learning for time series forecasting.

Learn:
- TensorFlow or PyTorch
- LSTM, GRU, 1D CNN, Transformer basics
- Normalization, scaling, seq2seq modeling

Features:
- LSTM-based trend prediction
- Predicted vs real price visualization
- “AI Trend Predictor” dashboard

Outputs / Deliverables:
- Real AI core in app
- Research idea: “Deep Learning for Financial Time Series Forecasting”
- Suitable for student conference publication

Acceptance Criteria:
- [ ] At least one DL architecture with tunable hyperparams
- [ ] Proper scaling + inverse transform
- [ ] Training/validation curves and test visualization

Task Checklist:
- [ ] Choose DL framework (TF/PyTorch)
- [ ] Data windowing + batching
- [ ] Model training + early stopping
- [ ] Save/Load models; inference pipeline

Status: Planned  
Notes: Consider GPU options later; keep fallback CPU path.

---

## Level 5 – AI Assistant Integration
Goal: Add conversational intelligence for user interaction.

Learn:
- LangChain / OpenAI API / RAG
- Natural language queries on financial data
- API design fundamentals

Features:
- Chatbot answers questions like:
  - “Why did AAPL drop today?”
  - “Which stock is less risky this week?”
- Generate automated financial reports via LLM

Outputs / Deliverables:
- LLM-enhanced financial assistant
- Research direction: “Conversational Financial AI Assistant”

Acceptance Criteria:
- [ ] Prompting strategy documented
- [ ] Retrieval grounded in the app’s data (RAG optional)
- [ ] Safety and limitation disclaimers

Task Checklist:
- [ ] Integrate LLM provider (keys via env)
- [ ] Build chat UI + backend endpoint
- [ ] Optional RAG over analytics + news
- [ ] Report generation (PDF/Markdown)

Status: Planned  
Notes: Will require API keys and usage guardrails.

---

## Level 6 – Portfolio Optimization & Reinforcement Learning
Goal: Integrate AI for financial decision-making.

Learn:
- Portfolio theory (mean-variance, Sharpe ratio)
- Convex optimization (CVXPY)
- Reinforcement Learning (Q-learning, Policy Gradient)

Features:
- “Portfolio Optimizer” – suggest best investment allocation
- “RL Trading Bot” – simulate AI trading decisions

Outputs / Deliverables:
- AI-powered decision modules
- Publishable research (forecasting, RL, optimization)

Acceptance Criteria:
- [ ] Mean-variance optimizer with constraints
- [ ] Backtesting with transaction costs
- [ ] RL agent benchmarked vs baseline

Task Checklist:
- [ ] Historical returns + risk modeling
- [ ] Optimization with CVXPY + constraints
- [ ] RL environment + policy training
- [ ] Backtest + performance metrics

Status: Planned  
Notes: Clearly label as simulation; not financial advice.

---

## Level 7 – AI Finance Ecosystem
Goal: Scale it into a real ecosystem product.

Learn:
- Cloud (AWS/GCP/Render)
- Database (PostgreSQL/MongoDB)
- Scalable backend + API gateway
- UX & product thinking

Features:
- User accounts and saved portfolios
- Unified dashboard: Market + Forecast + Portfolio
- Public API for other developers
- Integrate news sentiment, crypto, and macro data

Outputs / Deliverables:
- Real AI Finance Ecosystem
- Startup-ready showcase
- Excellent foundation for scholarships or conference papers

Acceptance Criteria:
- [ ] Auth + persistence for user data
- [ ] Background jobs/scheduling
- [ ] API rate limits + documentation
- [ ] Basic observability (logs/metrics)

Task Checklist:
- [ ] Choose cloud + managed DB
- [ ] Auth, sessions, and secure storage
- [ ] API versioning and docs
- [ ] Deployment pipeline (CI/CD)

Status: Planned  
Notes: Security, privacy, and cost controls are key.

---

## Backlog & Ideas
- News and social sentiment ingestion
- Macro data overlays (rates, CPI, jobs)
- Crypto and on-chain metrics
- Options data and Greeks
- Factor models (Fama-French)

---

## Decision Log
- 2025-10-08: Project tracking initialized; awaiting stack choice for Level 1

---

## Changelog
- 2025-10-08: Created PROJECT_TRACKER.md with 7-level roadmap and acceptance criteria placeholders