# avito_ads.DefaultApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_price**](DefaultApi.md#update_price) | **POST** /core/v1/items/{item_id}/update_price | Обновление цены объявления 


# **update_price**
> UpdatePriceResponse update_price(item_id, update_price_request=update_price_request)

Обновление цены объявления 

Обновляет цену товара по id. 
Максимальное количество запросов в минуту - 150.
**Внимание! Доступно для категорий Товары, Запчасти, Авто, Недвижимость (кроме краткосрочной)**


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.update_price_request import UpdatePriceRequest
from avito_ads.models.update_price_response import UpdatePriceResponse
from avito_ads.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_ads.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_ads.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_ads.DefaultApi(api_client)
    item_id = 56 # int | Идентификатор объявления на сайте
    update_price_request = avito_ads.UpdatePriceRequest() # UpdatePriceRequest | Набор параметров в теле запроса. (optional)

    try:
        # Обновление цены объявления 
        api_response = api_instance.update_price(item_id, update_price_request=update_price_request)
        print("The response of DefaultApi->update_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Идентификатор объявления на сайте | 
 **update_price_request** | [**UpdatePriceRequest**](UpdatePriceRequest.md)| Набор параметров в теле запроса. | [optional] 

### Return type

[**UpdatePriceResponse**](UpdatePriceResponse.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**404** | Неверный user_id в запросе |  -  |
**429** | Превышено количество запросов |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

