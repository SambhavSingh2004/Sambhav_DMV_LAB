import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset\Cleaned_Students_Performance.csv')

# Take 30x30 subset
df = df.iloc[:30, :30]

# Select numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Draw boxplot
plt.figure()
numeric_df.boxplot()
plt.xticks(rotation=90)
plt.title("Boxplot of Dataset")
plt.show()