# DecodeLabs E-Commerce Analytics Suite

A complete data analytics pipeline transforming raw, volatile transactional order logs into clean datasets, exploratory business insights, structured SQL databases, and interactive reporting dashboards.

---

##  Repository Structure

```text
DecodeLabs-Projects/
│
├── Project1-DataCleaning/       # Data sanitization, missing value imputation, schema standardization
├── Project2-EDA/                # Financial descriptive statistics, order trends, revenue analysis
├── Project3-SQL/                # Relational schema setup, query optimization, analytics reporting
└── Project4-Visualization/      # Interactive web application for executive data exploration
  Project Summaries
Project 1: Data Cleaning & Preprocessing
Objective: Transform a raw transactional dataset (Online-Store-Orders.xlsx) containing formatting errors, missing fields, and rogue whitespace into a standardized single source of truth.

Key Achievements:

Imputed missing CouponCode fields with dynamic default tags to preserve valid order records without listwise deletion.

Standardized timeline variables into standard ISO 8601 date formats (YYYY-MM-DD).

Enforced primary key uniqueness across OrderID records to eliminate duplicate transaction risks.

Project 2: Exploratory Data Analysis (EDA)
Objective: Audit order volumes, product revenue distributions, and payment channel performance using Python (pandas, numpy).

Key Insights:

Identified top-performing revenue categories and evaluated unit price variance across product lines.

Computed five-number financial summaries (mean, standard deviation, quartiles) across net order totals.

Project 3: Relational Database & SQL Analytics
Objective: Model transactional data into a relational database structure and execute analytical queries for operational decision-making.

Key Engineering Steps:

Designed table schemas with explicit data types and foreign key constraints.

Executed SQL queries covering aggregation (GROUP BY), window calculations, and segment-level filtering.

Project 4: Interactive Data Visualization
Objective: Build an accessible reporting UI for stakeholders to filter transactional trends dynamically.

Key Deliverables:

Built an interactive application interface to visualize key performance metrics, order volume changes, and payment channel breakdown.

  Environment & Tooling
Language: Python 

Data Processing: Pandas, NumPy

Database: SQL / SQLite

Visualization: Streamlit / Matplotlib

Version Control: Git, GitHub Desktop

