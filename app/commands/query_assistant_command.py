from app.services import AzureAssistantService

class AssistantHandler:
    """
    A class to handle assistant queries.
    """

    def __init__(self, assistant_service: AzureAssistantService):
        """
        Initialize the AssistantHandler with an instance of AzureAssistantService.
        """
        self.assistant_service = assistant_service

    async def handle_query(self, user_input: str) -> str:
        """
        Instance method to process the user's query and interact with the assistant service.
        """
        try:
            # Pass the user input to the service layer
            return await self.assistant_service.process_user_input(user_input)
        except Exception as e:
            # Handle errors and log them
            return f"An error occurred: {str(e)}"
