# Python-Assignment-Wk7

# Task 1
# 📊 Products-100 Dataset Analysis

This project shows how to load, explore, and clean a dataset (`products-100.csv`) using **Python** and **pandas**.

---

## 🚀 Usage

Save the following script as `analysis.py`:

```python
import pandas as pd

# Load dataset
df = pd.read_csv("products-100.csv")

# Show first rows
print("First 5 rows:\n", df.head())

# Dataset info
print("\nInfo:")
print(df.info())

# Missing values
print("\nMissing values:\n", df.isnull().sum())

# Clean data: fill numeric with mean, text with mode
df = df.fillna({
    col: df[col].mean() if df[col].dtype != "object" else df[col].mode()[0]
    for col in df.columns
})

print("\nAfter cleaning:\n", df.isnull().sum())
