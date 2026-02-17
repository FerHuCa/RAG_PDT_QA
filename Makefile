PYTHON ?= python3.11
PIP ?= $(PYTHON) -m pip
UVICORN_APP ?= app.main:app

.PHONY: install run test lint format

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]

run:
	uvicorn $(UVICORN_APP) --host 0.0.0.0 --port 8000 --reload

test:
	pytest

lint:
	ruff check .
	black --check .

format:
	ruff check . --fix
	black .
