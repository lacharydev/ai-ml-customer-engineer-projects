-- TRAIN MODEL
CREATE OR REPLACE MODEL `mydataset.customer_churn_model`
OPTIONS(
  model_type = 'logistic_reg',
  input_label_cols = ['Churn']
) AS
SELECT
  gender,
  SeniorCitizen,
  Partner,
  Dependents,
  tenure,
  PhoneService,
  MultipleLines,
  InternetService,
  OnlineSecurity,
  OnlineBackup,
  DeviceProtection,
  TechSupport,
  StreamingTV,
  StreamingMovies,
  Contract,
  PaperlessBilling,
  PaymentMethod,
  MonthlyCharges,
  TotalCharges,
  Churn
FROM `bigquery-public-data.ml_datasets.telecom_churn`;
