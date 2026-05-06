import pandas as pd

# Load dataset
df = pd.read_csv("data_cleaning.csv")

# 1) Remove completely empty rows
df = df.dropna(how="all")

# 2) Remove duplicate rows
df = df.drop_duplicates()

# 3) Fix column names (remove spaces + lowercase)
df.columns = df.columns.str.strip().str.lower()

# 4) Clean text columns (example: name, city)
if "name" in df.columns:
    df["name"] = df["name"].astype(str).str.strip().str.lower()

if "city" in df.columns:
    df["city"] = df["city"].astype(str).str.strip().str.title()

# 5) Convert salary to numeric (handle strings safely)
if "salary" in df.columns:
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# 6) Fill missing salary values with mean
if "salary" in df.columns:
    df["salary"] = df["salary"].fillna(df["salary"].mean())

# 7) Convert age to numeric
if "age" in df.columns:
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

# 8) Remove invalid age rows
if "age" in df.columns:
    df = df[(df["age"] >= 0) & (df["age"] <= 120)]

# 9) Split full name into first and last name
if "name" in df.columns:
    name_split = df["name"].str.split(" ", n=1, expand=True)
    df["first"] = name_split[0]
    df["last"] = name_split[1]

# 10) Filter data (age > 25 and salary > 50000)
if "age" in df.columns and "salary" in df.columns:
    filtered_df = df[(df["age"] > 25) & (df["salary"] > 50000)]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
filtered_df.to_csv("filtered_data.csv", index=False)

print("Data cleaning complete ✅")
print("Cleaned file saved as cleaned_data.csv")
print("Filtered file saved as filtered_data.csv")