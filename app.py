import time
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from openai import AzureOpenAI # type: ignore

# Initialize Flask
app = Flask(__name__)

# Swagger setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Azure-Assistant-API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Azure Assistant setup
client = AzureOpenAI(
    api_key="aedc8ec21a8b47908eadb2fa8ac648df",  
    api_version="2024-08-01-preview",
    azure_endpoint = "https://planb-eastus2-openai-service.openai.azure.com/"
    )

@app.route('/assistant/query', methods=['POST'])
def assistant_query():
    try:
        # Get user input from request body
        user_input = request.json.get('content')

        # Create thread with user message
        thread = client.beta.threads.create(
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )

        # Submit thread to assistant
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id="asst_3OtAZTPpmi0sKhR9pAh2qkFI")
        print(f"Run Created: {run.id}")

        # Wait for run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            print(f"Run Status: {run.status}")
            time.sleep(1)

        print("Run Completed!")

        # Get latest message from the thread
        message_response = client.beta.threads.messages.list(thread_id=thread.id)
        messages = message_response.data

        # Extract response content
        latest_message = messages[0]
        assistant_response = latest_message.content[0].text.value

        # Return assistant response as JSON
        return jsonify({
            "runStatus": "completed",
            "message": assistant_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
