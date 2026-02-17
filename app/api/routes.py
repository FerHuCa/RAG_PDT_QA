from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import settings
from app.services.ingest import ingest_pdf
from app.services.storage import ChunkStorage

router = APIRouter()
storage = ChunkStorage(settings.sqlite_path)


@router.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/rag/query", tags=["rag"])
def rag_query(q: str) -> dict[str, str]:
    """Endpoint base para consulta RAG (stub inicial)."""
    return {
        "query": q,
        "answer": "Implementa aquí tu pipeline de retrieval + generation.",
    }


@router.post("/ingest", tags=["ingestion"])
async def ingest(file: UploadFile = File(...)) -> dict[str, str | int]:
    is_pdf = file.content_type == "application/pdf" or file.filename.endswith(".pdf")
    if not is_pdf:
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")

    pdf_bytes = await file.read()
    if not pdf_bytes:
        raise HTTPException(status_code=400, detail="Archivo PDF vacío")

    result = ingest_pdf(
        pdf_bytes,
        storage=storage,
        chunk_size=settings.chunk_size,
        overlap=settings.chunk_overlap,
    )
    return result
