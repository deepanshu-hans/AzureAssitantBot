from app.services import AzureAssistantService

class AssistantHandler:
    """
    A class to handle assistant queries.
    """

    async def handle_query(user_input: str) -> str:
        """
        Method to process the user's query and interact with the assistant service.
        """
        # Pass the user input to the service layer
        return await AzureAssistantService.process_user_input(user_input)
