# API Overview

Current (Level 1):
- GET `/api/health` – Health check
- GET `/api/quotes?ticker=SYMBOL&range=1mo` – OHLCV data via yfinance

Planned:
- Level 2: `/api/indicators` (SMA/EMA/RSI), `/api/correlation`
- Level 3: `/api/forecast` – ML forecasts (sklearn)
- Level 4: `/api/dl-forecast` – DL forecasts (LSTM/GRU)
- Level 5: `/api/assistant` – LLM-powered Q&A
- Level 6: `/api/optimize`, `/api/rl-sim` – Portfolio + RL
- Level 7: Auth, rate limiting, API gateway notes
