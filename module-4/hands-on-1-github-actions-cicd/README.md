# Hands-on 1 (Module 4): Setting up GitHub Actions for CI/CD

## Goal
Set up a simple CI pipeline that runs on every push/PR to validate the AIOps Assistant before deploying.

## What you will implement
- A GitHub Actions workflow that:
  - checks out code
  - sets up Python
  - installs dependencies
  - runs lightweight checks/tests

## Steps

### 1) Create a GitHub repository
- Push this repo to GitHub (or fork and work in your fork).

### 2) Decide your CI scope
For this course repo, the code you typically validate lives under:
- `module-1/mini-aiops-rag-demo/`

Your CI should run commands from that folder.

### 3) Add a workflow file
Create:
- `.github/workflows/ci.yml`

This repo already includes a starter workflow at:
- `.github/workflows/ci.yml`

Your workflow should do these jobs:
- Install Python dependencies
- Run formatting/linting (if configured)
- Run tests (Module 4 Hands-on 2 adds tests)

### 4) Validate
- Open GitHub Actions in your repo.
- Trigger the workflow by pushing a small change.
- Confirm the workflow completes successfully.

If the workflow fails, open the failing step logs and fix the first error before moving on.

## Expected outcome
- Every push/PR runs CI.
- Failures block merging until fixed.

## Notes (AI/ML specific)
- Keep CI fast by avoiding heavyweight model downloads.
- Prefer small, deterministic tests (unit + contract tests) over full end-to-end inference in CI.

## Capstone alignment (AIOps-recommender)
The capstone repo uses the same idea:
- CI validates code and the knowledge-build pipeline before deployment.
