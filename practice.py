import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_attrition_dataset.csv")

# Basic Information
print(df.head())
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Attrition count
print(df["Attrition"].value_counts())

# Department-wise Attrition
dept = df.groupby("Department")["Attrition"].value_counts().unstack()
print(dept)

dept.plot(kind="bar")
plt.title("Department-wise Attrition")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.show()

# Age Distribution
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Attrition Pie Chart
df["Attrition"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Employee Attrition")
plt.ylabel("")
plt.show()