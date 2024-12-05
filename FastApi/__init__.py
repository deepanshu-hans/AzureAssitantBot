from fastapi import FastAPI
from app.routers import assistant_router
from app.dependencies import Container

app = FastAPI(
    title="Azure Assistant API",
    description="Interact with an AI assistant using Azure OpenAI services",
    version="1.0.0",
)

container = Container()

app.include_router(assistant_router.router, prefix="/api/v1/assistant", tags=["Assistant"])