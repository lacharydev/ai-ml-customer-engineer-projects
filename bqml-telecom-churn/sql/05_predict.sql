-- 05_predict.sql
-- Predict churn outcomes for all customers

SELECT
  customerID,
  predicted_Churn,
  predicted_Churn_probs
FROM ML.PREDICT(
  MODEL `learned-pact-475307-g8.my_datasets.churn_model`,
  TABLE `learned-pact-475307-g8.my_datasets.telecom_churn_trainview`
)
LIMIT 20;

