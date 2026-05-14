# HR-Employee-Attrition

# Employee Attrition Analysis Using Python

## Project Overview

This project focuses on performing an in-depth Exploratory Data Analysis (EDA) on an HR Employee Attrition dataset using Python. The main objective of this analysis is to understand employee behavior, identify the major factors contributing to attrition, and generate meaningful business insights through data visualization and feature engineering.

The project demonstrates practical data analysis skills including:

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Data Visualization
* Statistical Understanding of Employee Trends

This project was built using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

---

# Project Objectives

The major goals of this project are:

* Understand employee attrition patterns
* Analyze employee demographics and salary structure
* Identify important factors affecting employee turnover
* Perform feature engineering to create meaningful business metrics
* Visualize hidden trends and relationships in HR data
* Improve analytical and visualization skills using real-world datasets

---

# Dataset Information

The dataset contains HR-related employee information such as:

* Age
* Gender
* Department
* Monthly Income
* Job Role
* Work Life Balance
* Total Working Years
* Overtime Status
* Business Travel
* Distance From Home
* Attrition Status
* Years At Company
* Performance Ratings
* Job Satisfaction
* Promotion Details

The dataset is commonly used for Employee Attrition Analysis and HR Analytics projects.

---

# Technologies Used

## Programming Language

* Python

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# Project Workflow

## 1. Data Loading

The dataset was imported using Pandas and initial observations were performed using:

```python
pd.read_csv()
df.head()
df.shape
df.describe()
```

---

## 2. Data Understanding

Several inspection techniques were used to understand the structure of the dataset:

* Dataset Shape
* Statistical Summary
* Data Types
* Column Inspection
* Duplicate Checking
* Missing Value Analysis

---

## 3. Data Cleaning

The following preprocessing steps were performed:

* Removed missing values using `dropna()`
* Checked duplicate records
* Dropped unnecessary columns:

  * EmployeeCount
  * EmployeeNumber
  * Over18
  * StandardHours

These columns were removed because they provided little analytical value.

---

# Feature Engineering

Several new business-oriented features were created to improve analysis quality.

## 1. Age Group

Employees were categorized into different age brackets:

* 18-25
* 26-35
* 36-45
* 46-60

Purpose:

* Helps analyze attrition across age categories.

---

## 2. Income Rate Category

Monthly income was converted into salary bands:

* VeryLow
* Low
* Medium
* Average
* High

Purpose:

* Helps understand salary distribution and attrition trends.

---

## 3. Experience Level

Employees were grouped according to total work experience:

* Fresher
* MidLevel
* Expert
* SeniorEmployee
* Manager

Purpose:

* Understand how experience impacts attrition.

---

## 4. Promotion Gap

A custom feature was created:

```python
PromotionGap = YearsAtCompany - YearsSinceLastPromotion
```

Purpose:

* Measures promotion delay.
* Helps identify employee dissatisfaction.

---

## 5. Distance From Office Category

Employees were grouped according to office distance:

* Nearby
* Mid
* CanTravel
* Far
* TooFar

Purpose:

* Analyze whether travel distance impacts attrition.

---

## 6. Income Per Level

A feature was created to measure salary efficiency:

```python
IncomePerLevel = MonthlyIncome / JobLevel
```

Purpose:

* Compare employee compensation relative to hierarchy.

---

## 7. Overtime Flag

Overtime values were encoded numerically:

```python
Yes = 1
No = 0
```

Purpose:

* Easier correlation and modeling.

---

## 8. Attrition Flag

Attrition status was converted into numerical format.

Purpose:

* Simplifies visualization and correlation analysis.

---

## 9. Travel Stress Score

A custom feature was created using:

```python
TravelStressScore = DistanceFromHome * BusinessTravel
```

Purpose:

* Estimate employee travel burden.
* Understand travel-related stress impact.

---

# Exploratory Data Analysis (EDA)

Multiple visualizations were created to analyze employee behavior and attrition patterns.

---

## Visualizations Performed

### 1. Age Distribution

* Histogram with Attrition comparison
* Analyzed how attrition varies across age groups

### 2. Monthly Income Distribution

* Distribution analysis of employee salaries
* Compared salary trends with attrition

### 3. Daily Rate Distribution

* KDE Plot for salary distribution patterns

### 4. Hourly Rate Analysis

* Boxplot used for outlier detection

### 5. Years At Company Distribution

* Identified employee retention trends

### 6. Total Working Years Distribution

* Compared overall experience levels

### 7. Department Distribution

* Pie chart visualization of department sizes

### 8. Gender Distribution

* Countplot analysis of employee gender ratio

### 9. Job Role Distribution

* Pie chart for employee job roles

### 10. Overtime Analysis

* Compared overtime frequency with attrition

### 11. Work Life Balance vs Attrition

* Identified relationship between work-life balance and employee turnover

### 12. Monthly Income vs Attrition

* Boxplot analysis of salary impact on attrition

### 13. Correlation Heatmap

* Identified relationships between numerical variables

### 14. Pairplot Analysis

* Compared multiple numerical features together
* Visualized attrition clustering patterns

---

# Key Insights Generated

## Employee Attrition Insights

* Employees doing overtime showed higher attrition rates.
* Poor work-life balance was strongly associated with attrition.
* Employees with lower monthly income were more likely to leave.
* Employees with long promotion gaps may experience dissatisfaction.
* Employees living far from office locations showed higher travel stress.
* Younger employees showed different attrition behavior compared to experienced employees.

---

## Salary Insights

* Monthly income distribution was positively skewed.
* Salary differences existed across job levels.
* Higher experience generally resulted in better compensation.

---

## Workforce Insights

* Certain departments had significantly larger employee counts.
* Job role distribution showed workforce concentration in selected roles.
* Gender distribution analysis provided workforce diversity understanding.

---

# Correlation Analysis

The heatmap revealed important relationships among variables such as:

* Monthly Income and Job Level
* Years At Company and Total Working Years
* Overtime and Attrition
* Work Life Balance and Attrition

This analysis helps identify important features influencing employee behavior.

---

# Skills Demonstrated

This project demonstrates practical skills in:

* Data Analysis
* Data Cleaning
* Feature Engineering
* Statistical Thinking
* Data Visualization
* Business Understanding
* Exploratory Data Analysis
* Python Programming
* HR Analytics

---

# Project Structure

```bash
Employee-Attrition-Analysis/
│
├── main.ipynb
├── HR-Employee-Attrition.csv
├── README.md
└── requirements.txt
```

---

# Future Improvements

Possible future enhancements:

* Build Machine Learning models for attrition prediction
* Deploy project using Streamlit
* Add interactive dashboards
* Perform advanced statistical analysis
* Use Power BI or Tableau integration
* Add employee retention recommendation system

---

# Sample Visualizations

The project includes:

* Histograms
* KDE Plots
* Boxplots
* Countplots
* Pie Charts
* Correlation Heatmaps
* Pairplots

These visualizations help uncover hidden trends and business patterns.

---

# Learning Outcomes

Through this project, the following concepts were strengthened:

* Real-world data preprocessing
* Data transformation techniques
* Visualization storytelling
* Business-oriented feature engineering
* HR domain understanding
* Analytical thinking

---

# Conclusion

This project successfully analyzed employee attrition patterns using Python-based data analysis techniques. Through extensive EDA and feature engineering, several meaningful business insights were identified regarding employee salary, overtime, work-life balance, experience, and promotion trends.

The project highlights how data analytics can help organizations understand employee behavior and make better HR decisions to improve employee retention.

---

# Author

## Shlok Gadhave





