-- 01_explore_data.sql
-- Total rows in the dataset
SELECT COUNT(*) AS total_rows
FROM `learned-pact-475307-g8.my_datasets.telecom_churn`;

-- Churn distribution
SELECT Churn, COUNT(*) AS cnt
FROM `learned-pact-475307-g8.my_datasets.telecom_churn`
GROUP BY Churn;

-- Average charges by churn
SELECT Churn, AVG(MonthlyCharges) AS avg_monthly, AVG(tenure) AS avg_tenure
FROM `learned-pact-475307-g8.my_datasets.telecom_churn`
GROUP BY Churn;
