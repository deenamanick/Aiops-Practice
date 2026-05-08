# Module 1: Hands-on (AIOps Mini Demo)

## Hands-on labs
- `hands-on-1-env/README.md`
- `hands-on-2-venv-deps/README.md`
- `hands-on-3-project-structure/README.md`
- `hands-on-4-run-streamlit/README.md`
- `hands-on-5-data-model/README.md`

## Mini demo project
Path:
- `mini-aiops-rag-demo/`

Run (Linux/macOS):
```bash
cd module-1/mini-aiops-rag-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Student checklist
1) Create and activate venv

```bash
cd module-1/mini-aiops-rag-demo
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Run the app

```bash
streamlit run app/streamlit_app.py
```

4) Verify
- Open `http://localhost:8501`
- Run a query like: "High 5xx errors after deploy on checkout-service"
---
## Next Steps
Once you have completed Module 1, proceed to [Module 2: Advanced AIOps](../module-2/README.md) to learn about Dockerization, Vector Databases, and LLM integration.
