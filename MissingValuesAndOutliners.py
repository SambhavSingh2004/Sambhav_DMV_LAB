import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset (use full path if error comes)
df = pd.read_csv(r"d:\Subhadeep_DMV_LAB\Dataset\Students_Performance_dataset.csv")

# Trim to 30 rows × 30 columns
df = df.iloc[:30, :30]

for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        # Check if mode exists (important fix)
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna("Unknown")

outliers = {}

for col in df.select_dtypes(include=['float64', 'int64']).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outlier_index = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index.tolist()

    if len(outlier_index) > 0:
        outliers[col] = outlier_index

print("\nOutliers detected column-wise:")
for col, rows in outliers.items():
    print(f"{col}: {rows}")

for col in outliers:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

df.to_csv(r"d:\Subhadeep_DMV_LAB\Dataset\Cleaned_Students_Performance.csv", index=False)
