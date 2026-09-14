# DecodeLabs E-Commerce Analytics Suite

A complete engineering and business intelligence suite that transforms raw, volatile transactional order logs (`Online-Store-Orders.xlsx`) into standardized single-source-of-truth datasets, statistical exploratory models, optimized relational schemas, and an interactive executive web dashboard.

## Project Modules

### 1. Data Cleaning & Preprocessing (`Project1-DataCleaning/`)
* **Objective:** Ingest and sanitize raw transactional order logs containing formatting anomalies, missing fields, and rogue whitespace.
* **Engineering Deliverables:**
  * **Dynamic Imputation:** Tagged missing `CouponCode` attributes with default placeholder identifiers, preserving valid transaction rows without listwise deletion.
  * **Temporal Standardization:** Standardized disparate date strings into ISO 8601 compliant formatting (`YYYY-MM-DD`).
  * **Entity Integrity:** Applied strict primary key uniqueness constraints on `OrderID` fields to prevent duplicate transaction counting.

### 2. Exploratory Data Analysis (`Project2-EDA/`)
* **Objective:** Conduct rigorous parametric and non-parametric statistical audits across revenue streams, product distributions, and payment methods.
* **Engineering Deliverables:**
  * **Statistical Profiling:** Computed five-number financial summaries (Mean, Standard Deviation, Median, IQR) to isolate skewed transaction amounts.
  * **Revenue Concentration:** Mapped top-performing product lines and analyzed unit price variance across ordering channels.

### 3. Relational Database & SQL Analytics (`Project3-SQL/`)
* **Objective:** Structure flattened transaction records into an optimized relational schema and run complex analytical SQL queries.
* **Engineering Deliverables:**
  * **Relational Schema Design:** Built normalized SQLite tables enforcing primary keys, foreign key constraints, and strict data types.
  * **Analytical Queries:** Wrote optimized SQL queries using `GROUP BY` aggregations, CTEs, subqueries, and window functions to evaluate regional growth and customer purchasing frequency.

### 4. Interactive Web Dashboard (`Project4-Visualization/`)
* **Objective:** Deploy an interactive, web-based analytics dashboard allowing business stakeholders to explore transactional trends in real time.
* **Engineering Deliverables:**
  * **Interactive Controls:** Integrated dynamic date range, category, and payment channel filters powered by Streamlit and Matplotlib.
  * **Executive Metrics:** Designed responsive KPI cards tracking net revenue, order volumes, and average transaction value (AOV).

---

## Repository Structure

```text
DecodeLabs-Projects/
├── Project1-DataCleaning/       # Python cleaning scripts, missing value imputation, date parsing
├── Project2-EDA/                # Exploratory notebooks, statistical models, distributions
├── Project3-SQL/                # Database DDL scripts, relational schemas, analytical SQL queries
├── Project4-Visualization/      # Streamlit web application, dashboard layouts, custom charts
├── requirements.txt             # Environment dependencies
└── README.md                    # System architecture & documentation
Environment & Tooling
Language: Python 3.10+

Data Manipulation: Pandas, NumPy

Database & SQL: SQLite, Relational Schema Design, SQL Queries

Dashboard & Visualization: Streamlit, Matplotlib, Seaborn

Environment Control: Git, GitHub Desktop, Virtualenv (venv)
