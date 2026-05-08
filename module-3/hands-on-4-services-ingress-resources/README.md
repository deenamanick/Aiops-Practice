# Hands-on 4 (Module 3): Services, Networking, Secrets, and Resources

## Goal
Understand how Kubernetes networking and resource controls apply to AI workloads.

## Topics

### 1) Configuring and managing secrets
- Use Secrets for API keys and tokens.
- Inject via `envFrom` or `secretKeyRef`.

### 2) Service discovery and networking
- ClusterIP vs NodePort vs LoadBalancer
- DNS inside the cluster (`<service>.<namespace>.svc.cluster.local`)

### 3) Resource management for AI workloads
- requests/limits for CPU and memory
- why vector DB + embeddings can increase RAM usage

### 4) Ingress (optional)
- When to use Ingress vs NodePort
- TLS termination at the edge

## Practical exercise

### 1) Verify Service discovery (NodePort)
Confirm the service exists:

```bash
kubectl -n aiops get svc aiops-assistant
```

Expected: `TYPE` is `NodePort` and a node port `30081` is shown.

If you're on a local cluster and don't know the node IP, use port-forward:

```bash
kubectl -n aiops port-forward svc/aiops-assistant 8501:8501
```

Then open `http://localhost:8501`.

### 2) Verify Secret injection
Check that the secret exists:

```bash
kubectl -n aiops get secret aiops-secrets
```

Optionally, open `module-3/k8s/deployment.yaml` and confirm it uses:

```yaml
envFrom:
  - secretRef:
      name: aiops-secrets
```

### 3) Resource management (requests/limits)
In this repo, requests/limits are set in:
- `module-3/k8s/deployment.yaml`

Apply (or re-apply) the deployment after edits:

```bash
kubectl apply -f module-3/k8s/deployment.yaml
kubectl -n aiops rollout status deploy/aiops-assistant
```

Verify resources were applied:

```bash
kubectl -n aiops describe deploy aiops-assistant
```

### 4) Ingress (optional)
If your cluster has an Ingress controller installed, you can add an Ingress.

If your cluster does not have an Ingress controller, skip this section and use NodePort or port-forward.

Verification (controller exists):

```bash
kubectl get pods -A | grep -i ingress
```

## Capstone alignment (AIOps-recommender)
In the capstone repo, review:
- `k8s/deployment.yaml` for probes and startup behavior
- `k8s/service.yaml` for NodePort access
- `k8s/secrets.yaml` for secret injection patterns
