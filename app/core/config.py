from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "RAG FastAPI Service"
    app_version: str = "0.1.0"
    environment: str = "dev"
    log_level: str = "INFO"

    # Variables típicas de RAG
    vector_store_url: str = "http://localhost:6333"
    llm_provider: str = "openai"
    openai_api_key: str = ""

    # Ingestion local
    sqlite_path: str = "data/chunks.db"
    chunk_size: int = 500
    chunk_overlap: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
