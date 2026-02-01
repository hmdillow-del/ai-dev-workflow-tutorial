# Quickstart: E-Commerce Sales Analytics Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-01-31

## Prerequisites

- Python 3.11+
- Git

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

## Run the Dashboard

```bash
streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

## Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Pinned Python dependencies |
| `data/sales-data.csv` | Source sales dataset (482 transactions) |

## Verify

After launching, confirm:
- Total Sales shows ~$650,000-$700,000
- Total Orders shows 482
- Sales trend chart displays 12 months of 2024
- Category chart shows 5 categories sorted by revenue
- Region chart shows 4 regions sorted by revenue

## Deploy to Streamlit Community Cloud

1. Push the repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect the GitHub repository
4. Set main file path to `app.py`
5. Deploy
