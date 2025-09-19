import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/shree/Downloads/cafe_sales_dataset.csv")

# 1. Total Revenue
total_revenue = df["Total_Price"].sum()
print("Total Revenue:", total_revenue)

# 2. Top 3 Selling Items
top_items = df.groupby("Item")["Total_Price"].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Selling Items:\n", top_items)

# 3. Average Daily Sales
daily_sales = df.groupby("Date")["Total_Price"].sum()
print("\nAverage Daily Sales:", daily_sales.mean())

# 4. Popular Payment Method
payment_popularity = df["Payment_Method"].value_counts()
print("\nPayment Method Popularity:\n", payment_popularity)

# 5. Sales Trend Over Time
daily_sales.plot(kind="line", figsize=(8,5), title="Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()


