# app/routers/assistant.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.commands.assistant import handle_assistant_query

router = APIRouter()


class AssistantQueryPayload(BaseModel):
    content: str = Field(
        ...,
        example="which type of gadgets are available?",
        description="The user's query to be processed by the assistant."
    )

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

        # Delegate to the command layer
        response = await handle_assistant_query(user_input)
        return {"runStatus": "completed", "message": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
