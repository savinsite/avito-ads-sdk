# avito_autorization.ApplicationAccessApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token_authorization_code**](ApplicationAccessApi.md#get_access_token_authorization_code) | **POST** /token‎ | Получение access token
[**refresh_access_token_authorization_code**](ApplicationAccessApi.md#refresh_access_token_authorization_code) | **POST** /token‎‎ | Обновление access token


# **get_access_token_authorization_code**
> GetAccessTokenAuthorizationCode200Response get_access_token_authorization_code(client_id, client_secret, code, grant_type)

Получение access token

Получения временного ключа для авторизации запроса от лица пользователя

### Example


```python
import avito_autorization
from avito_autorization.models.get_access_token_authorization_code200_response import GetAccessTokenAuthorizationCode200Response
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
    api_instance = avito_autorization.ApplicationAccessApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    code = 'code_example' # str | 
    grant_type = 'authorization_code' # str |  (default to 'authorization_code')

    try:
        # Получение access token
        api_response = api_instance.get_access_token_authorization_code(client_id, client_secret, code, grant_type)
        print("The response of ApplicationAccessApi->get_access_token_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAccessApi->get_access_token_authorization_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **code** | **str**|  | 
 **grant_type** | **str**|  | [default to &#39;authorization_code&#39;]

### Return type

[**GetAccessTokenAuthorizationCode200Response**](GetAccessTokenAuthorizationCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_access_token_authorization_code**
> RefreshAccessTokenAuthorizationCode200Response refresh_access_token_authorization_code(client_id, client_secret, grant_type, refresh_token)

Обновление access token

Обновление временного ключа для авторизации запроса от лица пользователя

### Example


```python
import avito_autorization
from avito_autorization.models.refresh_access_token_authorization_code200_response import RefreshAccessTokenAuthorizationCode200Response
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
    api_instance = avito_autorization.ApplicationAccessApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    grant_type = 'refresh_token' # str | Тип OAuth flow. Строка refresh_token (default to 'refresh_token')
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Обновление access token
        api_response = api_instance.refresh_access_token_authorization_code(client_id, client_secret, grant_type, refresh_token)
        print("The response of ApplicationAccessApi->refresh_access_token_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAccessApi->refresh_access_token_authorization_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **grant_type** | **str**| Тип OAuth flow. Строка refresh_token | [default to &#39;refresh_token&#39;]
 **refresh_token** | **str**|  | 

### Return type

[**RefreshAccessTokenAuthorizationCode200Response**](RefreshAccessTokenAuthorizationCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

