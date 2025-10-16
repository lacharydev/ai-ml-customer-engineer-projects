# Customer Churn Prediction (BigQuery ML + Vertex AI)

### 🎯 Goal
Predict customer churn for a telecom company using **BigQuery ML** and (optionally) deploy to **Vertex AI** for real-time predictions.

### 🧠 Tools Used
- Google Cloud **BigQuery ML**
- **Vertex AI** (optional deployment)
- **SQL** (no Python required for core workflow)
- Google Cloud Console

### 🧩 Steps
1. **Pin public dataset**: `bigquery-public-data` → dataset: `ml_datasets.telecom_churn`.
2. **Train model** (logistic regression) with SQL in BigQuery ML.
3. **Evaluate** with `ML.EVALUATE` to view accuracy, precision, recall.
4. **Predict** with `ML.PREDICT` to get churn probabilities for customers.
5. **(Optional)** Import the model into **Vertex AI** and deploy to an endpoint for REST predictions.

### 📊 Results (example)
- Accuracy: ~0.75–0.80 (baseline logistic regression)
- Top features: **Contract**, **Tenure**, **MonthlyCharges**
- Example output:
  | customerID | predicted_churn | probability |
  |------------|------------------|-------------|
  | 7590-VHVEG | Yes              | 0.89        |

### 🚀 How to Run
In BigQuery, open **Compose New Query** and run scripts in this order:
1. [`sql/churn_model.sql`](sql/churn_model.sql) — trains/overwrites the model at `mydataset.customer_churn_model`
2. [`sql/evaluate.sql`](sql/evaluate.sql) — prints evaluation metrics
3. [`sql/predict.sql`](sql/predict.sql) — returns predictions/probabilities

> **Note:** Create a dataset named `mydataset` first (left panel → your project → three dots → *Create dataset*).

### 🏗️ (Optional) Vertex AI Deployment
1. In the Console: **Vertex AI → Models → Import**.
2. Select the BigQuery model `mydataset.customer_churn_model`.
3. Deploy to an endpoint. Copy the **endpoint ID** for REST calls.
4. Use the **Predict** tab to test payloads in the UI or via `curl`/Postman.

### 🏆 Skills Demonstrated
Cloud-native ML on GCP • SQL modeling • Model evaluation • (Optional) Vertex AI deployment • Communicating business value

### 📎 Resume Snippet
*Customer Churn Prediction (Vertex AI + BigQuery ML):* Built and evaluated a BigQuery ML logistic regression model on a telecom dataset and (optionally) deployed to Vertex AI; designed SQL-based training and inference pipeline with REST endpoint for predictions.

---

#### Author
Lakshmi Achary | linkedin.com/in/lakshmi-achary
