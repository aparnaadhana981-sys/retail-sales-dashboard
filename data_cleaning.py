import pandas as pd

# Simulating Raw Retail Sales Data
raw_data = {
    'OrderID':,
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Mouse'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Quantity': [2, 5, 1, 3, pd.NA],  # Missing value handling simulation
    'Price_Per_Unit':,
    'Region': ['North', 'East', 'West', 'South', 'North']
}

df = pd.DataFrame(raw_data)

# Data Cleaning: Filling missing values in Quantity with 1
df['Quantity'] = df['Quantity'].fillna(1)

# Feature Engineering: Calculating Total Sales Amount
df['Total_Sales'] = df['Quantity'] * df['Price_Per_Unit']

# Saving Cleaned Data for Power BI / Excel Dashboard
df.to_csv('cleaned_retail_sales.csv', index=False)
print("Retail data cleaned and exported successfully!")
