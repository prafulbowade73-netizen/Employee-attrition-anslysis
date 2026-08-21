# 📊 Employee Attrition Analysis

A Python-based **Employee Attrition Analysis** project using **Pandas** and **Matplotlib** to explore employee data, identify attrition patterns, and visualize key insights.

## 🚀 Project Overview

Employee attrition means employees leaving an organization. This project performs basic **Exploratory Data Analysis (EDA)** on an employee dataset to understand:

* Employee data structure
* Missing values
* Attrition distribution
* Department-wise attrition
* Employee age distribution
* Overall employee attrition percentage

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 📊 Matplotlib
* 📁 CSV Dataset
* 💻 Jupyter Notebook / VS Code

## 📂 Project Structure

```text
Employee-Attrition-Analysis/
│
├── employee_attrition_dataset.csv
├── employee_attrition_analysis.py
└── README.md
```

## 📌 Features

### 1. Load Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_csv("employee_attrition_dataset.csv")
```

### 2. Basic Data Analysis

The project checks the first rows, dataset information, and statistical summary:

```python
print(df.head())
print(df.info())
print(df.describe())
```

### 3. Missing Value Analysis

```python
print(df.isnull().sum())
```

This helps identify missing values in each column.

### 4. Attrition Count

```python
print(df["Attrition"].value_counts())
```

This shows how many employees stayed and how many employees left.

### 5. Department-wise Attrition

The project analyzes attrition across different departments:

```python
dept = df.groupby("Department")["Attrition"].value_counts().unstack()
print(dept)
```

A bar chart is then created to visualize the department-wise employee attrition.

### 6. Age Distribution

A histogram is used to understand the distribution of employee ages:

```python
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
```

### 7. Employee Attrition Pie Chart

A pie chart shows the overall proportion of employees who left versus those who stayed:

```python
df["Attrition"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
```

## 📈 Visualizations

This project generates the following visualizations:

1. **Department-wise Attrition Bar Chart**
2. **Employee Age Distribution Histogram**
3. **Employee Attrition Pie Chart**

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Employee-Attrition-Analysis.git
```

### Step 2: Open the Project

```bash
cd Employee-Attrition-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install pandas matplotlib
```

### Step 4: Run the Python File

```bash
python employee_attrition_analysis.py
```

## 📊 Example Analysis

The project helps answer questions such as:

* Which department has the highest attrition?
* How many employees have left the organization?
* What is the overall attrition rate?
* What is the age distribution of employees?
* Are some departments experiencing higher employee turnover?

## 🎯 Learning Outcomes

Through this project, I practiced:

* Loading CSV datasets using Pandas
* Data inspection and cleaning
* Handling missing values
* `groupby()` and `value_counts()`
* Basic statistical analysis
* Data visualization
* Bar charts
* Histograms
* Pie charts
* Exploratory Data Analysis (EDA)

## 🔮 Future Improvements

Possible improvements for this project:

* Add **Seaborn** visualizations
* Perform deeper EDA
* Analyze salary and job satisfaction
* Identify factors affecting attrition
* Build an **Employee Attrition Prediction** model using Machine Learning
* Add an interactive dashboard using **Power BI**

## 👨‍💻 Author

**Praful Bowade**

BCA — AI & Data Science

Interested in **Data Science, Data Analytics, Python, and Machine Learning**.

---

⭐ If you find this project useful, consider giving the repository a star!
