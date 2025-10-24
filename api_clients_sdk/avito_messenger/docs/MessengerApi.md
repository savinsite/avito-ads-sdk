# avito_messenger.MessengerApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_read**](MessengerApi.md#chat_read) | **POST** /messenger/v1/accounts/{user_id}/chats/{chat_id}/read | Прочитать чат
[**delete_message**](MessengerApi.md#delete_message) | **POST** /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/{message_id} | Удаление сообщения
[**get_chat_by_id_v2**](MessengerApi.md#get_chat_by_id_v2) | **GET** /messenger/v2/accounts/{user_id}/chats/{chat_id} | Получение информации по чату
[**get_chats_v2**](MessengerApi.md#get_chats_v2) | **GET** /messenger/v2/accounts/{user_id}/chats | Получение информации по чатам
[**get_messages_v3**](MessengerApi.md#get_messages_v3) | **GET** /messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/ | Получение списка сообщений V3
[**get_subscriptions**](MessengerApi.md#get_subscriptions) | **POST** /messenger/v1/subscriptions | Получение подписок (webhooks)
[**get_voice_files**](MessengerApi.md#get_voice_files) | **GET** /messenger/v1/accounts/{user_id}/getVoiceFiles | Получение голосовых сообщений
[**post_blacklist_v2**](MessengerApi.md#post_blacklist_v2) | **POST** /messenger/v2/accounts/{user_id}/blacklist | Добавление пользователя в blacklist
[**post_send_image_message**](MessengerApi.md#post_send_image_message) | **POST** /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/image | Отправка сообщения с изображением
[**post_send_message**](MessengerApi.md#post_send_message) | **POST** /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages | Отправка сообщения
[**post_webhook_unsubscribe**](MessengerApi.md#post_webhook_unsubscribe) | **POST** /messenger/v1/webhook/unsubscribe | Отключение уведомлений (webhooks)
[**post_webhook_v3**](MessengerApi.md#post_webhook_v3) | **POST** /messenger/v3/webhook | Включение уведомлений V3 (webhooks)
[**upload_images**](MessengerApi.md#upload_images) | **POST** /messenger/v1/accounts/{user_id}/uploadImages | Загрузка изображений


# **chat_read**
> ChatRead200Response chat_read(authorization, user_id, chat_id)

Прочитать чат

После успешного получения списка сообщений необходимо вызвать этот метод для того, чтобы чат стал прочитанным.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.chat_read200_response import ChatRead200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)

    try:
        # Прочитать чат
        api_response = api_instance.chat_read(authorization, user_id, chat_id)
        print("The response of MessengerApi->chat_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->chat_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 

### Return type

[**ChatRead200Response**](ChatRead200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> object delete_message(authorization, user_id, chat_id, message_id)

Удаление сообщения

Сообщение не пропадает из истории, а меняет свой тип на deleted.
Удалять сообщения можно не позднее часа с момента их отправки.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)
    message_id = 'message_id_example' # str | Идентификатор сообщения

    try:
        # Удаление сообщения
        api_response = api_instance.delete_message(authorization, user_id, chat_id, message_id)
        print("The response of MessengerApi->delete_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->delete_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 
 **message_id** | **str**| Идентификатор сообщения | 

### Return type

**object**

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_id_v2**
> Chat get_chat_by_id_v2(authorization, user_id, chat_id)

Получение информации по чату

Возвращает данные чата и последнее сообщение в нем


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)

    try:
        # Получение информации по чату
        api_response = api_instance.get_chat_by_id_v2(authorization, user_id, chat_id)
        print("The response of MessengerApi->get_chat_by_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->get_chat_by_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 

### Return type

[**Chat**](Chat.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_v2**
> Chats get_chats_v2(authorization, user_id, item_ids=item_ids, unread_only=unread_only, chat_types=chat_types, limit=limit, offset=offset)

Получение информации по чатам

Возвращает список чатов


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.chats import Chats
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    item_ids = [12345,6789] # List[int] | Получение чатов только по объявлениям с указанными item_id (optional)
    unread_only = False # bool | При значении true метод возвращает только непрочитанные чаты (optional) (default to False)
    chat_types = ['u2i,u2u'] # List[str] | Фильтрация возвращаемых чатов.  * u2i — чаты по объявлениям; * u2u — чаты между пользователями;  (optional)
    limit = 100 # int | Количество сообщений / чатов для запроса (optional) (default to 100)
    offset = 0 # int | Сдвиг сообщений / чатов для запроса (optional) (default to 0)

    try:
        # Получение информации по чатам
        api_response = api_instance.get_chats_v2(authorization, user_id, item_ids=item_ids, unread_only=unread_only, chat_types=chat_types, limit=limit, offset=offset)
        print("The response of MessengerApi->get_chats_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->get_chats_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **item_ids** | [**List[int]**](int.md)| Получение чатов только по объявлениям с указанными item_id | [optional] 
 **unread_only** | **bool**| При значении true метод возвращает только непрочитанные чаты | [optional] [default to False]
 **chat_types** | [**List[str]**](str.md)| Фильтрация возвращаемых чатов.  * u2i — чаты по объявлениям; * u2u — чаты между пользователями;  | [optional] 
 **limit** | **int**| Количество сообщений / чатов для запроса | [optional] [default to 100]
 **offset** | **int**| Сдвиг сообщений / чатов для запроса | [optional] [default to 0]

### Return type

[**Chats**](Chats.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_v3**
> List[MessagesInner] get_messages_v3(authorization, user_id, chat_id, limit=limit, offset=offset)

Получение списка сообщений V3

Получение списка сообщений.  **Не помечает чат прочитанным.**
После успешного получения списка сообщений необходимо вызвать [метод](https://api.avito.ru/docs/api.html#operation/chatRead), который сделает сообщения прочитанными.
Для получения новых сообщений в реальном времени используйте [webhooks](https://api.avito.ru/docs/api.html#operation/postWebhookV3)


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.messages_inner import MessagesInner
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)
    limit = 100 # int | Количество сообщений / чатов для запроса (optional) (default to 100)
    offset = 0 # int | Сдвиг сообщений / чатов для запроса (optional) (default to 0)

    try:
        # Получение списка сообщений V3
        api_response = api_instance.get_messages_v3(authorization, user_id, chat_id, limit=limit, offset=offset)
        print("The response of MessengerApi->get_messages_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->get_messages_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 
 **limit** | **int**| Количество сообщений / чатов для запроса | [optional] [default to 100]
 **offset** | **int**| Сдвиг сообщений / чатов для запроса | [optional] [default to 0]

### Return type

[**List[MessagesInner]**](MessagesInner.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> GetSubscriptions200Response get_subscriptions(authorization)

Получение подписок (webhooks)

Получение списка подписок


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.get_subscriptions200_response import GetSubscriptions200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации

    try:
        # Получение подписок (webhooks)
        api_response = api_instance.get_subscriptions(authorization)
        print("The response of MessengerApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 

### Return type

[**GetSubscriptions200Response**](GetSubscriptions200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_files**
> VoiceFiles get_voice_files(authorization, user_id, voice_ids)

Получение голосовых сообщений

Метод используется для получения ссылки на файл с голосовым сообщением по идентификатору voice_id, получаемому из тела сообщения с типом voice.

Особенности работы с голосовыми сообщениями:
- Голосовые сообщения Авито используют кодек **[opus](https://ru.wikipedia.org/wiki/Opus_(%D0%BA%D0%BE%D0%B4%D0%B5%D0%BA))** внутри **.mp4** контейнера; 
- Ссылка на голосовое сообщение доступна в течение **одного часа** с момента запроса. Попытка получить файл по ссылке спустя это время приведёт к ошибке. Для восстановления доступа необходимо получить новую ссылку на файл;
- Как и с обычными сообщениями, получение ссылки на файл доступно только для пользователей, находящихся в беседе, где голосовое сообщение было отправлено;


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.voice_files import VoiceFiles
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    voice_ids = ['voice_ids_example'] # List[str] | Получение файлов голосовых сообщений с указанными voice_id

    try:
        # Получение голосовых сообщений
        api_response = api_instance.get_voice_files(authorization, user_id, voice_ids)
        print("The response of MessengerApi->get_voice_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->get_voice_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **voice_ids** | [**List[str]**](str.md)| Получение файлов голосовых сообщений с указанными voice_id | 

### Return type

[**VoiceFiles**](VoiceFiles.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_blacklist_v2**
> post_blacklist_v2(authorization, user_id, add_blacklist_request_body=add_blacklist_request_body)

Добавление пользователя в blacklist

Добавление пользователя в blacklist


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.add_blacklist_request_body import AddBlacklistRequestBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    add_blacklist_request_body = avito_messenger.AddBlacklistRequestBody() # AddBlacklistRequestBody | Добавление пользователя в blacklist (optional)

    try:
        # Добавление пользователя в blacklist
        api_instance.post_blacklist_v2(authorization, user_id, add_blacklist_request_body=add_blacklist_request_body)
    except Exception as e:
        print("Exception when calling MessengerApi->post_blacklist_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **add_blacklist_request_body** | [**AddBlacklistRequestBody**](AddBlacklistRequestBody.md)| Добавление пользователя в blacklist | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_send_image_message**
> PostSendImageMessage200Response post_send_image_message(authorization, user_id, chat_id, send_image_message_request_body=send_image_message_request_body)

Отправка сообщения с изображением

Метод используется для отправки сообщения с изображением.

Для отправки сообщения с изображением необходимо передать в запросе id изображения, полученного после загрузки.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.post_send_image_message200_response import PostSendImageMessage200Response
from avito_messenger.models.send_image_message_request_body import SendImageMessageRequestBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)
    send_image_message_request_body = avito_messenger.SendImageMessageRequestBody() # SendImageMessageRequestBody | Вложение с изображением (optional)

    try:
        # Отправка сообщения с изображением
        api_response = api_instance.post_send_image_message(authorization, user_id, chat_id, send_image_message_request_body=send_image_message_request_body)
        print("The response of MessengerApi->post_send_image_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->post_send_image_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 
 **send_image_message_request_body** | [**SendImageMessageRequestBody**](SendImageMessageRequestBody.md)| Вложение с изображением | [optional] 

### Return type

[**PostSendImageMessage200Response**](PostSendImageMessage200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_send_message**
> PostSendMessage200Response post_send_message(authorization, user_id, chat_id, send_message_request_body=send_message_request_body)

Отправка сообщения

На данный момент можно отправить только текстовое сообщение


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.post_send_message200_response import PostSendMessage200Response
from avito_messenger.models.send_message_request_body import SendMessageRequestBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    chat_id = 'chat_id_example' # str | Идентификатор чата (клиента)
    send_message_request_body = avito_messenger.SendMessageRequestBody() # SendMessageRequestBody | Отправление сообщения (optional)

    try:
        # Отправка сообщения
        api_response = api_instance.post_send_message(authorization, user_id, chat_id, send_message_request_body=send_message_request_body)
        print("The response of MessengerApi->post_send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->post_send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **chat_id** | **str**| Идентификатор чата (клиента) | 
 **send_message_request_body** | [**SendMessageRequestBody**](SendMessageRequestBody.md)| Отправление сообщения | [optional] 

### Return type

[**PostSendMessage200Response**](PostSendMessage200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook_unsubscribe**
> ChatRead200Response post_webhook_unsubscribe(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)

Отключение уведомлений (webhooks)

Отключение уведомлений


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.chat_read200_response import ChatRead200Response
from avito_messenger.models.webhook_subscribe_request_body import WebhookSubscribeRequestBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    webhook_subscribe_request_body = avito_messenger.WebhookSubscribeRequestBody() # WebhookSubscribeRequestBody | Url, на который необходимо перестать слать уведомления (optional)

    try:
        # Отключение уведомлений (webhooks)
        api_response = api_instance.post_webhook_unsubscribe(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)
        print("The response of MessengerApi->post_webhook_unsubscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->post_webhook_unsubscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **webhook_subscribe_request_body** | [**WebhookSubscribeRequestBody**](WebhookSubscribeRequestBody.md)| Url, на который необходимо перестать слать уведомления | [optional] 

### Return type

[**ChatRead200Response**](ChatRead200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook_v3**
> ChatRead200Response post_webhook_v3(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)

Включение уведомлений V3 (webhooks)

Включение webhook-уведомлений. 

Схему JSON приходящего в webhook сообщения можно увидеть в примерах ответов.

После регистрации url'а для получения веб-хуков, убедитесь, что он доступен, работает и возвращает статус 200 ОК соблюдая timeout 2s,
например, выполнив запрос:

curl --connect-timeout 2 <url-вашего-вебхука> -i -d '{}'


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
from avito_messenger.models.chat_read200_response import ChatRead200Response
from avito_messenger.models.webhook_subscribe_request_body import WebhookSubscribeRequestBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    webhook_subscribe_request_body = avito_messenger.WebhookSubscribeRequestBody() # WebhookSubscribeRequestBody | Url на который будут отправляться уведомления (optional)

    try:
        # Включение уведомлений V3 (webhooks)
        api_response = api_instance.post_webhook_v3(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)
        print("The response of MessengerApi->post_webhook_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->post_webhook_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **webhook_subscribe_request_body** | [**WebhookSubscribeRequestBody**](WebhookSubscribeRequestBody.md)| Url на который будут отправляться уведомления | [optional] 

### Return type

[**ChatRead200Response**](ChatRead200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**201** | JSON сообщения, который будет приходить в webhook |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_images**
> Dict[str, Dict[str, str]] upload_images(authorization, user_id, uploadfile)

Загрузка изображений

Метод используется для загрузки изображений в формате JPEG, HEIC, GIF, BMP или PNG.

Особенности работы с загрузкой изображений:
- Метод поддерживает только одиночные изображения; для загрузки нескольких картинок необходимо сделать несколько запросов;
- Максимальный размер файла — 24 МБ;
- Максимальное разрешение — 75 мегапиксилей;


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_messenger
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_messenger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_messenger.MessengerApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    user_id = 56 # int | Идентификатор пользователя (клиента)
    uploadfile = None # bytearray | 

    try:
        # Загрузка изображений
        api_response = api_instance.upload_images(authorization, user_id, uploadfile)
        print("The response of MessengerApi->upload_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessengerApi->upload_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **uploadfile** | **bytearray**|  | 

### Return type

**Dict[str, Dict[str, str]]**

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

