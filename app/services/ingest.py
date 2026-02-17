import re
from uuid import uuid4

import fitz

from app.services.storage import ChunkStorage


def clean_text(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text)
    return normalized.strip()


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    if chunk_size <= 0:
        msg = "chunk_size debe ser mayor a 0"
        raise ValueError(msg)

    if overlap < 0 or overlap >= chunk_size:
        msg = "overlap debe ser >= 0 y menor que chunk_size"
        raise ValueError(msg)

    if not text:
        return []

    chunks: list[str] = []
    step = chunk_size - overlap
    start = 0

    while start < len(text):
        chunk = text[start : start + chunk_size]
        chunks.append(chunk)
        start += step

    return chunks


def extract_pdf_pages(pdf_bytes: bytes) -> list[tuple[int, str]]:
    pages: list[tuple[int, str]] = []
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page_index, page in enumerate(doc):
            text = clean_text(page.get_text("text"))
            if text:
                pages.append((page_index + 1, text))

    return pages


def build_chunks(
    pages: list[tuple[int, str]], chunk_size: int = 500, overlap: int = 100
) -> list[dict[str, str | int]]:
    doc_id = str(uuid4())
    all_chunks: list[dict[str, str | int]] = []
    chunk_id = 1

    for page_number, text in pages:
        for chunk in chunk_text(text, chunk_size=chunk_size, overlap=overlap):
            all_chunks.append(
                {
                    "doc_id": doc_id,
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "text": chunk,
                }
            )
            chunk_id += 1

    return all_chunks


def ingest_pdf(
    pdf_bytes: bytes,
    storage: ChunkStorage,
    chunk_size: int = 500,
    overlap: int = 100,
) -> dict[str, str | int]:
    pages = extract_pdf_pages(pdf_bytes)
    chunks = build_chunks(pages, chunk_size=chunk_size, overlap=overlap)
    saved = storage.save_chunks(chunks)

    doc_id = chunks[0]["doc_id"] if chunks else str(uuid4())

    return {
        "doc_id": str(doc_id),
        "pages": len(pages),
        "chunks": saved,
    }
