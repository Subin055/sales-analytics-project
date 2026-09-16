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
