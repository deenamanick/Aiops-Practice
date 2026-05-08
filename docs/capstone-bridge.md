# Capstone Bridge Guide: From `Aiops-Practice` to `AIOps-recommender`

This guide helps students move from the learning repo (`Aiops-Practice`) to the capstone implementation repo (`AIOps-recommender`).

The goal is simple:
- In `Aiops-Practice`, you learn the concepts in small steps.
- In `AIOps-recommender`, you implement the same ideas with a production-style structure: pipeline build, Kubernetes deployment, and automated CI/CD.

---

## 0) What “done” looks like (capstone success criteria)
By the end of `AIOps-recommender`, you should be able to:
- Build and push a Docker image via a CI pipeline.
- Deploy to Kubernetes in the `aiops-prod` namespace.
- Inject secrets from GitHub into Kubernetes Secrets.
- Run a knowledge-build pipeline (`pipeline/build_pipeline.py`) and serve the app.
- Verify rollout and access the app via NodePort.

---

## 1) Mental model: how the two repos relate

### `Aiops-Practice`
- Optimized for learning.
- Smaller, simpler code paths.
- Deployment is introduced with local Docker and basic Kubernetes manifests.

### `AIOps-recommender`
- Optimized for “real deployment.”
- Separate folders for:
  - `pipeline/` (data ingestion + embeddings + vectorstore build)
  - `app/` (UI)
  - `k8s/` (deployment manifests)
  - `ansible/` (runner + deployment automation)
  - `terraform/` (infrastructure automation, if used)

---

## 2) Module-by-module mapping

### Module 1 (Practice): Local assistant + retrieval basics
**Practice location**
- `module-1/mini-aiops-rag-demo/app/streamlit_app.py`
- `module-1/mini-aiops-rag-demo/src/retrieval.py`
- `module-1/mini-aiops-rag-demo/data/*.csv`

**Capstone equivalents**
- UI concept maps to: `AIOps-recommender/app/`
- Retrieval and intelligence concept maps to: `AIOps-recommender/pipeline/` and `AIOps-recommender/src/`
- Dataset maps to: `AIOps-recommender/data/`

**Student milestone**
- You can explain “user query → retrieval → answer” in simple terms.

---

### Module 2 (Practice): Semantic retrieval + LLM RCA
**Practice location**
- Vector store build: `module-1/mini-aiops-rag-demo/seed_vector_db.py`
- Vector retrieval helpers: `module-1/mini-aiops-rag-demo/src/vector_retrieval.py`

**Capstone equivalents**
- Knowledge build script: `AIOps-recommender/pipeline/build_pipeline.py`
- Loader: `AIOps-recommender/pipeline/loader.py`
- Embeddings: `AIOps-recommender/pipeline/embeddings.py`
- Vector store: `AIOps-recommender/pipeline/vectorstore.py`
- Retriever: `AIOps-recommender/pipeline/retriever.py`
- LLM orchestration: `AIOps-recommender/pipeline/llm.py`

**Student milestone**
- You understand the difference between:
  - offline “knowledge build”
  - online “query and answer”

---

### Module 3 (Practice): Kubernetes deployment using manifests
**Practice location**
- `module-3/k8s/namespace.yaml`
- `module-3/k8s/secrets.yaml`
- `module-3/k8s/deployment.yaml`
- `module-3/k8s/service.yaml`

**Capstone equivalents**
- `AIOps-recommender/k8s/namespace.yaml`
- `AIOps-recommender/k8s/deployment.yaml`
- `AIOps-recommender/k8s/service.yaml`
- Deployment notes: `AIOps-recommender/k8s/DEPLOYMENT.md`

**Key differences students must implement in capstone**
- Namespace is `aiops-prod` (capstone) vs `aiops` (practice).
- Manifests include production-hardening concerns (ex: cold start protections).

**Student milestone**
- You can:
  - apply manifests
  - check pods/services
  - port-forward or use NodePort

---

### Module 4 (Practice): CI/CD + testing + monitoring + scaling
**Practice location**
- CI starter workflow: `.github/workflows/ci.yml`
- Tests: `module-1/mini-aiops-rag-demo/tests/`
- HPA example: `module-4/k8s/hpa.yaml`

**Capstone equivalents**
- CI/CD concept is explained in:
  - `AIOps-recommender/README.md`
  - `AIOps-recommender/PIPELINE_DETAILS.md`
- Monitoring lab:
  - `AIOps-recommender/ADVANCED_LABS.md`
- Deployment automation:
  - `AIOps-recommender/ansible/`

**Key differences students must implement in capstone**
- Capstone uses a multi-stage pipeline (build/push, setup, deploy).
- Capstone uses a self-hosted runner pattern.
- Secrets come from GitHub Repo Secrets and are injected into Kubernetes.

---

## 3) Suggested capstone implementation plan (student checklist)

### Milestone A: Run the app locally
- Create `.env` from `.env.example` (do not commit secrets)
- Install dependencies from `requirements.txt`
- Run the app as described in `AIOps-recommender/README.md`

### Milestone B: Build the knowledge base (offline)
- Run the pipeline build script:
  - `pipeline/build_pipeline.py`

### Milestone C: Containerize
- Build the Docker image using `AIOps-recommender/Dockerfile`

### Milestone D: Kubernetes deploy (manual first)
- Apply manifests in `AIOps-recommender/k8s/`
- Verify pods and services in `aiops-prod`

### Milestone E: CI/CD automation
- Follow the pipeline architecture in `PIPELINE_DETAILS.md`
- Configure GitHub Secrets required by the pipeline

### Milestone F: Monitoring (optional advanced)
- Follow `ADVANCED_LABS.md` for Prometheus + Grafana

---

## 4) Quick reference: “where do I implement this?”

- Retrieval and RAG logic:
  - `AIOps-recommender/pipeline/`
- Kubernetes manifests:
  - `AIOps-recommender/k8s/`
- Deployment automation / runner:
  - `AIOps-recommender/ansible/`
- Monitoring addons:
  - `AIOps-recommender/addons/`

---

## 5) If you get stuck (common student errors)
- Vector DB not built yet:
  - run the pipeline build step before expecting good answers
- Pod restarts during first boot:
  - review `k8s/DEPLOYMENT.md` and cold-start settings
- Secrets not available:
  - confirm GitHub Secrets exist and Kubernetes Secret was created in `aiops-prod`
