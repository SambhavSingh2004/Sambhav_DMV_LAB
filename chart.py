import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv(r"D:\Subhadeep_DMV_LAB\Dataset\Cleaned_Students_Performance.csv")


# Scatter Plot: CGPA vs Attendance
plt.figure(figsize=(8,6))
plt.scatter(df["Average attendance on class"], df["What is your current CGPA?"], c="blue", alpha=0.6)
plt.xlabel("Average Attendance (%)")
plt.ylabel("Current CGPA")
plt.title("Scatter Plot: CGPA vs Attendance")
plt.legend(["Students"])
plt.tight_layout()

# Pie Chart: Gender distribution (first 30 rows)
plt.figure(figsize=(6,6))
gender_counts = df.iloc[:30]["Gender"].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart: Gender Distribution (First 30 Rows)")
plt.legend(gender_counts.index, title="Gender")
plt.tight_layout()

# Stair (Step) Chart: CGPA progression across students
plt.figure(figsize=(8,6))
plt.step(range(len(df)), df["What is your current CGPA?"], where="mid", color="green")
plt.xlabel("Student Index")
plt.ylabel("Current CGPA")
plt.title("Stair Chart: CGPA Progression")
plt.legend(["CGPA"])
plt.tight_layout()

# Line Chart: Average CGPA by Scholarship status
plt.figure(figsize=(8,6))
scholarship_avg = df.groupby("Do you have meritorious scholarship ?")["What is your current CGPA?"].mean()
scholarship_avg.plot(kind="line", marker="o", color="red")
plt.xlabel("Scholarship Status (Yes/No)")
plt.ylabel("Average CGPA")
plt.title("Line Chart: Average CGPA by Scholarship Status")
plt.legend(["Average CGPA"])
plt.tight_layout()

# Bar Chart: Average CGPA by Gender
plt.figure(figsize=(8,6))
df.groupby("Gender")["What is your current CGPA?"].mean().plot(kind="bar", color=['skyblue','lightgreen'])
plt.xlabel("Gender")
plt.ylabel("Average CGPA")
plt.title("Bar Chart: Average CGPA by Gender")
plt.legend(["Average CGPA"])
plt.xticks(rotation=0)
plt.tight_layout()


plt.show()