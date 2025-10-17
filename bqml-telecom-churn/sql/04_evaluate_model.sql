-- 04_evaluate_model.sql
-- Evaluate the churn model using held-out evaluation data

SELECT *
FROM ML.EVALUATE(MODEL `learned-pact-475307-g8.my_datasets.churn_model`);

