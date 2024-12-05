from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.services import AzureAssistantService


class AssistantRouter:
    """
    A class-based router for handling assistant-related queries.
    """

    def __init__(self):
        self.router = APIRouter()
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

    async def get_assistant_service() -> AzureAssistantService:
        """
        Dependency injection for the assistant service.
        """
        return AzureAssistantService(
            api_key="aedc8ec21a8b47908eadb2fa8ac648df",
            api_version="2024-08-01-preview",
            azure_endpoint="https://planb-eastus2-openai-service.openai.azure.com/",
            assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI",
        )

    @staticmethod
    async def assistant_query(
        payload: AssistantQueryPayload,
        service: AzureAssistantService = Depends(get_assistant_service),
    ):
        """
        Endpoint to submit a user query to the assistant.
        """
        try:
            user_input = payload.content
            response = await service.process_user_input(user_input)
            return {"response": response}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


assistant_router = AssistantRouter()
router = assistant_router.router