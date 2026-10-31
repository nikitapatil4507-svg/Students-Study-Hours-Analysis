# Students Study Hours Analysis Dashboard

## Project Overview

This project analyzes student study habits and academic performance using Python, Streamlit, and Microsoft Excel.

It helps understand the relationship between study hours, sleep hours, and exam scores through interactive visualizations and KPI metrics.

## Project Objectives

* Analyze students' daily study hours.
* Understand the relationship between study time and exam performance.
* Calculate the overall student pass rate.
* Explore the impact of sleep hours on exam scores.
* Present insights using interactive dashboards.

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Microsoft Excel

## Key Features

* 500 student records.
* Interactive gender, age, and result filters.
* CSV file upload.
* Total student count.
* Average study hours.
* Average exam score.
* Student pass rate.
* Average sleep hours.
* Study hours vs exam score visualization.
* Pass vs Fail analysis.
* Excel dashboard with KPI cards and charts.

## Dataset

The project uses a synthetic dataset containing 500 student records.

Main columns:

* Student_ID
* Gender
* Age
* Study_Hours
* Sleep_Hours
* Attendance
* Previous_Scores
* Exam_Score
* Internet_Usage
* Final_Result

## How to Run the Project

1. Clone or download the repository.

2. Open the project folder in VS Code.

3. Open the terminal.

4. Navigate to the Python dashboard folder:

   `cd python_dashboard`

5. Install the required libraries:

   `pip install -r requirements.txt`

6. Run the dashboard:

   `streamlit run app.py`

7. Open the local URL displayed in the terminal.

## Key Findings

* Average study time is 4.2 hours.
* Average exam score is 56.5.
* Overall pass rate is 94.4%.
* Average sleep time is 7.1 hours.
* Students in higher study-hour groups have higher average exam scores in this sample.

## Project Structure

```text
Students_Study_Analysis/
│
├── dataset/
│   └── students.csv
│
├── python_dashboard/
│   ├── app.py
│   ├── students.csv
│   └── requirements.txt
│
├── excel_dashboard/
│   └── students_analysis.xlsx
│
└── README.md
```

## Note

This project uses synthetic sample data for educational and demonstration purposes. The observed relationships do not establish causation.

## Author

Nikita Patil
