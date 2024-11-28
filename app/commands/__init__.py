from app.services import process_user_input

async def handle_assistant_query(user_input: str) -> str:
    """
    Command to process the user's query and interact with the assistant service.
    """
    # Pass the user input to the service layer
    return await process_user_input(user_input)
