# Hands-on 2 (Module 3): Building and Testing the Container Locally

## Goal
Build the Docker image locally and run the AIOps assistant as a container.

## Steps

### 1) Build the image
From the demo project folder:

```bash
cd module-1/mini-aiops-rag-demo
docker build -t aiops-assistant:v1 .
```

### 2) Run the container

```bash
docker run -p 8501:8501 aiops-assistant:v1
```

### 3) Verify
- Open `http://localhost:8501`
- Run at least 2 incident queries and confirm results appear.

### 4) Practical exercise
- Stop the container.
- Run in detached mode:

```bash
docker run -d -p 8501:8501 aiops-assistant:v1
```

- View logs:

```bash
docker logs <container_id>
```

## Capstone alignment (AIOps-recommender)
In the capstone repo you will run a similar container, but will also inject env vars like:
- `GROQ_API_KEY`
- `HUGGINGFACEHUB_API_TOKEN`
