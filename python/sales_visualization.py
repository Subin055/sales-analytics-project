import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
data = pd.read_csv("../data/sales_data.csv")

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])


# ==========================================
# 1. SALES BY PRODUCT
# ==========================================

product_sales = data.groupby("Product")["Sales"].sum()

plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")

plt.title("Sales by Product")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.savefig("../dashboard/sales_by_product.png")
plt.close()


# ==========================================
# 2. SALES BY REGION
# ==========================================

region_sales = data.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 6))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../dashboard/sales_by_region.png")
plt.close()


# ==========================================
# 3. MONTHLY SALES
# ==========================================

monthly_sales = data.groupby(
    data["Date"].dt.month
)["Sales"].sum()

plt.figure(figsize=(8, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../dashboard/monthly_sales.png")
plt.close()


# ==========================================
# 4. PROFIT BY PRODUCT
# ==========================================

product_profit = data.groupby("Product")["Profit"].sum()

plt.figure(figsize=(10, 6))
product_profit.sort_values().plot(kind="barh")

plt.title("Profit by Product")
plt.xlabel("Profit")
plt.ylabel("Product")

plt.tight_layout()
plt.savefig("../dashboard/profit_by_product.png")
plt.close()


print("All charts created successfully!")
