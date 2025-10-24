import os
from typing import List, Optional


class Settings:
    APP_NAME: str = "Avito Messenger Service"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Backend API to integrate Avito Messenger for frontend and n8n."
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    ORIGINS: List[str] = [o.strip() for o in os.getenv("ORIGINS", "").split(",") if o.strip()] or ["*"]
    ACCESS_TOKEN: Optional[str] = os.getenv("ACCESS_TOKEN")


settings = Settings()