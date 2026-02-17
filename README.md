# RAG FastAPI Service (Python 3.11)

Plantilla base para construir un servicio **RAG (Retrieval-Augmented Generation)** con FastAPI.

## Requisitos

- Python 3.11
- pip
- (Opcional) Docker + Docker Compose

## Estructura

```text
.
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── services/
│   │   ├── ingest.py
│   │   └── storage.py
│   └── main.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── architecture.md
├── scripts/
│   └── run.sh
├── tests/
│   ├── test_health.py
│   ├── test_ingest_endpoint.py
│   └── test_ingest_utils.py
├── .env.example
├── Makefile
└── pyproject.toml
```

## Ejecutar local

```bash
cp .env.example .env
make install
make run
```

Servicio disponible en:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## Endpoint de ingestión PDF

`POST /ingest` acepta `multipart/form-data` con un archivo `file` (PDF).

Pipeline implementado:
1. Extrae texto por página con **PyMuPDF**.
2. Limpia espacios y normaliza texto.
3. Aplica chunking con overlap configurable.
4. Guarda chunks en **SQLite local** con metadata:
   - `doc_id`
   - `chunk_id`
   - `page`
   - `text`

## Ejecutar tests y calidad

```bash
make test
make lint
make format
```

## Ejecutar con Docker

```bash
cp .env.example .env
docker compose -f docker/docker-compose.yml up --build
```

## Variables de entorno

Se cargan desde `.env` usando `pydantic-settings` (`app/core/config.py`).
Variables iniciales incluidas en `.env.example`.
