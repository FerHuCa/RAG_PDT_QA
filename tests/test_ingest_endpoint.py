from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ingest_rejects_non_pdf() -> None:
    response = client.post(
        "/ingest",
        files={"file": ("note.txt", b"hello", "text/plain")},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Solo se permiten archivos PDF"
