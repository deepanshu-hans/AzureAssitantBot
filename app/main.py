# app/main.py

from fastapi import FastAPI
from app.middleware import CustomMiddleware
from app.routers import assistant

app = FastAPI(
    title="Azure Assistant API",
    description="Interact with an AI assistant using Azure OpenAI services",
    version="1.0.0",
)

# Add middleware
app.add_middleware(CustomMiddleware)

# Include routers
app.include_router(assistant.router, prefix="/api/v1/assistant", tags=["Assistant"])