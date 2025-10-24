import os
import avito_messenger
from avito_messenger.models.post_send_message200_response import PostSendMessage200Response
from avito_messenger.models.send_message_request_body import SendMessageRequestBody
from avito_messenger.models.send_message_request_body_message import SendMessageRequestBodyMessage
from avito_messenger.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_messenger.Configuration(
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

#configuration.access_token = os.environ.get("ACCESS_TOKEN")

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = "Bearer zc9tj-heRAyB_5eExs31ywJivbpNYqJYlPRZfnJN" # str | Токен для авторизации
    user_id = 403662869 # int | Идентификатор пользователя (клиента)
    chat_id = 'u2u-u19PNvVypwmAXTQXzmjArw' # str | Идентификатор чата (клиента)
    send_message_request_body = SendMessageRequestBody(
        type="text",
        message=SendMessageRequestBodyMessage(text="Привет, чем могу помочь!")
    )  # SendMessageRequestBody | Отправление сообщения (optional)

    try:
        # Отправка сообщения
        api_response = api_instance.post_send_message(authorization, user_id, chat_id, send_message_request_body)
        print("The response of MessengerApi->post_send_message:\n")
        pprint(api_response.content.text)
    except ApiException as e:
        print(f"ApiException when calling MessengerApi->post_send_message: {e}\n")
    except Exception as e:
        print(f"Unexpected exception when calling MessengerApi->post_send_message: {e}\n")