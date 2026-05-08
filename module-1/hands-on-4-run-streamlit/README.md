# Hands-on 4: Running the application locally with Streamlit

## Goal
Run the mini AIOps demo locally and test it end-to-end.

## Steps

### 1) Activate your virtual environment
From `module-1/mini-aiops-rag-demo`:

```bash
source .venv/bin/activate
```

### 2) Start Streamlit

```bash
streamlit run app/streamlit_app.py
```

### 3) Test with a sample incident
Paste something like:
- "High 5xx errors after deploy. Checkout is failing and DB connections look stuck"

Click **Analyze**.

## Practical exercise
- Change the query text to mention a different service name (example: `auth-service`, `catalog-service`).
- Observe how the “similar incidents” result changes.

## Expected outcome
- The page loads locally (usually http://localhost:8501)
- You see:
  - A probable match from `incidents.csv`
  - Suggested runbook steps from `runbooks.csv`
