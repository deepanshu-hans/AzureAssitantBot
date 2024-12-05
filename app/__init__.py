from fastapi import FastAPI
import azure.functions as func
from app.routers import assistant_router

app = FastAPI(
    title="My FastAPI Function App",
    description="An API to demonstrate FastAPI with Azure Functions",
    version="1.0.0",
    docs_url="/docs",  
    redoc_url="/redoc",
)

app.include_router(assistant_router.router, prefix="/api/v1/assistant", tags=["Assistant"])

async def main(req: func.HttpRequest) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req)
