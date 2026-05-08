# Module 3: Deployment for AIOps (Docker & Kubernetes)

## Overview
In this module, you will take the AIOps assistant from a local development workflow into a deployable service.

Topics covered:
1. **Docker for AI/ML apps:** Containerizing the Streamlit assistant.
2. **Kubernetes fundamentals:** Deploying the app into a cluster.
3. **Secrets & configuration:** Managing API keys and env vars safely.
4. **Networking:** Services (and optional Ingress) for access.
5. **Resource management:** Requests/limits for AI workloads.

## Hands-on labs
- `hands-on-1-dockerfile/README.md`
- `hands-on-2-local-container-test/README.md`
- `hands-on-3-kubernetes-deploy/README.md`
- `hands-on-4-services-ingress-resources/README.md`

## Student checklist
1) Build Docker image

```bash
cd module-1/mini-aiops-rag-demo
docker build -t aiops-assistant:v1 .
```

2) Run locally (Docker)

```bash
docker run -p 8501:8501 aiops-assistant:v1
```

Verify: open `http://localhost:8501`

3) Deploy to Kubernetes (using provided manifests)

```bash
kubectl apply -f module-3/k8s/namespace.yaml
kubectl apply -f module-3/k8s/secrets.yaml
kubectl apply -f module-3/k8s/deployment.yaml
kubectl apply -f module-3/k8s/service.yaml
```

4) Verify Kubernetes

```bash
kubectl -n aiops get pods
kubectl -n aiops get svc
```

5) Access
- NodePort: `http://<NODE_IP>:30081`
- Or port-forward:

```bash
kubectl -n aiops port-forward svc/aiops-assistant 8501:8501
```

## Alignment to the capstone (AIOps-recommender)
This module is designed to prepare you for the capstone repo `AIOps-recommender/`, which includes:
- A production-ready `Dockerfile`
- Kubernetes manifests under `k8s/`
- Secrets injection for `GROQ_API_KEY` and `HUGGINGFACEHUB_API_TOKEN`
- NodePort access patterns and rollout verification
