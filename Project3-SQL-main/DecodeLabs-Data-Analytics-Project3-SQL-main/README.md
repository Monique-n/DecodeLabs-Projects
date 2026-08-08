# Relational Data Analysis & SQL Extraction Pipeline (Project 3)

## Project Overview
This repository focuses on Phase 3 of my data analytics track, shifting from dataframe-based manipulations into relational database architecture. The goal was to build a data pipeline that initializes a local, in-memory SQLite database, instantiates transactional schema constraints, and executes structural SQL queries to extract multi-metric business intelligence from 1,200 clean rows of store data.

## Core Objectives
* Initialize an in-memory SQL execution engine using Python's native `sqlite3` driver.
* Construct logical aggregations to audit gross metrics, order frequencies, and volume splits.
* Isolate high-value transaction outliers using precise operational row filtering.
* Evaluate absolute warehouse product movement against gross capital returns per payment channel.

## File Architecture
* `project3_sql.py`: Core automation script loading data, setting up the SQLite engine, and querying tables.
* `Clean_Online_Store_Orders.csv`: Polished source dataset acting as the flat-file record seed.
* `Project3_Report.pdf`: Final formal relational report containing annotated query outputs.

---

## Relational Queries & Data Insights

### Query 1: Global Metrics Audit
* **SQL Core Logic:** Evaluates full-table scale via `COUNT(OrderID)` and `SUM(TotalPrice)`.
* **Output:**
  * **Total Corporate Orders:** 1,200
  * **Gross Consolidated Revenue:** $1,264,761.96

### Query 2: Product Inventory & Order Frequency Ranking
* **SQL Core Logic:** Uses `GROUP BY Product` paired with an explicit `ORDER BY Order_Count DESC` sorting funnel.
* **Output:**
  * **Top Order Velocity Asset:** **Printers** lead the store with **181 separate transactions**, followed closely by Tablets (179) and Chairs (178).
  * **Operational Distinction:** While my Project 2 analysis identified Chairs as the highest absolute gross revenue driver ($195,620.11), this SQL inquiry proves that Printers maintain a higher transaction frequency, bringing in $195,612.61. The two primary core assets are separated by a razor-thin margin of just $7.50.

### Query 3: High-Value Transaction Isolation (> $2,000)
* **SQL Core Logic:** Leverages a strict row-level filter via `WHERE TotalPrice > 2000` to isolate premium checkouts.
* **Output:**
  * Out of 1,200 total records, **180 orders match the high-value profile** (exactly 15% of total business volume).
  * The top transaction isolated was order `ORD200789` (Customer `C57276` purchasing a Tablet) valued at **$3,456.40**.

### Query 4: Settlement Channel Total Performance Metrics
* **SQL Core Logic:** Groups data by payment method, aggregating absolute metrics through `SUM(Quantity)` and `SUM(TotalPrice)`.
* **Output:**
  * **Cash** and **Online Gateway** options physically move the most inventory items out of the facility (**753 units** and **731 units** respectively).
  * **Credit Cards** act as the primary capital generator for the business, securing the highest overall gross cash flow (**$263,847.63**) despite moving fewer raw units (712).

---

## Technical Replication & Environment Setup
To clone this project, instantiate the local relational database engine, and verify the query execution tables on your local machine, run the following commands:

```bash
# Clone the repository
git clone [https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project3-SQL.git](https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project3-SQL.git)

# Move into the project directory
cd DecodeLabs-Data-Analytics-Project3-SQL

# Run the relational SQL testing script
python project3_sql.py
