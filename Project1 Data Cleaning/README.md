# DecodeLabs Data Analytics Internship - Project 1
## Data Cleaning & Preparation

**Author:** Monica Nyambura George  
**Batch:** 2026  
**Domain:** Data Analytics  
**Status:** Completed & Validated  

---

## 1. Project Objective
The goal of this initiative was to transform a raw, volatile transactional tracking dataset (`Online-Store-Orders.xlsx`) containing 1,200 records into a production-ready, standardized single-source-of-truth dataset. By addressing logical anomalies, handling data gaps, and correcting format drifts, we protect downstream visualization and analytical models from calculation errors.

---

## 2. Executive Data Audit Checklist

| Phase | Target Area | Logic Applied / Action Taken | Business Impact |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Gaps & Missing Values | Imputed `NaN` locations inside the `CouponCode` metric with a static identifier string: `'NO_COUPON'`. | Prevents catastrophic Listwise Deletion. Preserved **309 records (25.7% of the dataset)** from being lost. |
| **Phase 2** | Record Integrity Audit | Enforced uniqueness constraints across the primary tracking entity key (`OrderID`). | Eliminated risk of transactional inflation. Confirmed a 100% unique row volume across all 1,200 entities. |
| **Phase 3** | Timeline Uniformity | Converted variable datetime patterns into the universal **ISO 8601 Standard** format (`YYYY-MM-DD`). | Ensures chronological uniformity across indexing engines and cross-database analytics engines. |
| **Phase 4** | Dimensional Text Alignment | Stripped rogue, trailing, and leading spaces from text arrays (`Product`, `PaymentMethod`, etc.). | Fixes hidden segmentation fragmentation during downstream aggregations (e.g., preventing 'Phone ' from grouping separately from 'Phone'). |
| **Phase 5** | Fiscal Financial Precision | Hard-coded monetary properties (`UnitPrice`, `TotalPrice`) to match strict decimal restrictions (`.round(2)`). | Eliminates floating-point precision display errors during fiscal calculations. |

---

## 3. Script Operational Metrics
* **Input Raw Records:** 1,200 Rows  
* **Output Polished Records:** 1,200 Rows  
* **Data Processing Integrity Level:** 100% Error-Free  
* **Final Saved Output Asset:** `Clean_Online_Store_Orders.csv`

---

## 4. How to Execute the Script
To reproduce this optimization pipeline, ensure you have the `pandas` and `openpyxl` dependencies installed via your terminal:

```bash
pip install pandas openpyxl
