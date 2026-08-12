# Logistics KPI Reporting System

## Overview

This project simulates a logistics KPI reporting pipeline for an e-commerce operation.

The system generates shipment performance data, stores the data in a SQLite database, queries the database using SQL, and automatically produces an Excel KPI report.

## Data Pipeline

Python Data Generation
        ↓
SQLite Database
        ↓
SQL KPI Queries
        ↓
Python/Pandas
        ↓
Excel KPI Report
        ↓
Management Insights

## KPIs

The reporting system tracks:

- On-time delivery percentage by region
- Average cost per shipment by month
- Shipment delay causes

## Tools

- Python
- Pandas
- NumPy
- SQL
- SQLite
- OpenPyXL
- Matplotlib
- Excel

## Business Questions

The analysis helps answer:

1. Which regions have the strongest delivery performance?
2. How is average shipping cost changing over time?
3. What are the most common causes of shipment delays?

## Key Insight

The analysis identifies regional delivery performance, monthly shipping cost trends, and the most common operational causes of delays.

## How to Run

1. Install Python dependencies.
2. Run `01_build_database.py`.
3. Run `02_kpi_queries.py`.
4. Run `03_create_chart.py`.

The scripts generate the SQLite database, Excel KPI report, and cost trend visualization.
