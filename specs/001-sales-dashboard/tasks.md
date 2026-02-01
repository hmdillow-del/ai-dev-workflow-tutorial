# Tasks: E-Commerce Sales Analytics Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

**Tests**: Not requested in specification. Manual verification only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization — virtual environment, dependencies, and base application file

- [x] T001 Create Python virtual environment with `python -m venv .venv` and activate it
- [x] T002 Create `requirements.txt` at repository root with pinned dependencies: streamlit, pandas, plotly
- [x] T003 Install dependencies from `requirements.txt` into the virtual environment
- [x] T004 Create skeleton `app.py` at repository root with Streamlit page config (title: "ShopSmart Sales Dashboard"), page icon, and wide layout

---

## Phase 2: Foundational (Data Loading)

**Purpose**: CSV data loading function that ALL user stories depend on. MUST complete before any story work begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Implement `load_data()` function in `app.py` that reads `data/sales-data.csv` with `pd.read_csv`, parses the `date` column, and validates that all 8 expected columns exist
- [ ] T006 Decorate `load_data()` with `@st.cache_data` for caching in `app.py`
- [ ] T007 Add error handling in `app.py` to display `st.error()` message if CSV file is missing or columns are invalid (FR-009)

**Checkpoint**: Data loads successfully and is cached. Error handling works for missing file. User story implementation can now begin.

---

## Phase 3: User Story 1 - View Key Business Metrics (Priority: P1) 🎯 MVP

**Goal**: Display total sales revenue and total order count as prominent KPI cards at the top of the dashboard.

**Independent Test**: Open `http://localhost:8501`, verify total sales shows ~$650,000-$700,000 and total orders shows 482. Values must match manual CSV calculations.

### Implementation for User Story 1

- [ ] T008 [US1] Calculate KPI metrics in `app.py`: total sales (`df["total_amount"].sum()`), total orders (`len(df)`)
- [ ] T009 [US1] Display KPI cards using `st.columns` and `st.metric` in `app.py` with formatted currency (`$XXX,XXX`) for total sales and formatted integer for total orders
- [ ] T010 [US1] Add dashboard title header ("ShopSmart Sales Dashboard") using `st.title` in `app.py`

**Checkpoint**: Dashboard shows title and two KPI cards with correct, formatted values. This is the MVP — independently functional and testable.

---

## Phase 4: User Story 2 - Sales Trends Over Time (Priority: P2)

**Goal**: Display a Plotly line chart showing monthly sales trends across all 12 months of 2024.

**Independent Test**: Verify the line chart shows 12 data points (Jan–Dec 2024), hovering shows exact month and sales amount, axes are labeled clearly.

### Implementation for User Story 2

- [ ] T011 [US2] Aggregate monthly sales data in `app.py`: group by month from `date` column, sum `total_amount`
- [ ] T012 [US2] Create Plotly Express line chart in `app.py` with title "Sales Trend Over Time", labeled axes (Month, Sales Amount), and interactive tooltips showing formatted currency values
- [ ] T013 [US2] Render the trend chart in `app.py` using `st.plotly_chart` with `use_container_width=True`

**Checkpoint**: Dashboard shows KPIs (US1) plus a monthly trend line chart with 12 months, tooltips, and clear labels.

---

## Phase 5: User Story 3 - Category Breakdown (Priority: P3)

**Goal**: Display a Plotly bar chart showing total sales by product category, sorted highest to lowest.

**Independent Test**: Verify bar chart shows all 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) sorted descending by sales, with tooltips on hover.

### Implementation for User Story 3

- [ ] T014 [US3] Aggregate category sales data in `app.py`: group by `category`, sum `total_amount`, sort descending
- [ ] T015 [US3] Create Plotly Express bar chart in `app.py` with title "Sales by Category", labeled axes, sorted bars, and interactive tooltips with formatted currency values
- [ ] T016 [US3] Render the category chart in `app.py` using `st.plotly_chart` with `use_container_width=True`

**Checkpoint**: Dashboard shows KPIs (US1), trend chart (US2), and category bar chart with all 5 categories sorted by revenue.

---

## Phase 6: User Story 4 - Regional Breakdown (Priority: P4)

