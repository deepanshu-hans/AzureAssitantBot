from app.commands import AssistantHandler

class CommandHost:
    """
    CommandHost serves as an intermediary between the API routes and the commands.
    """

    def __init__(self, assistant_handler: AssistantHandler):
        """
        Initialize the CommandHost with an instance of AssistantHandler.
        """
        self.assistant_handler = assistant_handler

    async def process_query(self, user_input: str) -> str:
        """
        Process the user's query by invoking the command.
        """
        try:
            # Call the command to handle the query
            result = await self.assistant_handler.handle_query(user_input)
            return result
        except Exception as e:
            # Handle errors gracefully and log them
            return f"An error occurred while processing the query: {str(e)}"
