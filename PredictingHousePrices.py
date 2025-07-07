from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target

# summary statistics
print("Summary statistics:\n", df.describe())

# Check if there are any missing values
print("\nMissing values =\n", df.isnull().sum())

# Plot first graph
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='twilight')
plt.title("Correlation Matrix")
plt.show()

# Plot second graph
sns.histplot(df['MedHouseVal'], bins=50, kde=True)
plt.title("Distribution of Median House Value")
plt.xlabel("Median House Value")
plt.show()
