# Arquitectura inicial

Este repositorio parte de una arquitectura mínima para un servicio RAG:

- **FastAPI** como capa HTTP.
- **pydantic-settings** para configuración por entorno.
- Endpoint `GET /rag/query` como stub para integrar retrieval + generation.
- Endpoint `POST /ingest` para carga de PDFs vía multipart.
- Extracción de texto con **PyMuPDF** y chunking con overlap.
- Persistencia local en SQLite (`chunks`) con metadata por fragmento.
- Carpeta `tests/` para pruebas unitarias/API.
