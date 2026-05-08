# Hands-on 3 (Module 3): Deploying to Kubernetes

## Goal
Deploy the AIOps assistant container into a Kubernetes cluster.

## Prerequisites
- A working Kubernetes cluster (kind, minikube, or your lab cluster)
- `kubectl` configured to talk to your cluster
- A built image accessible to the cluster

## Steps

### 0) Build the Docker image (if you haven't)
From the demo project folder:

```bash
cd module-1/mini-aiops-rag-demo
docker build -t aiops-assistant:v1 .
```

### 1) Make sure the image is available to your cluster
Pick the instruction that matches your cluster:

- kind:
```bash
kind load docker-image aiops-assistant:v1
```

- minikube:
```bash
minikube image load aiops-assistant:v1
```

If you are using a remote/lab cluster, push the image to a registry and update `module-3/k8s/deployment.yaml` with that image name.

### 2) Create the namespace

```bash
kubectl apply -f module-3/k8s/namespace.yaml
```

### 3) Create the Secret
Edit the values in `module-3/k8s/secrets.yaml` if you have keys. Otherwise keep them empty.

```bash
kubectl apply -f module-3/k8s/secrets.yaml
```

### 4) Deploy the app

```bash
kubectl apply -f module-3/k8s/deployment.yaml
kubectl apply -f module-3/k8s/service.yaml
```

### 5) Verify

```bash
kubectl -n aiops get pods
kubectl -n aiops get svc
```

Wait until the pod is `Running` and `READY` is `1/1`.

### 6) Access the app
- NodePort: open `http://<NODE_IP>:30081`

If you are using a local cluster, you can also port-forward:

```bash
kubectl -n aiops port-forward svc/aiops-assistant 8501:8501
```

Then open `http://localhost:8501`.

## Expected outcome
- A Deployment and Service exist in the `aiops` namespace.
- You can load the Streamlit UI via NodePort or port-forward.
- The pod has the secret env vars available (even if empty).

## Capstone alignment (AIOps-recommender)
In the capstone repo:
- Namespace is `aiops-prod`
- Secrets are injected via Ansible/GitHub Actions
- Service is exposed via NodePort
