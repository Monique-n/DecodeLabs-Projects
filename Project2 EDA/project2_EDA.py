import os
import pandas as pd

# Defines our clean dataset from Project 1
file_name = "Clean_Online_Store_Orders.csv"

print("PHASE 1: EXPLORATORY DATA ANALYSIS")

# Loads the polished data
df = pd.read_csv(file_name)
print("Success! Loaded " + str(len(df)) + " clean records for analysis.\n")

# 1. GENERATES THE FIVE-NUMBER SUMMARY
print("   FINANCIAL DESCRIPTIVE STATISTICS   ")
# .describe() automatically calculates count, mean, min, 25%, 50%, 75%, and max
print(df[['Quantity', 'UnitPrice', 'TotalPrice']].describe().round(2))


print("\n PHASE 2: CATEGORICAL TREND ANALYSIS  ")


# 1. PRODUCT PERFORMANCE TRACKING
# Columns used: 'Product' (Group), 'Quantity' (Sum), 'TotalPrice' (Sum)
print("\n TOP SELLING PRODUCTS BY REVENUE ")
# Group by 'Product' and sum the total quantities sold and total revenue generated
product_summary = df.groupby('Product')[['Quantity', 'TotalPrice']].sum()
# Sorts the results so that the highest revenue earner sits at the very top
product_summary = product_summary.sort_values(by='TotalPrice', ascending=False)
print(product_summary.round(2))


# 2. REFERRAL SOURCE PERFORMANCE (Marketing Channels)
# Columns used: 'ReferralSource' (Group), 'OrderID' (Count)
print("\n TRAFFIC SOURCES DRIVING SALES VOLUME ")
# Groups by 'ReferralSource' and counts how many orders came from each platform
marketing_summary = df.groupby('ReferralSource')['OrderID'].count()
# Sorts a Series from highest value to lowest directly, then converts to a clean table
marketing_summary = marketing_summary.sort_values(
    ascending=False).to_frame(name='Reference Count')
print(marketing_summary)


# 3. PAYMENT METHOD PREFERENCES
# Columns used: 'PaymentMethod' (Group), 'TotalPrice' (Mean/Average)
print("\n CUSTOMER PAYMENT PREFERENCES ")
# Groups by 'PaymentMethod' and calculates the average order size (TotalPrice) for each
payment_summary = df.groupby('PaymentMethod')['TotalPrice'].mean()
# Sorts a Series from highest value to lowest directly, then converts to a clean table
payment_summary = payment_summary.sort_values(
    ascending=False).to_frame(name='Average Order Value')
print(payment_summary.round(2))
