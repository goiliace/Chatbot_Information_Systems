from pydantic_settings import BaseSettings, SettingsConfigDict



class Setting(BaseSettings):
    OPENAI_API_KEY: str
    QDRANT_URL: str
    EMBEDDING_MODEL: str
    COLLECTION_NAME: str
    GROQ_API_KEY: str
    API_V1_STR: str = '/api/v1'
    POSTGRES_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    model_config = SettingsConfigDict(
        env_file='.env',
        extra="ignore",
    )

settings = Setting()
