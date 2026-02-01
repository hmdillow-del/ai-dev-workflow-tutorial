# Data Model: E-Commerce Sales Analytics Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-01-31

## Source Entity: Transaction

The single source entity, loaded from `data/sales-data.csv`.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| date | Date | Transaction date | 2024-01-15 |
| order_id | String | Unique order identifier | ORD-001234 |
| product | String | Product name | Wireless Headphones |
| category | String | Product category (5 values) | Electronics |
| region | String | Geographic region (4 values) | North |
| quantity | Integer | Units sold | 2 |
| unit_price | Decimal | Price per unit | 49.99 |
| total_amount | Decimal | Total transaction value | 99.98 |

### Validation Rules

- All 8 columns must be present in the CSV header.
- `date` must be parseable as a date (format: YYYY-MM-DD).
- `total_amount` must be numeric for aggregation.

## Derived Aggregations

These are computed at runtime from the Transaction data. They are not stored.

### KPI Metrics

| Metric | Derivation |
|--------|------------|
| Total Sales | `sum(total_amount)` |
| Total Orders | `count(order_id)` |

### Monthly Sales (for trend chart)

Group by `date` truncated to month, then `sum(total_amount)`.

### Category Sales (for category chart)

Group by `category`, then `sum(total_amount)`. Sort descending.

### Regional Sales (for region chart)

Group by `region`, then `sum(total_amount)`. Sort descending.

## Enumerated Values

**Categories**: Electronics, Accessories, Audio, Wearables, Smart Home

**Regions**: North, South, East, West
