# Hands-on 3: Exploring the mini AIOps RAG demo project structure

## Goal
Understand how the demo is organized so you can find data, app code, and utility scripts quickly.

## Project root
- `module-1/mini-aiops-rag-demo/`

## Expected structure
- `app/`
  - `streamlit_app.py` (UI entry point)
- `data/`
  - `incidents.csv`
  - `runbooks.csv`
- `src/`
  - `retrieval.py` (simple local retrieval logic)

## What to explore

### 1) List files
From `mini-aiops-rag-demo`:

```bash
find . -maxdepth 2 -type f
```

### 2) Open the app entrypoint
Open:
- `app/streamlit_app.py`

Look for:
- Where the incident text input is collected
- Which function is called to retrieve similar incidents

### 3) Open the retrieval code
Open:
- `src/retrieval.py`

Look for:
- Where CSV files are read
- How text similarity is calculated

## Practical exercise
Answer these questions (write the answers in a note):
- Which file is the Streamlit entry point?
- Which CSV column contains the incident description/alert text?
- How does the code decide which incident is the “most similar”?
