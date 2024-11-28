from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from app.commandhost import CommandHost
from app.dependencies import Container
from app.services import process_user_input 

router = APIRouter()


class AssistantQueryPayload(BaseModel):
    content: str = Field(
        ...,
        example="which type of gadgets are available?",
        description="The user's query to be processed by the assistant."
    )

# Inject the AssistantService dependency
async def get_assistant_service(service: process_user_input = Depends(Container.service)) -> process_user_input:
    return service

@router.post(
    "/query",
    summary="Submit a user query to the assistant",
    description="This endpoint processes a user's query and provides a response from the assistant."
)
    
async def assistant_query(payload: AssistantQueryPayload):
    """
    Endpoint to submit a user query to the assistant.
    """
    try:
        user_input = payload.content

        # Pass the query to CommandHost
        response = await CommandHost.process_query(user_input)
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
