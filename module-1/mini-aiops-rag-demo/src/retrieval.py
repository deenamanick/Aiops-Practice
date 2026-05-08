from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd


@dataclass(frozen=True)
class MatchResult:
    incident_id: int
    service: str
    alert: str
    root_cause: str
    resolution: str
    severity: str
    runbook_steps: Optional[str]
    score: float


def _tokenize(text: str) -> set[str]:
    return {t for t in "".join(ch.lower() if ch.isalnum() else " " for ch in text).split() if t}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_data(data_dir: str | Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data_dir = Path(data_dir)
    incidents = pd.read_csv(data_dir / "incidents.csv")
    runbooks = pd.read_csv(data_dir / "runbooks.csv")
    return incidents, runbooks


def find_best_match(query: str, incidents: pd.DataFrame) -> tuple[pd.Series, float]:
    q = _tokenize(query)

    best_score = -1.0
    best_row = None

    for _, row in incidents.iterrows():
        candidate_text = f"{row.get('service','')} {row.get('alert','')} {row.get('root_cause','')} {row.get('resolution','')}"
        score = _jaccard(q, _tokenize(str(candidate_text)))
        if score > best_score:
            best_score = score
            best_row = row

    if best_row is None:
        raise RuntimeError("No incidents found in incidents.csv")

    return best_row, float(best_score)


def lookup_runbook(service: str, runbooks: pd.DataFrame) -> Optional[str]:
    rows = runbooks[runbooks["service"] == service]
    if rows.empty:
        return None
    return str(rows.iloc[0]["steps"])


def analyze_query(query: str, data_dir: str | Path) -> MatchResult:
    incidents, runbooks = load_data(data_dir)
    row, score = find_best_match(query, incidents)

    runbook_steps = lookup_runbook(str(row["service"]), runbooks)

    return MatchResult(
        incident_id=int(row["incident_id"]),
        service=str(row["service"]),
        alert=str(row["alert"]),
        root_cause=str(row["root_cause"]),
        resolution=str(row["resolution"]),
        severity=str(row["severity"]),
        runbook_steps=runbook_steps,
        score=score,
    )
