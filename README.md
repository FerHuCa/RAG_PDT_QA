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
│   └── main.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── architecture.md
├── scripts/
│   └── run.sh
├── tests/
│   └── test_health.py
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
