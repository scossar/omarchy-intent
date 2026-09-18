"""Populate SQLite with descriptions of user intentions."""

import argparse
import sqlite3
from pathlib import Path

import yaml

DATA_PATH = Path(__file__).parent / "data" / "user-intentions.yaml"


def populate(database: Path) -> int:
    """Insert or update the intention descriptions in a transaction."""
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    connection = sqlite3.connect(database)
    try:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS intentions (
                    id INTEGER PRIMARY KEY,
                    intention TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL
                )

            """)
            connection.executemany(
                """
                INSERT INTO intentions
                    (intention, description)
                VALUES (?, ?)
                ON CONFLICT (intention) DO UPDATE SET
                    description = excluded.description
                """,
                [
                    (intention["intention"], intention["description"])
                    for intention in data
                ],
            )
    finally:
        connection.close()
    return len(data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "database",
        nargs="?",
        type=Path,
        default=Path("intentions.sqlite3"),
        help="SQLite file to populate (default: intentions.sqlite3)",
    )
    args = parser.parse_args()
    count = populate(args.database)
    print(f"Loaded {count} intention entries into {args.database}.")


if __name__ == "__main__":
    main()
