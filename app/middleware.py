# app/middleware.py

from fastapi import Request, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Example: Log incoming requests
        print(f"Incoming Request: {request.method} {request.url}")
        
        # Example: Add custom headers or perform validation
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "AzureAssistantAPI"
        return response
