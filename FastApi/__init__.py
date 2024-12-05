from fastapi import FastAPI
from app.services import AzureAssistantService
from app.routers import assistant_router
from app.dependencies import Container

# Dependency that provides an instance of AzureAssistantService
def get_assistant_service() -> AzureAssistantService:
    return AzureAssistantService(
        api_key="aedc8ec21a8b47908eadb2fa8ac648df",
        api_version="2024-08-01-preview",
        azure_endpoint="https://planb-eastus2-openai-service.openai.azure.com/",
        assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI",
    )

app = FastAPI(
    title="Azure Assistant API",
    description="Interact with an AI assistant using Azure OpenAI services",
    version="1.0.0",
)

container = Container()

app.include_router(assistant_router.router, prefix="/api/v1/assistant", tags=["Assistant"])