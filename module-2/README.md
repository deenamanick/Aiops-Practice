# Module 2: Advanced AIOps (Observability & LLMs)

## Overview
In this module, we advance from local similarity matching to enterprise-grade AIOps concepts, focusing on:
1. **Containerization:** Packaging the AIOps assistant for production.
2. **Advanced RAG:** Using Vector Databases and LLMs for more accurate root cause analysis.
3. **Automated Remediation:** Integrating with metrics and monitoring systems.

## Hands-on labs
- `hands-on-1-docker/README.md`
- `hands-on-2-vector-db/README.md`
- `hands-on-3-llm-rca/README.md`

## Getting started
Start with the labs in order.

Docker and Kubernetes deployment are covered in Module 3:
- `../module-3/README.md`

For Module 2 work, you will continue using the demo project from Module 1:
- `../module-1/mini-aiops-rag-demo/`

## Student checklist
1) Activate venv and install deps

```bash
cd module-1/mini-aiops-rag-demo
source .venv/bin/activate
pip install -r requirements.txt
```

2) Seed/build the vector store

```bash
python seed_vector_db.py
ls -la chroma_db
```

3) Run the app

```bash
streamlit run app/streamlit_app.py
```

4) Complete labs
- Follow `hands-on-2-vector-db/README.md` (vector search)
- Follow `hands-on-3-llm-rca/README.md` (LLM RCA + prompt tuning)

## How this module aligns to the final capstone (AIOps-recommender)
After finishing these labs, you will be ready to work on the final repository: `AIOps-recommender/`.

- **Data (incidents/runbooks)**
  - Here: `module-1/mini-aiops-rag-demo/data/*.csv`
  - Capstone: `AIOps-recommender/data/`
- **Vector store (persisted ChromaDB)**
  - Here: `module-1/mini-aiops-rag-demo/chroma_db/` (created by your seeding/build step)
  - Capstone: `AIOps-recommender/chroma_db/` (created by `pipeline/build_pipeline.py`)
- **Build step (offline knowledge build)**
  - Here: run a script to seed/build the vector store before starting the UI
  - Capstone: `AIOps-recommender/pipeline/build_pipeline.py`
- **Query path (UI -> retrieval -> answer)**
  - Here: `app/streamlit_app.py` calls retrieval logic
  - Capstone: `AIOps-recommender/app/streamlit_app.py` + `pipeline/` (retriever + llm orchestration)
- **LLM provider & env vars**
  - Here: start with local-only (no keys) and then add an LLM
  - Capstone: `.env` with `GROQ_API_KEY` and `HUGGINGFACEHUB_API_TOKEN`
---
## Next steps
After completing Module 2, you can extend the assistant with real observability signals (metrics/logs/traces) and automated runbook execution.
