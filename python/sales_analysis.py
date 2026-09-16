import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

data = pd.read_csv("../data/sales_data.csv")

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])


# ==========================================
# 2. BASIC DATA INFORMATION
# ==========================================

print("=" * 50)
print("SALES ANALYTICS REPORT")
print("=" * 50)

print("\nFirst 5 Records:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())


# ==========================================
# 3. TOTAL SALES AND PROFIT
# ==========================================

total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_quantity = data["Quantity"].sum()

print("\n" + "=" * 50)
print("OVERALL PERFORMANCE")
print("=" * 50)

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)


# ==========================================
# 4. PROFIT MARGIN
# ==========================================

profit_margin = (total_profit / total_sales) * 100

print("Overall Profit Margin:", round(profit_margin, 2), "%")


# ==========================================
# 5. SALES BY PRODUCT
# ==========================================

product_sales = (
    data.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.idxmax()

print("\n" + "=" * 50)
print("SALES BY PRODUCT")
print("=" * 50)

print(product_sales)
print("\nBest-Selling Product:", best_product)


# ==========================================
# 6. PROFIT BY PRODUCT
# ==========================================

product_profit = (
    data.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

most_profitable_product = product_profit.idxmax()

print("\nProfit by Product:")
print(product_profit)

print("\nMost Profitable Product:", most_profitable_product)


# ==========================================
# 7. SALES BY REGION
# ==========================================

region_sales = (
    data.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_region = region_sales.idxmax()

print("\n" + "=" * 50)
print("SALES BY REGION")
print("=" * 50)

print(region_sales)
print("\nBest-Performing Region:", best_region)


# ==========================================
# 8. PROFIT BY REGION
# ==========================================

region_profit = (
    data.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

most_profitable_region = region_profit.idxmax()

print("\nProfit by Region:")
print(region_profit)

print("\nMost Profitable Region:", most_profitable_region)


# ==========================================
# 9. MONTHLY SALES
# ==========================================

monthly_sales = (
    data.groupby(data["Date"].dt.month)["Sales"]
    .sum()
)

best_month = monthly_sales.idxmax()

print("\n" + "=" * 50)
print("MONTHLY SALES")
print("=" * 50)

print(monthly_sales)
print("\nBest Sales Month:", best_month)


# ==========================================
# 10. MONTHLY PROFIT
# ==========================================

monthly_profit = (
    data.groupby(data["Date"].dt.month)["Profit"]
    .sum()
)

best_profit_month = monthly_profit.idxmax()

print("\nMonthly Profit:")
print(monthly_profit)

print("\nMost Profitable Month:", best_profit_month)


# ==========================================
# 11. TOP 5 ORDERS BY SALES
# ==========================================

top_orders = (
    data.sort_values("Sales", ascending=False)
    .head(5)
)

print("\n" + "=" * 50)
print("TOP 5 ORDERS")
print("=" * 50)

print(
    top_orders[
        ["Order_ID", "Product", "Sales", "Profit", "Region"]
    ]
)


# ==========================================
# 12. AVERAGE ORDER VALUE
# ==========================================

average_order_value = data["Sales"].mean()

print("\nAverage Order Value:", round(average_order_value, 2))


# ==========================================
# 13. PRODUCT QUANTITY SOLD
# ==========================================

product_quantity = (
    data.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

most_sold_product = product_quantity.idxmax()

print("\n" + "=" * 50)
print("PRODUCT QUANTITY")
print("=" * 50)

print(product_quantity)
print("\nMost Units Sold:", most_sold_product)


# ==========================================
# 14. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 50)
print("FINAL BUSINESS SUMMARY")
print("=" * 50)

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Profit Margin:", round(profit_margin, 2), "%")
print("Best-Selling Product:", best_product)
print("Most Profitable Product:", most_profitable_product)
print("Best Region:", best_region)
print("Most Profitable Region:", most_profitable_region)
print("Best Sales Month:", best_month)
print("Most Profitable Month:", best_profit_month)
print("Average Order Value:", round(average_order_value, 2))
print("Most Units Sold:", most_sold_product)

print("\nAnalysis Completed Successfully!")
