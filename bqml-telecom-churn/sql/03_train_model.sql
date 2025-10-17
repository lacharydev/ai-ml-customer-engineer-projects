-- 03_train_model.sql
-- Train a Logistic Regression model for churn prediction

CREATE OR REPLACE MODEL `learned-pact-475307-g8.my_datasets.churn_model`
OPTIONS(
  model_type = 'logistic_reg',
  input_label_cols = ['Churn'],
  data_split_method = 'AUTO_SPLIT',     -- automatically split into train/eval
  data_split_eval_fraction = 0.2,
  learn_rate = 0.1
) AS
SELECT
  gender,
  SeniorCitizen,
  Partner,
  Dependents,
  tenure,
  PhoneService,
  InternetService,
  Contract,
  MonthlyCharges,
  Churn
FROM `learned-pact-475307-g8.my_datasets.telecom_churn_trainview`;

