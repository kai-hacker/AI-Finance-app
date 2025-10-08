// AI Finance App - Frontend (Level 1)
// Level 1: Fetch financial data from backend API and render candlestick chart
// Level 2: Add indicators overlay (SMA/EMA/RSI) and correlation views
// Level 3: Add forecast request to /api/forecast and display CI bands
// Level 4: Toggle DL model predictions
// Level 5: Chat UI to query AI assistant
// Level 6: Portfolio optimizer UI + RL bot simulator
// Level 7: Auth, saved portfolios, and unified dashboard

const API_BASE = 'http://127.0.0.1:5000';

const form = document.getElementById('ticker-form');
const message = document.getElementById('message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  message.textContent = 'Fetching data...';

  const ticker = document.getElementById('ticker').value.trim();
  const range = document.getElementById('range').value;

  if (!ticker) {
    message.textContent = 'Please enter a ticker.';
    return;
  }

  try {
    const url = new URL(`${API_BASE}/api/quotes`);
    url.searchParams.set('ticker', ticker);
    url.searchParams.set('range', range);
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Request failed: ${res.status}`);
    const data = await res.json();

    renderCandlestick(data);
    message.textContent = `Loaded ${ticker} (${range})`;
  } catch (err) {
    console.error(err);
    message.textContent = `Error: ${err.message}`;
  }
});

function renderCandlestick(data) {
  // data: { dates:[], open:[], high:[], low:[], close:[], volume:[] }
  const trace = {
    x: data.dates,
    open: data.open,
    high: data.high,
    low: data.low,
    close: data.close,
    type: 'candlestick',
    name: 'OHLC'
  };

  const layout = {
    title: 'Candlestick',
    xaxis: { rangeslider: { visible: false } },
    yaxis: { title: 'Price' },
    margin: { t: 40, r: 20, b: 40, l: 50 }
  };

  Plotly.newPlot('candlestick', [trace], layout, { responsive: true });
}