**Goal**: Display a Plotly bar chart showing total sales by geographic region, sorted highest to lowest.

**Independent Test**: Verify bar chart shows all 4 regions (North, South, East, West) sorted descending by sales, with tooltips on hover.

### Implementation for User Story 4

- [ ] T017 [US4] Aggregate regional sales data in `app.py`: group by `region`, sum `total_amount`, sort descending
- [ ] T018 [US4] Create Plotly Express bar chart in `app.py` with title "Sales by Region", labeled axes, sorted bars, and interactive tooltips with formatted currency values
- [ ] T019 [US4] Render the region chart in `app.py` using `st.plotly_chart` with `use_container_width=True`

**Checkpoint**: Dashboard shows all 4 components — KPIs, trend chart, category chart, and region chart. All user stories are complete.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Layout refinement and deployment readiness

- [ ] T020 [P] Arrange category and region charts side-by-side using `st.columns` in `app.py` for a professional two-column layout
- [ ] T021 [P] Add section dividers or subheaders between dashboard sections in `app.py` using `st.subheader` or `st.divider`
- [ ] T022 Verify all chart titles, axis labels, and tooltips are clear and professional in `app.py`
- [ ] T023 Run `streamlit run app.py` and validate against quickstart.md verification checklist (total sales ~$650K-$700K, 482 orders, 12 months, 5 categories, 4 regions)
- [ ] T024 [P] Add `.gitignore` entries for `.venv/` and `__pycache__/` if not already present

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Stories (Phases 3–6)**: All depend on Foundational phase completion
  - Stories can proceed sequentially in priority order (P1 → P2 → P3 → P4)
  - Since all tasks write to the same `app.py`, sequential execution is recommended
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 — no dependencies on other stories
- **User Story 2 (P2)**: Can start after Phase 2 — independent of US1 (but sequential recommended since same file)
- **User Story 3 (P3)**: Can start after Phase 2 — independent of US1/US2
- **User Story 4 (P4)**: Can start after Phase 2 — independent of US1/US2/US3

### Within Each User Story

- Aggregation before chart creation
- Chart creation before rendering
- All tasks within a story are sequential (same file)

### Parallel Opportunities

- T001, T002 can run in parallel (different files)
- T020, T021, T024 can run in parallel (different concerns / files)
- User stories are logically independent but share `app.py`, so sequential execution within a single developer is more practical

---

## Parallel Example: Phase 1 Setup

```bash
# These can run in parallel:
Task: "Create Python virtual environment with python -m venv .venv"
Task: "Create requirements.txt at repository root"
```

## Parallel Example: Phase 7 Polish

```bash
# These can run in parallel:
Task: "Arrange charts side-by-side using st.columns in app.py"
Task: "Add .gitignore entries for .venv/ and __pycache__/"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T004)
2. Complete Phase 2: Foundational data loading (T005–T007)
3. Complete Phase 3: KPI cards (T008–T010)
4. **STOP and VALIDATE**: Run `streamlit run app.py`, verify KPIs show correct values
5. Deploy/demo if ready — this alone delivers stakeholder value

### Incremental Delivery

1. Setup + Foundational → Data loads correctly
2. Add User Story 1 (KPIs) → Test → Commit (MVP!)
3. Add User Story 2 (Trend chart) → Test → Commit
4. Add User Story 3 (Category chart) → Test → Commit
5. Add User Story 4 (Region chart) → Test → Commit
6. Polish → Final validation → Deploy

### Commit Strategy

Each phase or user story completion is a natural commit point:
- `ECOM-X: set up project structure and dependencies`
- `ECOM-X: add data loading with caching and error handling`
- `ECOM-X: add KPI cards for total sales and orders`
- `ECOM-X: add monthly sales trend chart`
- `ECOM-X: add category breakdown chart`
- `ECOM-X: add regional breakdown chart`
- `ECOM-X: polish layout and finalize dashboard`

---

## Notes

- All implementation is in a single file (`app.py`) per constitution
- No test tasks generated — spec uses manual verification
- Each user story adds one visible component to the dashboard
- Commit after each completed user story with Jira issue key reference
- Validate against quickstart.md checklist before final deployment
