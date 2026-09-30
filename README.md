# 📊 Employee Attrition Analysis

A Python-based **Employee Attrition Analysis** project that uses **Pandas** and **Matplotlib** to explore employee data, identify attrition patterns, and generate meaningful visual insights.

This project demonstrates practical **Exploratory Data Analysis (EDA)** skills that are useful for Data Analyst and Data Science roles.

---

## 🚀 Project Overview

Employee attrition refers to employees leaving an organization.

The goal of this project is to analyze employee data and understand patterns related to employee turnover.

The analysis covers:

* Dataset structure and data types
* Missing-value analysis
* Employee attrition distribution
* Department-wise attrition
* Employee age distribution
* Overall attrition percentage
* Basic statistical analysis
* Data visualization

---

## 🛠️ Technologies & Tools

| Technology                    | Purpose            |
| ----------------------------- | ------------------ |
| 🐍 Python                     | Data analysis      |
| 🐼 Pandas                     | Data manipulation  |
| 📊 Matplotlib                 | Data visualization |
| 📁 CSV                        | Dataset            |
| 💻 Jupyter Notebook / VS Code | Development        |

---

## 📂 Project Structure

```text
Employee-Attrition-Analysis/
│
├── employee_attrition_dataset.csv
├── employee_attrition_analysis.py
└── README.md
```

---

## 📌 Project Workflow

```text
CSV Dataset
     ↓
Load Data using Pandas
     ↓
Data Inspection
     ↓
Missing Value Analysis
     ↓
Exploratory Data Analysis
     ↓
Attrition Analysis
     ↓
Department Analysis
     ↓
Data Visualization
     ↓
Business Insights
```

---

## 🔍 Analysis Performed

### 1. Load Dataset

The employee dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv("employee_attrition_dataset.csv")

print(df.head())
```

---

### 2. Dataset Inspection

The project examines the structure and statistical information of the dataset.

```python
print(df.head())
print(df.info())
print(df.describe())
```

This helps understand:

* Number of rows and columns
* Data types
* Numerical statistics
* Dataset structure

---

### 3. Missing Value Analysis

Missing values are checked using:

```python
print(df.isnull().sum())
```

This helps identify columns that may require data cleaning before further analysis.

---

### 4. Attrition Analysis

The number of employees who stayed and left is calculated using:

```python
print(df["Attrition"].value_counts())
```

The overall attrition rate can also be calculated:

```python
attrition_rate = (
    df["Attrition"].value_counts(normalize=True) * 100
)

print(attrition_rate)
```

---

### 5. Department-wise Attrition

Attrition is analyzed across different departments:

```python
dept = df.groupby("Department")["Attrition"].value_counts().unstack()

print(dept)
```

A bar chart is used to compare attrition across departments.

```python
dept.plot(kind="bar")

plt.title("Department-wise Employee Attrition")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.xticks(rotation=0)
plt.show()
```

---

### 6. Age Distribution

A histogram is used to understand the age distribution of employees.

```python
plt.hist(df["Age"], bins=10)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Employee Count")

plt.show()
```

---

### 7. Employee Attrition Visualization

A pie chart is used to visualize the proportion of employees who left and stayed.

```python
df["Attrition"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Employee Attrition Distribution")
plt.ylabel("")

plt.show()
```

---

## 📈 Visualizations

The project generates the following visualizations:

### 📊 1. Department-wise Attrition

Shows employee attrition across different departments.

### 📈 2. Employee Age Distribution

Shows how employee ages are distributed across the organization.

### 🥧 3. Employee Attrition Distribution

Shows the overall proportion of employees who stayed and left.

---

## 💡 Business Questions

This project helps answer questions such as:

* What percentage of employees left the organization?
* Which departments have more employee turnover?
* What is the age distribution of employees?
* How many employees stayed versus left?
* Are there noticeable differences in attrition between departments?

---

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python for data analysis
* Pandas DataFrames
* CSV data handling
* Data inspection
* Missing-value analysis
* `groupby()`
* `value_counts()`
* Statistical analysis
* Data visualization
* Bar charts
* Histograms
* Pie charts
* Exploratory Data Analysis (EDA)
* Extracting basic business insights from data

---

## 🔮 Future Improvements

The project can be extended into a complete **Employee Attrition Prediction** system.

Planned improvements:

* Add advanced EDA
* Add Seaborn visualizations
* Analyze salary and income
* Analyze job satisfaction
* Analyze overtime and working conditions
* Study employee experience and tenure
* Perform correlation analysis
* Build Machine Learning models
* Compare classification algorithms
* Evaluate model performance
* Create an interactive **Power BI dashboard**
* Deploy the ML model as a web application

### 🤖 Future ML Pipeline

```text
Employee Dataset
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Encoding
       ↓
Train/Test Split
       ↓
Machine Learning Model
       ↓
Model Evaluation
       ↓
Employee Attrition Prediction
```

---

## 💼 Skills Demonstrated

This project demonstrates practical skills in:

**Python • Pandas • Matplotlib • Data Cleaning • EDA • Data Visualization • Business Analysis**

---

## 👨‍💻 Author

### Praful Bowade


---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star** on GitHub.
