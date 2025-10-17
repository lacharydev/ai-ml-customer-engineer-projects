-- 02_create_view.sql
-- Create a clean training view with selected features

CREATE OR REPLACE VIEW `learned-pact-475307-g8.my_datasets.telecom_churn_trainview` AS
SELECT
  customerID,
  CAST(SeniorCitizen AS INT64) AS SeniorCitizen,
  gender,
  Partner,
  Dependents,
  CAST(tenure AS INT64) AS tenure,
  PhoneService,
  InternetService,
  Contract,
  CAST(MonthlyCharges AS FLOAT64) AS MonthlyCharges,
  Churn
FROM `learned-pact-475307-g8.my_datasets.telecom_churn`;

