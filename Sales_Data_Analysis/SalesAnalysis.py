import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv("sales_dataset_250_rows_clean.csv")

# Display first 5 rows
print(df.head())

# Dataset size
print("\nDataset Shape:")
print(df.shape)

# Column information
print("\nDataset Information:")
print(df.info())

# Column names
print("\nColumn Names:")
print(df.columns)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Handle missing values

df["Customer"] = df["Customer"].fillna("Unknown")
df["Payment Method"] = df["Payment Method"].fillna("Unknown")

# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

# Check data types
print("\nData Types After Formatting:")
print(df.dtypes)



# ==============================
# SALES ANALYSIS
# ==============================

# Total Sales
total_sales = df["Sales"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

# Average Sales per Order
average_sales = df["Sales"].mean()

print("\n===== KEY PERFORMANCE INDICATORS =====")
print("Total Sales:", total_sales)
print("Total Orders:", total_orders)
print("Average Sales per Order:", average_sales)

# ==============================
# TOP-SELLING PRODUCTS
# ==============================

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP-SELLING PRODUCTS =====")
print(product_sales)


# ==============================
# REGIONAL SALES ANALYSIS
# ==============================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== REGIONAL SALES =====")
print(region_sales)

df["Month"] = df["Order Date"].dt.month

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .sort_index()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# ==============================
# MONTHLY SALES CHART
# ==============================

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# ==============================
# REGIONAL SALES CHART
# ==============================

plt.figure(figsize=(8, 5))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Regional Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# TOP PRODUCTS CHART
# ==============================

top_products = product_sales.sort_values(ascending=True)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top-Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.show()

# ==============================
# CATEGORY-WISE SALES ANALYSIS
# ==============================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

# ==============================
# CATEGORY-WISE SALES CHART
# ==============================

plt.figure(figsize=(9, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ==============================
# BUSINESS INSIGHTS
# ==============================

print("\n===== BUSINESS INSIGHTS =====")

# 1. Best-selling product
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print(f"1. Best-selling product: {best_product}")
print(f"   Sales: {best_product_sales:,.2f}")

# 2. Best-performing region
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()

print(f"\n2. Best-performing region: {best_region}")
print(f"   Sales: {best_region_sales:,.2f}")

# 3. Best-performing month
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print(f"\n3. Highest sales month: {best_month}")
print(f"   Sales: {best_month_sales:,.2f}")

# 4. Best-selling category
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print(f"\n4. Best-selling category: {best_category}")
print(f"   Sales: {best_category_sales:,.2f}")

# 5. Lowest-performing region
lowest_region = region_sales.idxmin()
lowest_region_sales = region_sales.min()

print(f"\n5. Lowest-performing region: {lowest_region}")
print(f"   Sales: {lowest_region_sales:,.2f}")