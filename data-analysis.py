import pandas as pd

# Task 1: Data Loading and Cleaning

# 1. Load the dataset
df = pd.read_csv("products-100.csv")

# 2. Display the first few rows
print("First 5 rows:")
print(df.head())

# 3. Explore dataset structure
print("\nDataset info:")
print(df.info())

# 4. Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 5. Clean dataset
# Option A: Drop missing rows
# df = df.dropna()

# Option B: Fill missing values (example: numeric columns with mean, text columns with mode)
df = df.fillna({
    col: df[col].mean() if df[col].dtype != "object" else df[col].mode()[0]
    for col in df.columns
})

print("\nAfter cleaning, missing values per column:")
print(df.isnull().sum())

# Task 2: Data Analysis
import pandas as pd

# Load dataset
df = pd.read_csv("products-100.csv")

# 1. Basic statistics for numerical columns
print("📊 Basic Statistics:\n")
print(df.describe())

# 2. Group by a categorical column (example: Category) and compute mean Price
print("\n📂 Average Price per Category:\n")
grouped = df.groupby("Category")["Price"].mean()
print(grouped)

# 3. Optional: Highlight findings
print("\n🔎 Interesting Findings:")
print("- Categories with the highest and lowest average prices:")
print("   Highest:", grouped.idxmax(), "→", grouped.max())
print("   Lowest:", grouped.idxmin(), "→", grouped.min())

#Task 3: Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("products-100.csv")

# 1. Line Chart – Stock trend by Index (simulating time series)
plt.figure(figsize=(8,5))
plt.plot(df["Index"], df["Stock"], marker="o", linestyle="-", label="Stock")
plt.title("📈 Stock Trend by Index")
plt.xlabel("Index (as time order)")
plt.ylabel("Stock Quantity")
plt.legend()
plt.show()

# 2. Bar Chart – Average Price per Category
plt.figure(figsize=(10,6))
df.groupby("Category")["Price"].mean().sort_values().plot(kind="bar", color="skyblue")
plt.title("💰 Average Price per Category")
plt.xlabel("Category")
plt.ylabel("Average Price (USD)")
plt.xticks(rotation=45, ha="right")
plt.show()

# 3. Histogram – Price distribution
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=10, color="orange", edgecolor="black")
plt.title("📊 Price Distribution")
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot – Price vs Stock
plt.figure(figsize=(8,5))
sns.scatterplot(x="Price", y="Stock", hue="Category", data=df, palette="Set2", s=100, alpha=0.7)
plt.title("⚖️ Relationship between Price and Stock")
plt.xlabel("Price (USD)")
plt.ylabel("Stock Quantity")
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
