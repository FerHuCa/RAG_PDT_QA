import sqlite3
from pathlib import Path


class ChunkStorage:
    def __init__(self, db_path: str) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS chunks (
                    doc_id TEXT NOT NULL,
                    chunk_id INTEGER NOT NULL,
                    page INTEGER NOT NULL,
                    text TEXT NOT NULL,
                    PRIMARY KEY (doc_id, chunk_id)
                )
                """
            )
            conn.commit()

    def save_chunks(self, chunks: list[dict[str, str | int]]) -> int:
        if not chunks:
            return 0

        rows = [
            (chunk["doc_id"], chunk["chunk_id"], chunk["page"], chunk["text"])
            for chunk in chunks
        ]

        with sqlite3.connect(self.db_path) as conn:
            conn.executemany(
                """
                INSERT INTO chunks (doc_id, chunk_id, page, text)
                VALUES (?, ?, ?, ?)
                """,
                rows,
            )
            conn.commit()

        return len(rows)
