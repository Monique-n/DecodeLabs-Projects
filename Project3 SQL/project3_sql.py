import sqlite3
import pandas as pd

# 1. Load our clean data from Project 1
csv_file = "Clean_Online_Store_Orders.csv"
df = pd.read_csv(csv_file)

# 2. Connects to an in-memory SQL database engine
conn = sqlite3.connect(":memory:")

# 3. Transfers the clean data into a SQL table named 'Orders'
df.to_sql("Orders", conn, index=False, if_exists="replace")
print(" SQL DATABASE ENGINE ")
print("The 'Orders' table is ready for query testing.\n")


# QUERY 1: GLOBAL REVENUE & ORDER COUNT AUDIT
print(" SQL QUERY 1: GLOBAL METRICS ")
sql_query_1 = """
SELECT 
    COUNT(OrderID) AS Total_Orders,
    SUM(TotalPrice) AS Total_Revenue
FROM Orders;
"""
result_1 = pd.read_sql_query(sql_query_1, conn)
print(result_1.to_string(index=False), "\n")


# QUERY 2: PRODUCT VOLUME RANKING
print(" SQL QUERY 2: PRODUCT ORDER COUNT RANKING ")
# Columns used: Product (Group), OrderID (Count)
sql_query_2 = """
SELECT 
    Product,
    COUNT(OrderID) AS Order_Count
FROM Orders
GROUP BY Product
ORDER BY Order_Count DESC;
"""
result_2 = pd.read_sql_query(sql_query_2, conn)
print(result_2.to_string(index=False), "\n")


# QUERY 3: HIGH-VALUE TRANSACTION ISOLATION
print(" SQL QUERY 3: PREMIUM HIGH-VALUE ORDERS (> $2000) ")
# Columns used: OrderID, CustomerID, Product, TotalPrice (Filtered via WHERE)
sql_query_3 = """
SELECT 
    OrderID,
    CustomerID,
    Product,
    TotalPrice
FROM Orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;
"""
result_3 = pd.read_sql_query(sql_query_3, conn)
# Displaying just the first 10 rows to keep the terminal readable
print(f"Total high-value records found: {len(result_3)}")
print(result_3.head(10).to_string(index=False), "\n")


# QUERY 4: SETTLEMENT INFRASTRUCTURE TOTALS
print(" SQL QUERY 4: PAYMENT METHOD TOTAL PERFORMANCE METRICS ")
# Columns used: PaymentMethod (Group), Quantity (Sum), TotalPrice (Sum)
sql_query_4 = """
SELECT 
    PaymentMethod,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue_Generated
FROM Orders
GROUP BY PaymentMethod
ORDER BY Total_Revenue_Generated DESC;
"""
result_4 = pd.read_sql_query(sql_query_4, conn)
print(result_4.to_string(index=False), "\n")
