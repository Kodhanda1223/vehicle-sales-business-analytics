import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/car_prices.csv", low_memory=False)

print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

# Data information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False))

# Duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Remove invalid records
df = df[
    (df["sellingprice"] > 100) &
    (df["year"].between(1990, 2016)) &
    (df["odometer"] >= 0)
].copy()

# Create price difference
df["price_difference"] = df["sellingprice"] - df["mmr"]

# Create vehicle age
df["vehicle_age"] = 2015 - df["year"]

# Create mileage category
df["mileage_category"] = pd.cut(
    df["odometer"],
    bins=[0, 30000, 70000, 100000, np.inf],
    labels=["Low", "Medium", "High", "Very High"]
)

# Top brands
top_brands = (
    df.groupby("make")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Brands:")
print(top_brands)

# Average selling price by brand
brand_price = (
    df.groupby("make")["sellingprice"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nHighest Average Selling Price by Brand:")
print(brand_price)

# Sales by state
state_sales = (
    df.groupby("state")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 States by Sales:")
print(state_sales)

# Mileage analysis
mileage_analysis = (
    df.groupby("mileage_category", observed=True)["sellingprice"]
    .mean()
)

print("\nAverage Price by Mileage Category:")
print(mileage_analysis)

# Visualization 1
top_brands.plot(
    kind="bar",
    figsize=(10, 5),
    title="Top Vehicle Brands by Sales Volume"
)

plt.xlabel("Vehicle Brand")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2
plt.figure(figsize=(10, 5))

plt.scatter(
    df["odometer"],
    df["sellingprice"],
    alpha=0.25
)

plt.title("Mileage vs Selling Price")
plt.xlabel("Mileage")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()

# Visualization 3
mileage_analysis.plot(
    kind="bar",
    figsize=(8, 5),
    title="Average Selling Price by Mileage Category"
)

plt.xlabel("Mileage Category")
plt.ylabel("Average Selling Price")
plt.tight_layout()
plt.show()

print("\nAnalysis completed successfully.")
