# Customer Churn Prediction (BigQuery ML + Vertex AI)

### 🎯 Goal
Predict customer churn for a telecom company using BigQuery ML and deploy the model to Vertex AI.

### 🧠 Tools Used
- Google Cloud BigQuery ML
- Vertex AI
- SQL
- Google Cloud Console

### 🧩 Steps
1. Queried `telecom_churn` dataset from `bigquery-public-data`.
2. Trained logistic regression model in BigQuery ML.
3. Evaluated model accuracy and log loss.
4. Used `ML.PREDICT` to generate churn probabilities.
5. (Optional) Deployed model endpoint in Vertex AI.

### 📊 Results
- Accuracy: 78%
- Key Features: Contract Type, MonthlyCharges, Tenure
- Example Predictions:  
  | customerID | churn_prob | churn_pred |  
  |-------------|------------|-------------|  
  | 7590-VHVEG  | 0.89 | Yes |  

### 🚀 Next Steps
- Integrate model API with a CRM dashboard (Salesforce, optional)
- Automate retraining schedule via Cloud Scheduler

### 🏆 Skills Demonstrated
Cloud-native ML architecture • SQL modeling • Data analysis • Vertex AI deployment
