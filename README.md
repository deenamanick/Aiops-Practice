# Aiops-Practice

Comprehensive hands-on labs for learning AIOps concepts, from basic retrieval-augmented generation (RAG) to advanced vector search and LLM integration.

## Repository Structure

### [Module 1: Hands-on (AIOps Mini Demo)](./module-1/README.md)
- Setting up the development environment.
- Understanding project structure and data models (CSV).
- Building a basic RAG system using Jaccard similarity.
- Running a Streamlit-based incident assistant.

### [Module 2: Advanced AIOps (Observability & LLMs)](./module-2/README.md)
- **Dockerization:** Packaging the AIOps assistant for production.
- **Vector Search:** Moving from Jaccard similarity to semantic search with ChromaDB and Sentence-Transformers.
- **LLM RCA:** Integrating Large Language Models for automated Root Cause Analysis.

### [Module 3: Deployment for AIOps (Docker & Kubernetes)](./module-3/README.md)
- **Docker:** Containerizing AI/ML applications.
- **Kubernetes:** Deployments, services, and (optional) ingress.
- **Secrets & Resources:** Managing API keys and resource requests/limits.

### [Module 4: Production Operations for AI/ML (CI/CD, Monitoring, Scaling, Security)](./module-4/README.md)
- **CI/CD:** GitHub Actions pipelines for build + test.
- **Testing:** Automated tests for AI/ML and LLM-adjacent components.
- **Monitoring:** Performance, reliability, and resource visibility.
- **Scaling & Security:** Autoscaling patterns and secure configuration.

After completing Module 2, continue with the capstone repository: `AIOps-recommender/`.

## Capstone bridge
Use this guide to transition from this learning repo to the capstone implementation:
- [`docs/capstone-bridge.md`](./docs/capstone-bridge.md)

## Quick Start (Module 1 Demo)

```bash
cd module-1/mini-aiops-rag-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Testing with Docker (Module 2)

```bash
cd module-1/mini-aiops-rag-demo
docker build -t aiops-assistant:v1 .
docker run -p 8501:8501 aiops-assistant:v1
```
