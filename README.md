# Python-Assignment-Wk7

## 📊 Dataset Analysis Project (products-100.csv)

This project demonstrates how to **load, clean, explore, analyze, and visualize** a dataset using **Python**, **pandas**, **matplotlib**, and **seaborn**.  
The dataset used is `products-100.csv`.

---

## 🚀 Workflow

```python
import pandas as pd

# Load dataset
df = pd.read_csv("products-100.csv")

# Inspect first rows
print(df.head())

# Check info and missing values
print(df.info())
print(df.isnull().sum())

# Clean missing values (fill numeric with mean, text with mode)
df = df.fillna({
    col: df[col].mean() if df[col].dtype != "object" else df[col].mode()[0]
    for col in df.columns
})

# Basic statistics(Task 2)

print(df.describe())

# Group by Category → average Price
grouped = df.groupby("Category")["Price"].mean()
print(grouped)

# Highlight min & max
print("Highest:", grouped.idxmax(), "→", grouped.max())
print("Lowest:", grouped.idxmin(), "→", grouped.min())


# Data Visualization (Task 3)
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line Chart – Stock trend
plt.plot(df["Index"], df["Stock"], marker="o")
plt.title("📈 Stock Trend by Index")
plt.xlabel("Index (as time order)")
plt.ylabel("Stock Quantity")
plt.show()

# 2. Bar Chart – Average Price per Category
df.groupby("Category")["Price"].mean().sort_values().plot(kind="bar", color="skyblue")
plt.title("💰 Average Price per Category")
plt.xlabel("Category")
plt.ylabel("Average Price (USD)")
plt.xticks(rotation=45)
plt.show()

# 3. Histogram – Price distribution
plt.hist(df["Price"], bins=10, color="orange", edgecolor="black")
plt.title("📊 Price Distribution")
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot – Price vs Stock
sns.scatterplot(x="Price", y="Stock", hue="Category", data=df, palette="Set2", s=100, alpha=0.7)
plt.title("⚖️ Price vs Stock")
plt.xlabel("Price (USD)")
plt.ylabel("Stock Quantity")
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
