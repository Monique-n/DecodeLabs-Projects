# Enterprise Store Performance & Transaction Analytics 
---
##  Live Interactive Dashboard
To interact with the live filter controls, adjust metrics, and explore the visualizations directly in your browser, click the web production application:

 **[ Live Visualisation dashboard](https://decodelabs-data-analytics-project4-visualisation-utksz3k5axn59.streamlit.app/)**

##  Project Objective
This project contains an end-to-end operational analytics engine and interactive intelligence dashboard designed to transition raw retail telemetry into dynamic executive insights. Utilizing a structured dataset of e-commerce transactions in **`Clean_Online_Store_Orders.csv`**, I engineered a programmatic data ingestion pipeline in Python, integrated advanced conditional chart aesthetics using Plotly, and built a low-latency, responsive web dashboard deployed natively via Streamlit.

**The Operational Result:** A high-fidelity control panel providing real-time filtering, revenue generation distribution arrays, full-width time-series tracking, and automated strategic decision recommendations.

---

##  Production App Structure
The workspace is decoupled into clear components to ensure high performance and strict layout isolation:
*  **`Clean_Online_Store_Orders.csv`**: The standardized transactional ledger housing metrics across order values, fulfillment tracking, coupon usage, and marketing acquisition channels.
*  **`Visualisation_app_2.py`**: The core production engine handling memory caching (`@st.cache_data`), responsive UI styling via custom CSS injection, and layout assembly.
*  **Theme Canvas Matrix**: A custom UI canvas utilizing a Lighter Deep Purple theme (`#221B33`) combined with high-contrast Graphite Black container surfaces (`#1A1C23`) to maximize scannability.
---

##  Core Technical Implementations

### 1. High-Density High-Contrast Metric Matrix
The top section of the dashboard instantly isolates core business health indicators through tailored HTML components with fluid hover-state transformations:
* **Total Revenue & Average Order Value (AOV):** Dynamic calculation fields handling programmatic currency masking.
* **Top Payment Channel & Top Referral Source:** Mode evaluation strings calculating underlying transaction velocities live based on active sidebar timeframes.

### 2. Multi-Dimensional Plotly Analytics Grid
The center layer deploys three high-density charts optimized for immediate executive comparison:
*  **Revenue Generation by Product:** A horizontal bar chart isolating the top-performing asset classes with sharp contextual highlight tracking.
*  **Order Status Volumes:** A color-coded velocity distribution chart providing immediate visual alerts on operational choke points (Delivered vs. Cancelled/Returned transactions).
*  **Coupon Code Utilization:** A customized donut chart using a sorted matrix that arranges promotional performance in a descending, counter-clockwise array starting at the top vertical axis to map market share precisely.

### 3. Chronological Revenue Performance Timeline
* **Time-Series Windowing:** Merges operating year and month integers into a uniform string period layout (`YYYY-MM`).
* **Continuous Line Interpolation:** Programmed a heavy 4-width line layer equipped with custom cross-sectional data markers to track long-term revenue shifts without visual clutter.

---

##  Local Deployment Guide
To host this relational web dashboard on a local instance for development or auditing:

1. **Clone the Project Workspace:**
```bash
git clone [https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project4-Visualisation.git](https://github.com/Monique-n/DecodeLabs-Data-Analytics-Project4-Visualisation.git)
cd DecodeLabs-Data-Analytics-Project4-Visualisation
