# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational tutorial that teaches AI-assisted development workflows. Students fork this repo and build a Streamlit e-commerce analytics dashboard using a spec-driven process: PRD → spec-kit planning → Jira tickets → Claude Code development → GitHub → Streamlit Cloud deployment.

The target application is a Python/Streamlit dashboard using Pandas and Plotly, analyzing sales data in `data/sales-data.csv` (482 transactions, 2024, across 5 product categories and 4 regions).

## Repository Structure

- `prd/ecommerce-analytics.md` — Product requirements document defining the dashboard to build
- `data/sales-data.csv` — Sample dataset (columns: date, order_id, product, category, region, quantity, unit_price, total_amount)
- `docs/` — Tutorial session guides, troubleshooting, and reference materials (not application code)

## Tech Stack

- **Python 3.11+** with **uv** for package management
- **Streamlit** for the web dashboard
- **Pandas** for data processing
- **Plotly** for interactive charts
- **Streamlit Community Cloud** for deployment

## Development Workflow

This project uses spec-kit for requirements planning and Jira for issue tracking via the Atlassian MCP server:

```bash
# Connect Claude Code to Jira
claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse

# Spec-kit workflow
specify init  # Initialize spec-kit planning
```

Commits should reference Jira issue keys (e.g., `ECOM-1: add sales dashboard`).

## Key Requirements from PRD

The dashboard must include: KPI summary cards (total sales, order count, avg order value, top category), sales trend chart, category breakdown, and regional analysis. Target: dashboard loads in under 5 seconds with ~$650K-$700K total sales across the dataset.

## Active Technologies
- Python 3.11+ + Streamlit, Pandas, Plotly (001-sales-dashboard)
- CSV file (`data/sales-data.csv`) — read-only (001-sales-dashboard)

## Recent Changes
- 001-sales-dashboard: Added Python 3.11+ + Streamlit, Pandas, Plotly
