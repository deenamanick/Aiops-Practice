# Module 4: Production Operations for AI/ML (CI/CD, Monitoring, Scaling, Security)

## Overview
This module focuses on taking the AIOps Assistant from a working deployment (Module 3) to a production-ready delivery and operations workflow.

Topics covered:
1. **CI/CD for AI/ML applications:** Build, test, and ship changes safely.
2. **Monitoring AI/ML systems:** Track availability, latency, and application health.
3. **Performance optimization:** Reduce cold-start time, improve response times, control resource usage.
4. **Security best practices:** Protect secrets, reduce attack surface, safer supply chain.
5. **Scaling AI/ML workloads:** Autoscaling patterns and capacity planning.

## Hands-on labs
- `hands-on-1-github-actions-cicd/README.md`
- `hands-on-2-automated-ml-testing/README.md`
- `hands-on-3-monitoring-performance/README.md`
- `hands-on-4-autoscaling-ai-workloads/README.md`

## Prerequisites
- Completion of Module 3 (Docker + Kubernetes).
- A GitHub account.
- A Kubernetes cluster you can access with `kubectl` (kind/minikube/lab cluster).

## Student checklist
1) Confirm baseline app runs locally

```bash
cd module-1/mini-aiops-rag-demo
streamlit run app/streamlit_app.py
```

2) Confirm you can build the container image

```bash
docker build -t aiops-assistant:v1 .
```

3) Confirm you can deploy to Kubernetes (Module 3 manifests)

```bash
kubectl apply -f module-3/k8s/namespace.yaml
kubectl apply -f module-3/k8s/secrets.yaml
kubectl apply -f module-3/k8s/deployment.yaml
kubectl apply -f module-3/k8s/service.yaml
```

4) Complete Module 4 labs (in order)
- Follow `hands-on-1-github-actions-cicd/README.md`
- Follow `hands-on-2-automated-ml-testing/README.md`
- Follow `hands-on-3-monitoring-performance/README.md`
- Follow `hands-on-4-autoscaling-ai-workloads/README.md`

## Alignment to the capstone (AIOps-recommender)
This module mirrors real production concerns in the capstone:
- CI pipelines that run tests on every PR
- Secure secrets management
- Operational monitoring and SLO thinking
- Scaling the service under load
