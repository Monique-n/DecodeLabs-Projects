import os
import pandas as pd

# FILE LOADING
input_file = "Online-Store-Orders.xlsx"
output_file = "Clean_Online_Store_Orders.csv"

# PHASE 1: STRATEGIC IMPUTATION (Handling the Gaps)
# The 'CouponCode' column has empty cells. Instead of deleting the rows
# (which ruins our metrics), we fill them with the string 'NO_COUPON'.
df = pd.read_excel(input_file)
df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
print("\nPhase 1 Complete: Missing coupons filled successfully.")

# PHASE 2: THE INTEGRITY AUDIT (Isolating Duplicates)
# To protect transaction tracking, our primary tracking key ('OrderID') must be unique.
# We drop any duplicate orders based on OrderID and keep only the first instance.
df.drop_duplicates(subset=['OrderID'], keep='first', inplace=True)
print("Phase 2 Complete: Duplicate OrderID check validated.")

# PHASE 3: DATA STANDARDIZATION (Format & Precision Updates)
# 1. Timeline: Force dates to use the universal ISO 8601 standard format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# 2. Text: Trim hidden trailing or leading whitespaces from categories
text_columns = ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource']
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# 3. Currency: Limit financial values strictly to 2 decimal placesdf['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)
print("Phase 3 Complete: Formats unified (Dates standardized, Text trimmed, Decimals fixed).")

# STEP 4: PORTFOLIO OUTPUT EXPORT
# Save the polished dataset as a clean CSV
df.to_csv(output_file, index=False)

print("Final clean row count: " + str(len(df)))
print("File saved as: " + output_file)
