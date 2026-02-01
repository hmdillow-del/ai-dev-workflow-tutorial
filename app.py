import streamlit as st
import pandas as pd
import plotly.express as px

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

# --- Phase 3: KPI Cards (US1) ---
st.title("ShopSmart Sales Dashboard")

total_sales = df["total_amount"].sum()
total_orders = len(df)

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")

st.divider()

# --- Phase 4: Monthly Sales Trend (US2) ---
st.subheader("Sales Trend Over Time")

monthly_sales = df.groupby(df["date"].dt.to_period("M")).agg(
    total_amount=("total_amount", "sum")
).reset_index()
monthly_sales["date"] = monthly_sales["date"].dt.to_timestamp()

fig_trend = px.line(
    monthly_sales,
    x="date",
    y="total_amount",
    title="Sales Trend Over Time",
    labels={"date": "Month", "total_amount": "Sales Amount"},
)
fig_trend.update_traces(hovertemplate="Month: %{x|%b %Y}<br>Sales: $%{y:,.0f}")
st.plotly_chart(fig_trend, use_container_width=True)

st.divider()

# --- Phase 5 & 6: Category and Region Charts (US3 & US4) ---
col_cat, col_reg = st.columns(2)

with col_cat:
    st.subheader("Sales by Category")
    category_sales = (
        df.groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig_cat = px.bar(
        category_sales,
        x="category",
        y="total_amount",
        title="Sales by Category",
        labels={"category": "Category", "total_amount": "Sales Amount"},
    )
    fig_cat.update_traces(hovertemplate="Category: %{x}<br>Sales: $%{y:,.0f}")
    st.plotly_chart(fig_cat, use_container_width=True)

with col_reg:
    st.subheader("Sales by Region")
    region_sales = (
        df.groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig_reg = px.bar(
        region_sales,
        x="region",
        y="total_amount",
        title="Sales by Region",
        labels={"region": "Region", "total_amount": "Sales Amount"},
    )
    fig_reg.update_traces(hovertemplate="Region: %{x}<br>Sales: $%{y:,.0f}")
    st.plotly_chart(fig_reg, use_container_width=True)
