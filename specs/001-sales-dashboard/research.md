# Research: E-Commerce Sales Analytics Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-01-31

## Technology Decisions

### Streamlit Application Structure

**Decision**: Single `app.py` file with helper functions for data loading and chart creation.

**Rationale**: The dashboard has only 4 components. Streamlit apps are conventionally single-file for this scale. The constitution explicitly recommends this approach. Splitting into modules adds import complexity without meaningful benefit for ~150 lines of code.

**Alternatives considered**:
- Multi-module structure (separate files for data, charts, layout) — rejected as over-engineering for this scope.
- Streamlit multipage app — rejected; only one page is needed.

### Data Loading Strategy

**Decision**: Use `@st.cache_data` to load and cache the CSV with Pandas. Parse dates during load with `pd.read_csv(..., parse_dates=["date"])`.

**Rationale**: `@st.cache_data` prevents re-reading the CSV on every Streamlit rerun (caused by user interaction or page refresh). Date parsing at load time avoids repeated conversion downstream.

**Alternatives considered**:
- `@st.cache_resource` — not appropriate for DataFrames; designed for database connections and ML models.
- No caching — would re-read CSV on every interaction, degrading performance.

### Chart Library

**Decision**: Plotly Express (`plotly.express`) for all charts.

**Rationale**: Plotly Express provides a high-level API that produces interactive charts with tooltips in a single function call. The constitution mandates Plotly (no matplotlib, no Streamlit native charts). Express API keeps code simple vs. the lower-level `plotly.graph_objects`.

**Alternatives considered**:
- `plotly.graph_objects` — more verbose, only needed for highly custom layouts.
- Altair — constitution prohibits; not in the approved stack.
- Streamlit native `st.line_chart` / `st.bar_chart` — constitution prohibits.

### KPI Display

**Decision**: Use `st.metric` for KPI cards, displayed in `st.columns`.

**Rationale**: `st.metric` is Streamlit's built-in component for displaying large numbers with labels. It renders as a visually prominent card and supports formatting. Using `st.columns` places them side-by-side for a dashboard layout.

**Alternatives considered**:
- Custom HTML with `st.markdown` — more flexible styling but harder to maintain and fragile.
- Plotly indicator charts — heavier than needed for simple number display.

### Currency Formatting

**Decision**: Format with `f"${value:,.0f}"` for display in KPI cards. Use Plotly's built-in tick formatting for chart axes.

**Rationale**: Python's format spec with comma grouping and zero decimal places matches the PRD requirement (e.g., "$650,000"). Plotly handles axis tick formatting natively.

### Deployment

**Decision**: Deploy to Streamlit Community Cloud directly from the GitHub repository.

**Rationale**: Streamlit Community Cloud reads `requirements.txt` from the repo root and runs `app.py` automatically. No Dockerfile or CI/CD pipeline needed. The constitution requires this deployment target.

**Alternatives considered**:
- Docker + cloud VM — unnecessary complexity for a read-only dashboard with a CSV data source.
- Heroku — requires additional configuration (Procfile, runtime.txt).
