import time
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="aedc8ec21a8b47908eadb2fa8ac648df",
    api_version="2024-08-01-preview",
    azure_endpoint="https://planb-eastus2-openai-service.openai.azure.com/",
)

async def process_user_input(user_input: str) -> str:
    """
    Core service logic to process the user's input and get a response from Azure OpenAI.
    """
    try:
        # Create a thread with the user's message
        thread = client.beta.threads.create(
            messages=[{"role": "user", "content": user_input}]
        )

        # Submit the thread to the assistant
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI")

        # Wait for the run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(1)

        # Get the latest message from the thread
        message_response = client.beta.threads.messages.list(thread_id=thread.id)
        messages = message_response.data
        latest_message = messages[0]
        return latest_message.content[0].text.value

    except Exception as e:
        raise Exception(f"Error in processing: {str(e)}")
