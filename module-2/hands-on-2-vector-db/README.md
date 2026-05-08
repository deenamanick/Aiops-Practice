# Hands-on 2 (Module 2): Moving to Vector Search

## Goal
Replace the basic Jaccard similarity logic with Vector Embeddings and a Vector Database (ChromaDB) for semantically accurate incident retrieval.

## Why Vector Search?
Unlike Jaccard similarity which looks for exact word overlaps, Vector Search understands the *meaning* of words (e.g., "latency" is related to "slow response").

## Steps

### 0) Activate your environment
From the repo root:

```bash
cd module-1/mini-aiops-rag-demo
source .venv/bin/activate
```

If you do not have `.venv` yet, complete Module 1 Hands-on 2 first.

### 1) Install dependencies
Install the new packages required for embeddings + vector DB:

```bash
pip install -r requirements.txt
```

Verify:

```bash
python -c "import chromadb; import sentence_transformers; print('ok')"
```

### 2) The Vector Search Logic
In this repository, the runnable demo project lives at:
- `module-1/mini-aiops-rag-demo/`

The vector retrieval implementation belongs in:
- `module-1/mini-aiops-rag-demo/src/vector_retrieval.py`

Key pieces to implement:
- **Embedding Generation**: convert text to vectors using Sentence-Transformers.
- **Collection Setup**: create a persisted ChromaDB collection (saved on disk).
- **Similarity Search**: query the collection for closest matches.

This is the same idea as the capstone repo, where the build step is `AIOps-recommender/pipeline/build_pipeline.py` and the persisted DB is `AIOps-recommender/chroma_db/`.

### 3) Build/Seed the Vector Store (offline build)
From the demo project folder:

```bash
cd module-1/mini-aiops-rag-demo
python seed_vector_db.py
```

Expected: a local `chroma_db/` folder is created/updated.

Verify the folder exists:

```bash
ls -la chroma_db
```

### 4) Run the app and test retrieval

```bash
streamlit run app/streamlit_app.py
```

Test queries:
- "High 5xx errors after deploy on checkout-service"
- "checkout failing due to database connection pool"

## Troubleshooting
- If seeding is slow the first time, wait for Sentence-Transformers model download.
- If you see import errors, confirm your virtualenv is active: `which python` should point to `.venv`.

### 4) Practical Exercise
- Compare results of the same query between Jaccard and Vector search.
- Try paraphrases:
  - "checkout failing due to database connection pool"
  - "high latency on gateway during traffic spike"

## Expected Outcome
- The assistant should now find relevant incidents even if the user uses different terminology (e.g., searching for "system lag" should match incidents mentioning "high latency").
