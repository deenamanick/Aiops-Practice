# Hands-on 3 (Module 4): Monitoring application performance

## Goal
Add basic monitoring practices for the AIOps Assistant so you can detect failures and performance issues after deployment.

## What to monitor
- Availability: is the app responding?
- Latency: how long do requests take?
- Resource usage: CPU/memory for the pod
- Error rate: failed requests / exceptions

## Steps

### 1) Kubernetes-level visibility
After deploying via Module 3, review:

```bash
kubectl -n aiops get pods
kubectl -n aiops describe pod -l app=aiops-assistant
kubectl -n aiops logs -l app=aiops-assistant --tail=200
```

### 2) Resource monitoring
Check current usage (if metrics-server is installed):

```bash
kubectl -n aiops top pods
kubectl -n aiops top nodes
```

If `kubectl top` is not available, confirm with your cluster/lab whether metrics-server is installed.

### 3) Application-level logging
Ensure the app logs:
- startup
- errors/exceptions
- timing around retrieval/LLM steps

### 4) Define simple SLOs
Write down target thresholds (example):
- UI available 99% during lab
- p95 response time < 5s for local-only mode

## Expected outcome
- You can quickly answer: is it up, is it slow, is it failing, is it resource constrained?

## Capstone alignment (AIOps-recommender)
In the capstone, you’ll expand this into:
- more structured logging
- health checks/probes
- dashboards/alerts
