from app.services import ingest


def test_chunk_text_with_overlap() -> None:
    text = "ABCDEFGHIJ"
    chunks = ingest.chunk_text(text, chunk_size=4, overlap=2)
    assert chunks == ["ABCD", "CDEF", "EFGH", "GHIJ", "IJ"]


def test_chunk_text_invalid_overlap() -> None:
    try:
        ingest.chunk_text("hola", chunk_size=4, overlap=4)
    except ValueError as exc:
        assert "overlap" in str(exc)
    else:
        raise AssertionError("Se esperaba ValueError para overlap inválido")


def test_extract_pdf_pages(monkeypatch) -> None:
    class FakePage:
        def __init__(self, text: str) -> None:
            self._text = text

        def get_text(self, _mode: str) -> str:
            return self._text

    class FakeDoc:
        def __enter__(self):
            return iter([FakePage("  página 1\ntexto  "), FakePage("\n\n")])

        def __exit__(self, exc_type, exc, tb) -> bool:
            return False

    def fake_open(*, stream: bytes, filetype: str):
        assert stream == b"pdf-bytes"
        assert filetype == "pdf"
        return FakeDoc()

    monkeypatch.setattr(ingest.fitz, "open", fake_open)

    pages = ingest.extract_pdf_pages(b"pdf-bytes")
    assert pages == [(1, "página 1 texto")]
