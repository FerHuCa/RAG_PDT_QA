from fastapi import APIRouter

router = APIRouter()


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
