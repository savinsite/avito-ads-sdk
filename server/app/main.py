from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.v1.messenger import router as messenger_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

# v1 API
app.include_router(messenger_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    # Запускайте как модуль, чтобы работали относительные импорты:
    # uvicorn server.app.main:app --reload
    uvicorn.run("server.app.main:app", host=settings.HOST, port=settings.PORT, reload=True)