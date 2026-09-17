"""Embed intention descriptions and save them to a persistent Chroma collection"""

import argparse
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import cast

import chromadb
from chromadb.api.types import Embeddable, EmbeddingFunction
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction


def create_embeddings(
    database: Path,
    chroma_path: Path,
    collection_name: str = "user-intentions",
) -> int:
    """Generate and upsert embeddings for the descriptions stored in SQLite."""
    with closing(
        sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    ) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute("""
            SELECT id, intention, description
            FROM intentions
            ORDER BY id
        """).fetchall()

    if not rows:
        return 0

    embedding_function = DefaultEmbeddingFunction()
    client = chromadb.PersistentClient(path=str(chroma_path))
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=cast(EmbeddingFunction[Embeddable], embedding_function),
        metadata={"embedding_model": "all-MiniLM-L6-v2"},
    )

    for start in range(0, len(rows), 128):
        batch = rows[start : start + 128]
        documents = [row["description"] for row in batch]

        embeddings = embedding_function(documents)

        collection.upsert(
            ids=[row["intention"] for row in batch],
            embeddings=embeddings,
            documents=documents,
            metadatas=[{"intention": row["intention"]} for row in batch],
        )
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database",
        type=Path,
        default=Path("intentions.sqlite3"),
        help="Populated SQLite source (default: intentions.sqlite3)",
    )
    parser.add_argument(
        "--chroma",
        type=Path,
        default=Path("data/chroma"),
        help="Persistent Chroma directory (default: data/chroma)",
    )
    parser.add_argument(
        "--collection",
        default="user-intentions",
        help="Chroma collection name (default: user-intentions)",
    )
    args = parser.parse_args()
    count = create_embeddings(args.database, args.chroma, args.collection)
    print(
        f"Stored {count} intention descriptions and embeddings in {args.chroma} ({args.collection})."
    )


if __name__ == "__main__":
    main()
