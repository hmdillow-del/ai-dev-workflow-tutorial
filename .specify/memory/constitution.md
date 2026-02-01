# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Simple, Readable Code
All code must be clear and understandable at a glance. Use descriptive variable and function names. Keep functions short and single-purpose. Avoid clever tricks or premature abstractions. Comments should explain *why*, not *what*. Follow PEP 8 style conventions consistently.

### II. User-Friendly Interactive Visualizations
Every chart must include clear titles, axis labels, and interactive tooltips. Use Plotly for all visualizations to ensure consistent interactivity. Currency values must be formatted with `$` and thousand separators. Layout should be clean and suitable for executive presentations. KPI cards must be immediately visible without scrolling.

### III. Python Best Practices
Use type hints for function signatures. Organize imports per PEP 8 (stdlib, third-party, local). Use `@st.cache_data` for data loading to avoid redundant reads. Keep the application in a single `app.py` file unless complexity warrants splitting. Use Pandas idioms (vectorized operations) over loops for data processing.

### IV. Virtual Environment and Dependency Isolation
Use Python virtual environments (`python -m venv .venv`) for all development. Pin dependencies in `requirements.txt` with exact versions for reproducibility. Never install packages globally. The `requirements.txt` must include only direct dependencies: `streamlit`, `pandas`, `plotly`.

### V. Data Integrity
Load data from `data/sales-data.csv` as the single source of truth. Parse dates explicitly during data loading. Validate that expected columns exist before processing. Never modify the source CSV file.

## Technical Constraints

- **Python 3.11+** required
- **Streamlit** for the web application framework
- **Pandas** for data loading and transformation
- **Plotly** for all charts (no matplotlib, no Streamlit native charts)
- **uv** for package management (or pip as fallback)
- Dashboard must load in under 5 seconds with the sample dataset
- Deployable to Streamlit Community Cloud without modification

## Development Workflow

- Commits must reference Jira issue keys (e.g., `ECOM-1: add KPI cards`)
- Each feature maps to a Jira ticket in the ECOM project
- Code changes go through GitHub pull requests
- Test the dashboard locally with `streamlit run app.py` before committing
- Scope is strictly Phase 1 as defined in the PRD; do not add features from Phase 2

## Governance

This constitution defines the standards for all code in the E-Commerce Analytics Dashboard project. All development work and code reviews must verify compliance with these principles. Amendments require updating this document and noting the change.

**Version**: 1.0 | **Ratified**: 2026-01-31 | **Last Amended**: 2026-01-31
