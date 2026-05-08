import os
from typing import Optional

# NOTE: This is a skeleton for Hands-on 3 in Module 2
# It demonstrates how to wrap an LLM call for Root Cause Analysis

class RCAAgent:
    def __init__(self, provider: str = "ollama", model: str = "llama3"):
        self.provider = provider
        self.model = model

    def generate_explanation(self, query: str, incident_context: dict, runbook_context: str) -> str:
        """
        Combines incident data and runbook steps into a prompt for the LLM.
        """
        prompt = f"""
        User Query: {query}
        
        Retrieved Context:
        - Incident: {incident_context.get('alert')}
        - Root Cause: {incident_context.get('root_cause')}
        - Resolution: {incident_context.get('resolution')}
        
        Runbook Steps:
        {runbook_context}
        
        Task: Provide a concise Expert Opinion on why this happened and what the next immediate step should be.
        """
        
        # Placeholder for actual LLM API call (OpenAI, Ollama, etc.)
        return f"[LLM {self.model} Analysis]: Based on the context, this looks like a {incident_context.get('service')} issue..."

def get_rca_analysis(query: str, incident: dict, runbook: str):
    agent = RCAAgent()
    return agent.generate_explanation(query, incident, runbook)
