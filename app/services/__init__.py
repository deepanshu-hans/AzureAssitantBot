import time
from openai import AzureOpenAI

class AzureAssistantService:
    """
    A service class for interacting with Azure OpenAI to process user inputs.
    """

    def __init__(self, api_key: str, api_version: str, azure_endpoint: str, assistant_id: str):
        """
        Initialize the AzureAssistantService with necessary configurations.

        :param api_key: Azure OpenAI API key.
        :param api_version: Azure OpenAI API version.
        :param azure_endpoint: Azure OpenAI service endpoint.
        :param assistant_id: ID of the assistant to use for queries.
        """
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint,
        )
        self.assistant_id = assistant_id

    async def process_user_input(self, user_input: str) -> str:
        """
        Process the user's input and get a response from Azure OpenAI.
        """
        try:
            # Create a thread with the user's message
            thread = self.client.beta.threads.create(
                messages=[{"role": "user", "content": user_input}]
            )

            # Submit the thread to the assistant
            run = self.client.beta.threads.runs.create(
                thread_id=thread.id, assistant_id=self.assistant_id
            )

            # Wait for the run to complete
            while run.status != "completed":
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=thread.id, run_id=run.id
                )
                time.sleep(1)

            # Get the latest message from the thread
            message_response = self.client.beta.threads.messages.list(thread_id=thread.id)
            messages = message_response.data
            latest_message = messages[0]
            return latest_message.content[0].text.value

        except Exception as e:
            raise Exception(f"Error in processing: {str(e)}")


# Example of instantiating and using the service
if __name__ == "__main__":
    # Example initialization
    service = AzureAssistantService(
        api_key="aedc8ec21a8b47908eadb2fa8ac648df",
        api_version="2024-08-01-preview",
        azure_endpoint="https://planb-eastus2-openai-service.openai.azure.com/",
        assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI",
    )