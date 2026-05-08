# Hands-on 3 (Module 2): LLM-Powered Root Cause Analysis (RCA)

## Goal
Enhance the AIOps Assistant by integrating a Large Language Model (LLM) to summarize findings and provide intelligent remediation steps.

## Steps

### 0) Activate your environment
From the repo root:

```bash
cd module-1/mini-aiops-rag-demo
source .venv/bin/activate
```

If `.venv` does not exist, complete Module 1 Hands-on 2 first.

### 1) Choose an LLM Provider
In this lab, you can use:
- **Local:** Ollama (run `ollama run llama3`)
- **Cloud (Capstone-aligned):** Groq API (same provider used in `AIOps-recommender/`)

### 2) Implement the RCA Agent
Create `src/rca_agent.py` to:
- Combine the user query with the retrieved incident/runbook data.
- Send this "context" to the LLM with a specific prompt.
- Return a natural language explanation of the issue and fix.

If you follow the capstone path later, this same role is handled by:
- `AIOps-recommender/pipeline/llm.py` (prompt + Groq model)

### 3) Update the Streamlit UI
Modify `app/streamlit_app.py` to include an "LLM Analysis" section that displays the agent's output.

### 4) Environment Variables (capstone-aligned)
If you want to mirror the capstone repo setup, use env vars:
- `GROQ_API_KEY`
- `HUGGINGFACEHUB_API_TOKEN`

In the capstone repository these are configured via `.env` and consumed by the pipeline/app.

Example (temporary for the current shell session):

```bash
export GROQ_API_KEY="<your_key>"
export HUGGINGFACEHUB_API_TOKEN="<your_token>"
```

### 5) Run and verify

```bash
streamlit run app/streamlit_app.py
```

Test query:
- "High 5xx errors after deploy on checkout-service"

Expected:
- You still see retrieval output (incident + runbook)
- You also see an **LLM Analysis** section with a concise recommendation

## Troubleshooting
- If your LLM output is missing, confirm the UI change is in `app/streamlit_app.py`.
- If you are using Groq and see auth errors, confirm `echo $GROQ_API_KEY` is set.
- If you are using Ollama, confirm it is running locally (`ollama list`).

## Practical Exercise
- Prompt engineering: Adjust the prompt to make the LLM output more concise or more detailed.
- Experiment with different models (e.g., GPT-3.5 vs GPT-4 or Llama-3) to see which provides better RCA for your incident data.

## Expected Outcome
- Instead of just showing raw CSV rows, the app now provides a cohesive "Expert Opinion" on how to handle the alert.
