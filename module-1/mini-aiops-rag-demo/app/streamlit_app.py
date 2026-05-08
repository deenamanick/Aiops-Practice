from __future__ import annotations

from pathlib import Path

import streamlit as st

from src.retrieval import analyze_query


DATA_DIR = Path(__file__).resolve().parents[1] / "data"

st.set_page_config(page_title="Mini AIOps Incident Assistant", layout="wide")

st.title("Mini AIOps Incident Assistant")
st.markdown("Type an incident/alert description. The app finds the most similar incident and shows the matching runbook steps.")

query = st.text_area(
    "Incident / Alert Details",
    height=160,
    placeholder="Example: High 5xx errors after deploy on checkout-service. Seeing DB timeouts and connection issues...",
)

run = st.button("Analyze", type="primary")

if run:
    if not query.strip():
        st.warning("Please enter some incident details.")
    else:
        try:
            result = analyze_query(query, DATA_DIR)
            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Closest Incident")
                st.write(f"Incident ID: {result.incident_id}")
                st.write(f"Service: {result.service}")
                st.write(f"Severity: {result.severity}")
                st.write(f"Similarity score: {result.score:.2f}")
                st.write("Alert:")
                st.write(result.alert)

            with col2:
                st.subheader("Suggested Root Cause & Resolution")
                st.write("Root cause:")
                st.write(result.root_cause)
                st.write("Resolution:")
                st.write(result.resolution)

            st.subheader("Runbook")
            if result.runbook_steps:
                st.write(result.runbook_steps)
            else:
                st.info("No runbook found for this service.")
        except Exception as e:
            st.error(f"Error: {e}")
