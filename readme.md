# Salary Prediction using Machine Learning

## Project Overview

This project predicts the salary of data science professionals using Machine Learning. It demonstrates the complete Machine Learning pipeline including data cleaning, feature engineering, model training, evaluation, and model saving.

This project is built to showcase real-world ML skills required for Data Scientist and Machine Learning Engineer roles.

---

## Problem Statement

Given job-related features such as experience level, employment type, job title, company size, company location, and remote ratio, the goal is to predict the salary in USD.

This is a supervised machine learning regression problem.

---

## Dataset Information

Total records: 600+

Features used:

* experience_level
* employment_type
* job_title
* company_size
* company_location
* remote_ratio

Target variable:

* salary_in_usd

---

## Machine Learning Pipeline

### 1. Data Cleaning

* Checked for missing values
* Verified data types
* Removed unnecessary columns
* Ensured data consistency

### 2. Feature Engineering

* Converted categorical features into numerical using Label Encoding
* Saved encoders for future predictions using pickle

### 3. Model Training

Models used:

* Linear Regression
* Random Forest Regressor

Random Forest performed better and was selected as the final model.

### 4. Model Evaluation

Evaluation metrics used:

* R² Score
* Mean Absolute Error (MAE)

Final Model Performance:

* R² Score: 0.36
* Mean Absolute Error: 33444

### 5. Model Saving

Saved model and encoders using pickle:

* model/random_forest_model.pkl
* model/label_encoders.pkl

---

## Project Structure

```
salary-prediction-ml/
│
├── data/
│   ├── Salary_dataset_DS.csv
│   ├── X_processed.csv
│   └── y_processed.csv
│
├── src/
│   ├── feature_engineering.ipynb
│   ├── model_training.ipynb
│   └── random_forest.ipynb
│
├── model/
│   ├── random_forest_model.pkl
│   └── label_encoders.pkl
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

---

## Skills Demonstrated

* Data Cleaning
* Feature Engineering
* Machine Learning
* Regression Modeling
* Model Training and Evaluation
* Model Saving and Loading
* Git Version Control
* GitHub Project Management

---

## How to Run This Project

### Step 1: Clone the repository

```
git clone https://github.com/muthurajeshkumarofficial-sketch/salary-prediction-ml.git
```

### Step 2: Navigate to project folder

```
cd salary-prediction-ml
```

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

### Step 4: Open Jupyter Notebook

```
jupyter notebook
```

Run:

```
src/random_forest.ipynb
```

---

## Project Purpose

This project is created for learning and demonstrating Machine Learning skills required for entry-level Data Scientist and Machine Learning Engineer roles.

---

## Author

Muthu Rajesh Kumar K

GitHub:
https://github.com/muthurajeshkumarofficial-sketch

LinkedIn:
https://www.linkedin.com/in/rajesh-kumar-761622250/
