import avito_autorization
from avito_autorization.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_autorization.Configuration(
    host = "https://api.avito.ru"
)



# Enter a context with an instance of the API client
with avito_autorization.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_autorization.AccessApi(api_client)
    client_id = 'RHlN3JXvQ1SlaY-dZw_9' # str | 
    client_secret = 'rKQ1SW1YMtR8n0eAce8-AURWYPuydvrAijjdJb2K' # str | 
    grant_type = 'client_credentials' # str |  (default to 'client_credentials')

    try:
        # Получение access token
        api_response = api_instance.get_access_token(client_id, client_secret, grant_type)
        print("The response of AccessApi->get_access_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessApi->get_access_token: %s\n" % e)
