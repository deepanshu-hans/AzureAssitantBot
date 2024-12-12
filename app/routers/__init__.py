from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.services import AzureAssistantService


class AssistantRouter:
    """
    A class-based router for handling assistant-related queries.
    """

    def __init__(self, api_key: str, api_version: str, azure_endpoint: str, assistant_id: str):
        self.router = APIRouter()
        self.api_key = api_key
        self.api_version = api_version
        self.azure_endpoint = azure_endpoint
        self.assistant_id = assistant_id

        # Define routes
        self.router.post(
            "/query",
            summary="Submit a user query to the assistant",
            description="This endpoint processes a user's query and provides a response from the assistant."
        )(self.assistant_query)

    class AssistantQueryPayload(BaseModel):
        """
        Pydantic model for assistant query payload.
        """
        content: str = Field(
            ...,
            example="Which type of gadgets are available?",
            description="The user's query to be processed by the assistant."
        )

    def get_assistant_service(self) -> AzureAssistantService:
        """
        Creates and returns an instance of the AzureAssistantService.
        """
        return AzureAssistantService(
            api_key=self.api_key,
            api_version=self.api_version,
            azure_endpoint=self.azure_endpoint,
            assistant_id=self.assistant_id,
        )

    async def assistant_query(self, payload: AssistantQueryPayload):
        """
        Endpoint to submit a user query to the assistant.
        """
        try:
            user_input = payload.content
            service = self.get_assistant_service()
            response = await service.process_user_input(user_input)
            return {"response": response}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


# Instantiate the router with required configurations
assistant_router = AssistantRouter(
    api_key="aedc8ec21a8b47908eadb2fa8ac648df",
    api_version="2024-08-01-preview",
    azure_endpoint="https://planb-eastus2-openai-service.openai.azure.com/",
    assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI"
)

# Use the router in your FastAPI app
router = assistant_router.router