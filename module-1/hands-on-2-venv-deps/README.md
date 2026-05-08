# Hands-on 2: Python virtual environment and dependencies

## Goal
Create an isolated Python environment and install dependencies for our mini demo.

## You will use
- `venv` (virtual environments)
- `pip` (dependency installer)

## Steps

### 1) Open the mini demo folder
In this repo, we will use:
- `module-1/mini-aiops-rag-demo`

### 2) Create a virtual environment
From `module-1/mini-aiops-rag-demo`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Freeze what you installed (verification)

```bash
pip freeze | head
```

## Practical exercise
- Create `verify_install.py`:

```python
import streamlit
import pandas
print("streamlit:", streamlit.__version__)
print("pandas:", pandas.__version__)
```

- Run:

```bash
python verify_install.py
```

## Expected output
You should see the installed versions for Streamlit and Pandas.
