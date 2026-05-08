from __future__ import annotations

from pathlib import Path

from src.vector_retrieval import ensure_seeded, get_collection


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    incidents_csv = base_dir / "data" / "incidents.csv"

    collection = get_collection(persist_dir=base_dir / "chroma_db")
    count = ensure_seeded(collection, incidents_csv_path=incidents_csv)

    print(f"Seeded collection 'incidents' (records: {count})")


if __name__ == "__main__":
    main()
