# Hands-on 1 (Module 3): Creating a Dockerfile for the AIOps Application

## Goal
Create and understand a Dockerfile that can package the Streamlit AIOps assistant into a portable container.

## What you will use
- The runnable demo project from Module 1: `module-1/mini-aiops-rag-demo/`

## Steps

### 1) Review the existing Dockerfile
Navigate to:
- `module-1/mini-aiops-rag-demo/Dockerfile`

Identify:
- Base image and Python version
- System dependencies installed
- How dependencies are installed from `requirements.txt`
- Exposed port (Streamlit)
- Entrypoint command

### 2) Explain why containerization matters for AIOps
- Repeatable deployments across machines
- Consistent dependencies for embeddings/vector DB libs
- Easier to deploy to Kubernetes later

## Capstone alignment (AIOps-recommender)
In the capstone repo you will use the same pattern with:
- `AIOps-recommender/Dockerfile`
- runtime env vars injected for API keys
