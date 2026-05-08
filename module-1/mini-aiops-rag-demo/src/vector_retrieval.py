from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import pandas as pd

import chromadb
from chromadb.utils import embedding_functions


def get_collection(persist_dir: str | Path = "./chroma_db"):
    client = chromadb.PersistentClient(path=str(persist_dir))
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    return client.get_or_create_collection(name="incidents", embedding_function=emb_fn)


def seed_collection(collection, incidents_csv_path: str | Path) -> int:
    df = pd.read_csv(incidents_csv_path)

    documents: list[str] = []
    metadatas: list[dict[str, Any]] = []
    ids: list[str] = []

    for _, row in df.iterrows():
        incident_id = str(row["incident_id"])
        doc = " ".join(
            [
                str(row.get("service", "")),
                str(row.get("alert", "")),
                str(row.get("root_cause", "")),
                str(row.get("resolution", "")),
            ]
        ).strip()

        documents.append(doc)
        ids.append(incident_id)
        metadatas.append({k: (None if pd.isna(v) else v) for k, v in row.to_dict().items()})

    if not ids:
        return 0

    collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
    return len(ids)


def ensure_seeded(collection, incidents_csv_path: str | Path) -> int:
    existing = collection.count()
    if existing and existing > 0:
        return int(existing)
    return seed_collection(collection, incidents_csv_path=incidents_csv_path)


def query_best(collection, query: str) -> tuple[Optional[dict[str, Any]], float]:
    results = collection.query(query_texts=[query], n_results=1, include=["metadatas", "distances"])

    metadatas = results.get("metadatas")
    distances = results.get("distances")

    if not metadatas or not metadatas[0]:
        return None, 0.0

    distance = None
    if distances and distances[0]:
        distance = distances[0][0]

    score = 0.0
    if distance is not None:
        try:
            score = 1.0 / (1.0 + float(distance))
        except Exception:
            score = 0.0

    return dict(metadatas[0][0]), float(score)
