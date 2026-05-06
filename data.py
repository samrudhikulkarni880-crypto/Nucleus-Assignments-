import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load and Inspect Data
df = pd.read_csv("data.csv")

print("First 5 rows:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# 2. Data Cleaning
for col in df.select_dtypes(include='number').columns:
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 3. Filter Data
filtered_df = df[(df['age'] > 30) & (df['city'] == "Mumbai")]
print("\nFiltered Data:\n", filtered_df)

# 4. GroupBy Aggregation
grouped = df.groupby('department')['salary'].agg(['mean', 'max', 'count'])
print("\nGrouped Data:\n", grouped)

# 5. Sort Data
sorted_df = df.sort_values(by=['salary', 'age'], ascending=[False, True])
print("\nSorted Data:\n", sorted_df)

# 6. Create New Columns
df['annual_salary'] = df['salary'] * 12

def age_group(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

df['age_group'] = df['age'].apply(age_group)

print("\nData with New Columns:\n", df.head())

# 7. Data Visualization
df['department'].value_counts().plot(kind='bar')
plt.title("Department Count")
plt.show()

df['salary'].plot(kind='hist', bins=10)
plt.title("Salary Distribution")
plt.show()

# 8. Correlation Analysis
corr = df.corr(numeric_only=True)

plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()

# 9. Merge Datasets
df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")

merged_df = pd.merge(df1, df2, on='id', how='inner')
print("\nMerged Data:\n", merged_df)