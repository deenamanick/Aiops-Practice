# Hands-on 2 (Module 4): Implementing automated testing for ML/LLM features

## Goal
Add automated tests that catch regressions in the AI/ML parts of the assistant without needing external API keys.

## What to test (recommended)
- Retrieval returns expected results for known inputs
- Prompt construction is stable (no accidental breaking changes)
- The app can start without secrets (keys optional in dev)

## Steps

### 1) Choose a test framework
- Use `pytest` for Python tests.

### 2) Add a minimal test suite
Create a `tests/` folder inside:
- `module-1/mini-aiops-rag-demo/`

This repo already includes starter tests at:
- `module-1/mini-aiops-rag-demo/tests/test_smoke_imports.py`
- `module-1/mini-aiops-rag-demo/tests/test_retrieval_basic.py`

Start with:
- A smoke test that imports core modules
- A deterministic retrieval test using local data

### 3) Mock external calls
If your code can call an LLM provider:
- mock the LLM call
- avoid real network calls in CI

### 4) Run tests locally
From `module-1/mini-aiops-rag-demo/`:

```bash
pytest -q
```

### 5) Wire tests into CI
Update the workflow from Hands-on 1 so it runs `pytest`.

## Expected outcome
- Tests run locally and in GitHub Actions.
- Failures are visible and actionable.

## Capstone alignment (AIOps-recommender)
The capstone expects:
- fast tests
- deterministic behavior in CI
- external providers only used in controlled environments
