import pandas as pd

# Load the sales dataset
data = pd.read_csv("../data/sales_data.csv")

# Display the first 5 rows
print(data.head())

# Calculate total sales
total_sales = data["Sales"].sum()

# Calculate total profit
total_profit = data["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Calculate sales by product
product_sales = data.groupby("Product")["Sales"].sum()

# Find the best-selling product
best_product = product_sales.idxmax()

print("\nSales by Product:")
print(product_sales)

print("Best-Selling Product:", best_product)

# Calculate sales by region
region_sales = data.groupby("Region")["Sales"].sum()

# Find the region with the highest sales
best_region = region_sales.idxmax()

print("\nSales by Region:")
print(region_sales)

print("Best-Performing Region:", best_region)
