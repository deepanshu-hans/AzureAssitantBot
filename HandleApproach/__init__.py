import logging
import azure.functions as func
from fastapi import FastAPI
from azure.functions import AsgiMiddleware
from FastApi import app 

# Create an instance of ASGI middleware with the FastAPI app
fastapi_asgi_app = AsgiMiddleware(app)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Main entry point for the Azure Function. This wraps the FastAPI app.
    """
    logging.info('Processing request...')
    
    # Use the middleware to handle the request and return the response
    return fastapi_asgi_app(req)
