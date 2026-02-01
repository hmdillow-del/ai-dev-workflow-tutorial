import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    page_icon="📊",
    layout="wide",
)

EXPECTED_COLUMNS = [
    "date", "order_id", "product", "category",
    "region", "quantity", "unit_price", "total_amount",
]


@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/sales-data.csv", parse_dates=["date"])
    except FileNotFoundError:
        st.error("Data file not found: data/sales-data.csv")
        st.stop()

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        st.error(f"CSV is missing expected columns: {', '.join(sorted(missing))}")
        st.stop()

    return df


df = load_data()
