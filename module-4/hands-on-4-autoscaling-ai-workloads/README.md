# Hands-on 4 (Module 4): Implementing autoscaling for AI workloads

## Goal
Understand and implement autoscaling patterns for AI/ML services on Kubernetes.

## Concepts
- **Vertical vs Horizontal scaling**
- **HPA (Horizontal Pod Autoscaler)**: scales replicas based on CPU/memory/custom metrics
- **Resource requests/limits**: required for predictable scheduling and scaling

## Steps

### 1) Validate requests/limits are set
In this repo, requests/limits are defined in:
- `module-3/k8s/deployment.yaml`

Confirm the deployment has requests/limits, then apply:

```bash
kubectl apply -f module-3/k8s/deployment.yaml
kubectl -n aiops rollout status deploy/aiops-assistant
```

### 2) Create an HPA
Create an HPA that targets the `aiops-assistant` deployment.

Minimum expectations:
- min replicas: 1
- max replicas: 3
- target CPU utilization: 60-80%

This repo includes a starter HPA manifest:
- `module-4/k8s/hpa.yaml`

Apply it:

```bash
kubectl apply -f module-4/k8s/hpa.yaml
```

### 3) Generate load (lightweight)
Use a simple load approach appropriate to your environment:
- repeated refreshes / requests
- or a small script that hits the service endpoint

### 4) Observe scaling

```bash
kubectl -n aiops get hpa
kubectl -n aiops get pods -w
```

## Expected outcome
- Under load, replicas increase (if metrics are available).
- When load drops, replicas scale back down.

## Notes (AI/ML specific)
- Inference workloads are often memory-bound.
- Consider startup time and warm caches when scaling.

## Capstone alignment (AIOps-recommender)
In production you’ll typically also add:
- readiness/liveness probes
- rollout strategies
- autoscaling based on custom metrics (queue length, request latency)
