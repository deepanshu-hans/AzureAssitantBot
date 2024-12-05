from app.commands import AssistantHandler

class CommandHost:
    """
    CommandHost serves as an intermediary between the API routes and the commands.
    """

    @staticmethod
    async def process_query(user_input: str) -> str:
        """
        Process the user's query by invoking the command.
        """
        try:
            # Call the command to handle the query
            result = await AssistantHandler.handle_query(user_input)
            return result
        except Exception as e:
            # Handle errors gracefully and log them
            return f"An error occurred while processing the query: {str(e)}"
