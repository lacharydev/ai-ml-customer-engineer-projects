-- PREDICT CHURN
SELECT
  customerID,
  predicted_Churn AS predicted_churn,
  (SELECT prob FROM UNNEST(predicted_Churn_probs) WHERE label = 'Yes') AS churn_probability
FROM ML.PREDICT(MODEL `mydataset.customer_churn_model`,
  (
    SELECT * EXCEPT(Churn)
    FROM `bigquery-public-data.ml_datasets.telecom_churn`
  ))
LIMIT 25;
