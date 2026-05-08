from __future__ import annotations

from pathlib import Path

from src.retrieval import MatchResult, analyze_query


def test_analyze_query_returns_matchresult() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"

    result = analyze_query("High 5xx errors on checkout service", data_dir)

    assert isinstance(result, MatchResult)
    assert isinstance(result.incident_id, int)
    assert isinstance(result.service, str)
    assert 0.0 <= result.score <= 1.0

