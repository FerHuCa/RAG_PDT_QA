# Arquitectura inicial

Este repositorio parte de una arquitectura mínima para un servicio RAG:

- **FastAPI** como capa HTTP.
- **pydantic-settings** para configuración por entorno.
- Endpoint `GET /rag/query` como stub para integrar retrieval + generation.
- Carpeta `tests/` para pruebas unitarias/API.
