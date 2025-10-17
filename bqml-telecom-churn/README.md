Telecom Customer Churn Prediction with BigQuery ML

## 🚀 Project Overview
This project demonstrates how to use **Google BigQuery ML** to build a churn prediction model.  
I uploaded a Telecom Churn dataset to BigQuery, explored customer behavior, trained a logistic regression model, and generated churn predictions.

---

## 📂 Dataset
- Source: Kaggle [Telco Customer Churn dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  
- Uploaded to my project:
learned-pact-475307-g8.my_datasets.telecom_churn

yaml
Copy code

### Schema (sample)
| Column          | Type      | Description                            |
|-----------------|-----------|----------------------------------------|
| customerID      | STRING    | Unique customer ID                     |
| gender          | STRING    | Male / Female                          |
| SeniorCitizen   | INT64     | 0 = No, 1 = Yes                        |
| Partner         | STRING    | Yes / No                               |
| Dependents      | STRING    | Yes / No                               |
| tenure          | INT64     | Months the customer stayed             |
| PhoneService    | STRING    | Yes / No                               |
| InternetService | STRING    | DSL / Fiber optic / No                 |
| Contract        | STRING    | Month-to-month / One year / Two year   |
| MonthlyCharges  | FLOAT64   | Monthly bill                           |
| Churn           | STRING    | Target label (Yes / No)                |

---

## 🛠️ Steps

### 1. Explore Data
File: `sql/01_explore_data.sql`  
- Row counts  
- Churn distribution  
- Average charges and tenure by churn

![Dataset Preview](./images/dataset_preview.png)

---

### 2. Create Clean View
File: `sql/02_create_view.sql`  
- Casts numeric fields  
- Selects relevant features  

---

### 3. Train Model
File: `sql/03_train_model.sql`  
```sql
CREATE OR REPLACE MODEL `my_datasets.churn_model`
OPTIONS(model_type='logistic_reg', input_label_cols=['Churn']) AS
SELECT * EXCEPT(customerID)
FROM `my_datasets.telecom_churn_trainview`;

4. Evaluate Model
File: sql/04_evaluate_model.sql

Accuracy, precision, recall, F1, log_loss, roc_auc

Results saved in data/evaluation_results.csv


5. Predict Churn
File: sql/05_predict.sql

Generate churn predictions for each customer

Results saved in data/predictions_sample.csv


6. Top Risk Customers
File: sql/06_top_risk_customers.sql

Sort by churn probability descending

📈 Results
Accuracy: ~80%

ROC AUC: ~0.85

Customers with month-to-month contracts and high monthly charges are most at risk of churn.


