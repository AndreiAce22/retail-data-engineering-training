# Retail Data Engineering Platform

A hands-on retail data engineering project built with **Databricks, PySpark, Delta Lake, and Medallion Architecture**. The project demonstrates batch ingestion, incremental processing, data transformation, analytics, data quality validation, orchestration, and pipeline monitoring.

## Project Architecture

The pipeline organizes retail data into three layers:

- **Bronze:** Raw source data ingested into Delta tables.
- **Silver:** Cleaned and validated sales data, including duplicate checks and revenue calculations.
- **Gold:** Analytics-ready sales summaries for monthly, product, and store-level reporting.

## Technologies Used

- Databricks
- Apache Spark / PySpark
- Delta Lake
- SQL
- Medallion Architecture
- Databricks Jobs and Workflows
- Git and GitHub

## Pipeline Workflow

The `retail_data_pipeline` job orchestrates the following tasks:

1. `02_bronze_ingestion` — Ingest raw retail data.
2. `05_incremental_processing` — Process incremental sales batches while preventing duplicate sales IDs.
3. `03_silver_transformation` — Clean and validate sales records.
4. `04_gold_analytics` — Generate monthly, product, and store sales summaries.
5. `06_data_quality_checks` — Execute data quality checks.
6. `07_pipeline_validation` — Validate aggregate consistency between Silver and Gold.
7. `08_pipeline_monitoring` — Record table metrics, quality-check results, and audit information.

## Idempotency Testing

**Objective:** Verify that rerunning the pipeline with an already processed sales batch does not introduce duplicate sales records or increase the tested table row counts.

The `retail_data_pipeline` job was rerun successfully. The following results were verified:

| Table | Expected Rows | Actual Rows | Result |
|---|---:|---:|---|
| `bronze_sales` | 110 | 110 | PASS |
| `silver_sales` | 110 | 110 | PASS |
| `gold_monthly_sales` | 4 | 4 | PASS |
| `gold_product_sales` | 12 | 12 | PASS |
| `gold_store_sales` | 5 | 5 | PASS |

### Data Quality Verification

- Bronze sales contained 110 rows and 110 unique sale IDs.
- Silver sales contained 110 rows and 110 unique sale IDs.
- Sale IDs ranged from 1 to 110.
- Silver and Gold aggregate revenue and quantity totals reconciled.
- All seven tasks in the complete pipeline job succeeded.
- Three pipeline reconciliation checks passed.
- Six monitoring quality checks passed.
- Row-count metrics for eight Bronze, Silver, and Gold tables were recorded.

These results support idempotent behavior for the tested batch and outputs. Additional tests with genuinely new batches and conflicting records would further strengthen the verification.

## Monthly Sales Reconciliation

The following results were obtained from the Gold monthly sales summary and reconciled against Silver sales data.

| Month | Total Sales | Quantity | Revenue |
|---|---:|---:|---:|
| January 2026 | 38 | 102 | 986,200.00 |
| February 2026 | 33 | 76 | 552,000.00 |
| March 2026 | 34 | 88 | 800,000.00 |
| April 2026 | 5 | 12 | 33,000.00 |
| **Total** | **110** | **278** | **2,371,200.00** |

## Monitoring and Audit

The monitoring notebook records table row counts and quality-check outcomes. The pipeline audit log captures task execution status and related metadata, helping support troubleshooting and operational visibility.

## Project Outcome

This project demonstrates an end-to-end retail data engineering workflow using Databricks. It covers layered data processing, incremental batch handling, Delta Lake tables, SQL-based analytics, data quality validation, aggregate reconciliation, job orchestration, and operational monitoring.

The completed pipeline provides a foundation for further enhancements, including new-batch testing, improved error handling, and expanded validation.
