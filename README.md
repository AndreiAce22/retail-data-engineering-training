# Retail Data Engineering Platform

A hands-on data engineering project using Databricks, PySpark,
Delta Lake, and the Medallion Architecture.

## Architecture
- Bronze: Raw source data
- Silver: Cleaned and validated data
- Gold: Analytics-ready fact and dimension tables



## Idempotency Testing

**Objective:** Verify that rerunning the Databricks retail data pipeline does not duplicate sales records and preserves consistent analytics results.

### Test Results

The `retail_data_pipeline` job was executed a second time and completed successfully.

| Table | Expected Rows | Actual Rows | Result |
|---|---:|---:|---|
| `bronze_sales` | 110 | 110 | PASS |
| `silver_sales` | 110 | 110 | PASS |
| `gold_monthly_sales` | 4 | 4 | PASS |
| `gold_product_sales` | 12 | 12 | PASS |
| `gold_store_sales` | 5 | 5 | PASS |

### Data Quality Verification

- Bronze and Silver each contained 110 rows and 110 unique sale IDs.
- Sale IDs ranged from 1 to 110.
- Monthly sales totals in Silver matched the Gold monthly summary.
- The pipeline rerun did not increase the tested sales or Gold table row counts.

### Monthly Sales Reconciliation

| Month | Total Sales | Quantity | Revenue |
|---|---:|---:|---:|
| January 2026 | 38 | 102 | 986,200.00 |
| February 2026 | 33 | 76 | 552,000.00 |
| March 2026 | 34 | 88 | 800,000.00 |
| April 2026 | 5 | 12 | 33,000.00 |
| **Total** | **110** | **278** | **2,371,200.00** |

**Conclusion:** The tested pipeline rerun preserved sales record counts and Gold output counts, and monthly Silver-to-Gold totals reconciled successfully. This supports idempotent behavior for the tested data and outputs.
