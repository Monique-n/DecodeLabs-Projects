# E-Commerce Transaction Logs - Exploratory Data Analysis (Project 2)

## Project Overview
This repository contains the documentation, code, and findings for Phase 2 of my data analytics track. The objective was to perform an extensive Exploratory Data Analysis (EDA) on a cleaned dataset of 1,200 retail records. By applying descriptive statistical summaries and categorical aggregations via Python and Pandas, I profiled customer acquisition trends, isolated financial gravity points, and evaluated underperforming inventory assets.

## Core Objectives
* Establish a foundational statistical baseline using five-number descriptive summaries.
* Aggregate and rank product class performance based on units sold and gross revenue.
* Audit marketing channel efficiency by tracking customer acquisition volume.
* Evaluate customer spending habits against operational settlement channels (AOV analysis).

## File Architecture
* `project2_EDA.py`: Main Python script utilizing Pandas for analytical data slicing and groupings.
* `Clean_Online_Store_Orders.csv`: Standardized transactional source dataset (1,200 unique order inputs).
* `Project2_Report.pdf`: Final structured executive report highlighting core findings.

---

## Technical Implementations & Findings

### 1. Financial descriptive Baseline
Using quantitative metrics, I generated a summary of the financial dataset to understand skewness and variance across transaction totals:
* **The Revenue Floor (Min Order):** $11.39
* **Median Spend (50th Percentile):** $823.62
* **Mean Spend (Average Order Value):** $1,053.97
* **The Revenue Ceiling (Max Order Anomaly):** $3,456.40

**Analytical Takeaway:** The data shows a significant right-skewed distribution. Because the mean ($1,053.97) sits substantially higher than the median ($823.62), it demonstrates that high-value enterprise orders or bulk consumer purchases near the $3,456.40 ceiling pull the mathematical averages upward, whereas half of daily routine checkouts remain under $823.62.

### 2. Product Revenue Matrix
Categorical grouping was executed on product classes to evaluate overall volume and actual capital returns:
* **Chairs & Printers** serve as the anchor assets of the portfolio, driving over $195,600 each.
* **Data Distinction:** A micro-level evaluation revealed that Chairs ($195,620.11) edge out Printers ($195,612.61) by a razor-thin margin of only $7.50.
* **Phones** represented the lower performance tier, generating the lowest gross revenue ($151,722.39) due to a lower volume of units sold.

### 3. Customer Acquisition & Payment Mechanics
* **Traffic Inflow:** Marketing channel distribution is highly competitive, but **Instagram** leads active customer conversions with 259 transactions, proving strong ad-spend performance on visual media assets.
* **Payment Architecture:** While Debit Cards show a lower baseline average ($1,001.56), **Credit Card transactions** yield the highest single-basket value with an Average Order Value of **$1,127.55**.

---

## How to Run the Analysis
To replicate the environment and generate the command-line statistical summary, ensure you have your dependencies installed and run:

```bash
# Clone the repository
git clone [https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project2-EDA.git](https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project2-EDA.git)

# Navigate into the project folder
cd DecodeLabs-Data-Analytics-Project2-EDA

# Execute the analysis pipeline
python project2_EDA.py
