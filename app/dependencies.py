from dependency_injector import containers, providers
from app.services import AzureAssistantService 
from app.commandhost import CommandHost 

class Container(containers.DeclarativeContainer):
    # Defining providers for your dependencies
    service = providers.Factory(AzureAssistantService.process_user_input)
    command_host = providers.Singleton(CommandHost)
