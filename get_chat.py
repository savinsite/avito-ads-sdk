import avito_messenger
from avito_messenger.models.chat import Chat
from avito_messenger.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_messenger.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# configuration.access_token = os.environ["ACCESS_TOKEN"]

# configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer zc9tj-heRAyB_5eExs31ywJivbpNYqJYlPRZfnJN' # str | Токен для авторизации
    user_id = 403662869 # int | Идентификатор пользователя (клиента)
    chat_id = 'u2u-u19PNvVypwmAXTQXzmjArw' # str | Идентификатор чата (клиента)

    try:
        # Получение информации по чату
        api_response = api_instance.get_chat_by_id_v2(authorization, user_id, chat_id)
        print("The response of MessengerApi->get_chat_by_id_v2:\n")
        print(api_response.last_message.content.text)
    except Exception as e:
        print("Exception when calling MessengerApi->get_chat_by_id_v2: %s\n" % e)