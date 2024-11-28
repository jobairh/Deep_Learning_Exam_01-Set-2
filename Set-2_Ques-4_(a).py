import pandas as pd

df = pd.read_csv('sales.csv')
print("Dataset loaded:\n", df.head())

missing_values = df[['Quantity', 'UnitPrice']].isnull().sum()
print("Checking for missing values:\n", missing_values)

# I have used df[['Quantity', 'UnitPrice']].isnull().sum() to check for missing values and 
# it will return the number of missing (NaN) values in each column

df['Quantity'].fillna(df['Quantity'].median(), inplace=True)
df['UnitPrice'].fillna(df['UnitPrice'].median(), inplace=True)

missing_values_after = df[['Quantity', 'UnitPrice']].isnull().sum()
print("Missing values after handling:\n", missing_values_after)

df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df['Year'] = df['OrderDate'].dt.year 

print("Data with 'Year' extracted from 'OrderDate'\n:", df.head())
