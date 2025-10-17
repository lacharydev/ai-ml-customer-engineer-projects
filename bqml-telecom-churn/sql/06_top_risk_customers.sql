-- 06_top_risk_customers.sql
-- Get the top customers most likely to churn

SELECT
  customerID,
  probs['Yes'] AS churn_probability
FROM (
  SELECT
    customerID,
    predicted_Churn_probs AS probs
  FROM ML.PREDICT(
    MODEL `learned-pact-475307-g8.my_datasets.churn_model`,
    TABLE `learned-pact-475307-g8.my_datasets.telecom_churn_trainview`
  )
)
ORDER BY churn_probability DESC
LIMIT 20;

