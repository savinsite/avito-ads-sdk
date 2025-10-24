# avito_autorization.AccessApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AccessApi.md#get_access_token) | **POST** /token | Получение access token


# **get_access_token**
> GetAccessToken200Response get_access_token(client_id, client_secret, grant_type)

Получение access token

Получения временного ключа для авторизации

### Example


```python
import avito_autorization
from avito_autorization.models.get_access_token200_response import GetAccessToken200Response
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
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    grant_type = 'client_credentials' # str |  (default to 'client_credentials')

    try:
        # Получение access token
        api_response = api_instance.get_access_token(client_id, client_secret, grant_type)
        print("The response of AccessApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessApi->get_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **grant_type** | **str**|  | [default to &#39;client_credentials&#39;]

### Return type

[**GetAccessToken200Response**](GetAccessToken200Response.md)

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

