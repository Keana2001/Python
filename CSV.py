import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mall_Customers.csv') 

# print information 
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

df.columns = ['CustomerID', 'Gender', 'Age', 'AnnualIncome', 'SpendingScore']

# Summary statistics
print(df.describe())

# Make graph
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='AnnualIncome', y='SpendingScore', hue='Gender', palette='coolwarm')
plt.title('Spending Score vs Annual Income')
plt.show()
