# avito_job.JobApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_get_by_ids**](JobApi.md#applications_get_by_ids) | **POST** /job/v1/applications/get_by_ids | Получение списка откликов 
[**applications_get_ids**](JobApi.md#applications_get_ids) | **GET** /job/v1/applications/get_ids | Получение идентификаторов откликов 
[**applications_set_is_viewed**](JobApi.md#applications_set_is_viewed) | **POST** /job/v1/applications/set_is_viewed | Изменение статуса отклика 
[**applications_webhook_delete**](JobApi.md#applications_webhook_delete) | **DELETE** /job/v1/applications/webhook | Отключение уведомлений по откликам (webhook) 
[**applications_webhook_get**](JobApi.md#applications_webhook_get) | **GET** /job/v1/applications/webhook | Получение информации о подписках (webhook) 
[**applications_webhook_put**](JobApi.md#applications_webhook_put) | **PUT** /job/v1/applications/webhook | Включение уведомлений по откликам (webhook) 
[**applications_webhooks_get**](JobApi.md#applications_webhooks_get) | **GET** /job/v1/applications/webhooks | Получение списка подписок (webhook) 
[**get_dict_by_id**](JobApi.md#get_dict_by_id) | **GET** /job/v2/vacancy/dict/{dictionary_id} | Получение доступных значений списка по ID словаря
[**get_dicts**](JobApi.md#get_dicts) | **GET** /job/v2/vacancy/dict | Получение списка доступных словарей
[**resume_get_contacts**](JobApi.md#resume_get_contacts) | **GET** /job/v1/resumes/{resume_id}/contacts/ | Доступ к контактным данным соискателя 
[**resume_get_item**](JobApi.md#resume_get_item) | **GET** /job/v2/resumes/{resume_id} | Просмотр данных резюме 
[**resumes_get**](JobApi.md#resumes_get) | **GET** /job/v1/resumes/ | Поиск резюме 
[**search_vacancy**](JobApi.md#search_vacancy) | **GET** /job/v2/vacancies | Поиск вакансий 
[**vacancies_get_by_ids**](JobApi.md#vacancies_get_by_ids) | **POST** /job/v2/vacancies/batch | Просмотр данных вакансий 
[**vacancy_archive**](JobApi.md#vacancy_archive) | **PUT** /job/v1/vacancies/archived/{vacancy_id} | Остановка публикации вакансии
[**vacancy_auto_renewal**](JobApi.md#vacancy_auto_renewal) | **PUT** /job/v2/vacancies/{vacancy_uuid}/auto_renewal | Автопродление вакансии v2
[**vacancy_create**](JobApi.md#vacancy_create) | **POST** /job/v1/vacancies | Публикация вакансии
[**vacancy_create_v2**](JobApi.md#vacancy_create_v2) | **POST** /job/v2/vacancies | Публикация вакансии v2
[**vacancy_get_item**](JobApi.md#vacancy_get_item) | **GET** /job/v2/vacancies/{vacancy_id} | Просмотр данных вакансии 
[**vacancy_get_statuses**](JobApi.md#vacancy_get_statuses) | **POST** /job/v2/vacancies/statuses | Получение статуса публикации вакансий V2
[**vacancy_prolongate**](JobApi.md#vacancy_prolongate) | **POST** /job/v1/vacancies/{vacancy_id}/prolongate | Реактивация вакансии
[**vacancy_update**](JobApi.md#vacancy_update) | **PUT** /job/v1/vacancies/{vacancy_id} | Редактирование вакансии
[**vacancy_update_v2**](JobApi.md#vacancy_update_v2) | **POST** /job/v2/vacancies/update/{vacancy_uuid} | Редактирование вакансии v2


# **applications_get_by_ids**
> GetApplicationsByIdsResult applications_get_by_ids(authorization, x_is_employee=x_is_employee, applications_get_by_ids_request=applications_get_by_ids_request)

Получение списка откликов 

Получение списка откликов по uuid, полученным по  [подписке на уведомления](https://developers.avito.ru/api-catalog/job/documentation#operation/applicationsWebhookPut) (webhook) и через метод  [получение идентификаторов откликов](https://developers.avito.ru/api-catalog/job/documentation#operation/applicationsGetIds) Максимальный лимит = 100


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.applications_get_by_ids_request import ApplicationsGetByIdsRequest
from avito_job.models.get_applications_by_ids_result import GetApplicationsByIdsResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    x_is_employee = True # bool | Сотрудник может получить информацию по откликам для вакансий которые он разместил в рамках компании (optional)
    applications_get_by_ids_request = avito_job.ApplicationsGetByIdsRequest() # ApplicationsGetByIdsRequest |  (optional)

    try:
        # Получение списка откликов 
        api_response = api_instance.applications_get_by_ids(authorization, x_is_employee=x_is_employee, applications_get_by_ids_request=applications_get_by_ids_request)
        print("The response of JobApi->applications_get_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_get_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **x_is_employee** | **bool**| Сотрудник может получить информацию по откликам для вакансий которые он разместил в рамках компании | [optional] 
 **applications_get_by_ids_request** | [**ApplicationsGetByIdsRequest**](ApplicationsGetByIdsRequest.md)|  | [optional] 

### Return type

[**GetApplicationsByIdsResult**](GetApplicationsByIdsResult.md)

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

# **applications_get_ids**
> GetApplicationsIdsResult applications_get_ids(authorization, updated_at_from, x_is_employee=x_is_employee, cursor=cursor, vacancy_ids=vacancy_ids, is_viewed=is_viewed)

Получение идентификаторов откликов 

Возвращает лимитированное количество идентификаторов откликов отсортированных по дате создания  начиная с самых свежих, для последующего получения по ним расширенной информации через метод [получение списка откликов](https://developers.avito.ru/api-catalog/job/documentation#operation/applicationsGetByIds).
Максимальный лимит = 100


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.get_applications_ids_result import GetApplicationsIdsResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    updated_at_from = '2006-01-02' # str | Возвращать отклики с датой обновления от указанной даты
    x_is_employee = True # bool | Сотрудник может получить список его откликов для вакансий которые он разместил в рамках компании (optional)
    cursor = '623850d1d3819d935dd02702' # str | <p>Идентификатор последнего отклика из предыдущего запроса</p>  <p>Пример использования параметра:</p>  <p>Получение первой страницы откликов, с датой обновления от 12 июня 2022 года:</p>  <p><code>GET /job/v1/applications/get_ids?updatedAtFrom=2022-06-12</code></p>  <p><code>[<br>   &nbsp{\"id\": \"62e3e7e542c3d9af3d85205e\",<...>},<br>   &nbsp<...>,<br>   &nbsp{\"id\": \"<strong>623850d1d3819d935dd02702</strong>\",<...>}<br> ]</code></p>  <p>Получение следующей страницы откликов:</p>  <p><code>GET /job/v1/applications/get_ids?updatedAtFrom=2022-06-12&cursor=<strong>623850d1d3819d935dd02702</strong></code></p>  (optional)
    vacancy_ids = '2241333,1424232' # str | Идентификаторы вакансий. Опциональный фильтр (можно указать одно или несколько значений через запятую) (optional)
    is_viewed = true # bool | Отклик просмотрен (optional)

    try:
        # Получение идентификаторов откликов 
        api_response = api_instance.applications_get_ids(authorization, updated_at_from, x_is_employee=x_is_employee, cursor=cursor, vacancy_ids=vacancy_ids, is_viewed=is_viewed)
        print("The response of JobApi->applications_get_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_get_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **updated_at_from** | **str**| Возвращать отклики с датой обновления от указанной даты | 
 **x_is_employee** | **bool**| Сотрудник может получить список его откликов для вакансий которые он разместил в рамках компании | [optional] 
 **cursor** | **str**| &lt;p&gt;Идентификатор последнего отклика из предыдущего запроса&lt;/p&gt;  &lt;p&gt;Пример использования параметра:&lt;/p&gt;  &lt;p&gt;Получение первой страницы откликов, с датой обновления от 12 июня 2022 года:&lt;/p&gt;  &lt;p&gt;&lt;code&gt;GET /job/v1/applications/get_ids?updatedAtFrom&#x3D;2022-06-12&lt;/code&gt;&lt;/p&gt;  &lt;p&gt;&lt;code&gt;[&lt;br&gt;   &amp;nbsp{\&quot;id\&quot;: \&quot;62e3e7e542c3d9af3d85205e\&quot;,&lt;...&gt;},&lt;br&gt;   &amp;nbsp&lt;...&gt;,&lt;br&gt;   &amp;nbsp{\&quot;id\&quot;: \&quot;&lt;strong&gt;623850d1d3819d935dd02702&lt;/strong&gt;\&quot;,&lt;...&gt;}&lt;br&gt; ]&lt;/code&gt;&lt;/p&gt;  &lt;p&gt;Получение следующей страницы откликов:&lt;/p&gt;  &lt;p&gt;&lt;code&gt;GET /job/v1/applications/get_ids?updatedAtFrom&#x3D;2022-06-12&amp;cursor&#x3D;&lt;strong&gt;623850d1d3819d935dd02702&lt;/strong&gt;&lt;/code&gt;&lt;/p&gt;  | [optional] 
 **vacancy_ids** | **str**| Идентификаторы вакансий. Опциональный фильтр (можно указать одно или несколько значений через запятую) | [optional] 
 **is_viewed** | **bool**| Отклик просмотрен | [optional] 

### Return type

[**GetApplicationsIdsResult**](GetApplicationsIdsResult.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Превышено допустимое количество запросов |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_set_is_viewed**
> SetApplicationsisVewedResult applications_set_is_viewed(authorization, x_is_employee=x_is_employee, applications_set_is_viewed_request=applications_set_is_viewed_request)

Изменение статуса отклика 

Возвращает информацию по откликам и статусу просмотренности отклика, при изменении статуса также статус изменится в Авито Pro.  Максимальный лимит = 100


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.applications_set_is_viewed_request import ApplicationsSetIsViewedRequest
from avito_job.models.set_applicationsis_vewed_result import SetApplicationsisVewedResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    x_is_employee = True # bool | Предоставляет возможность менять статус отклика от имени сотрудника (optional)
    applications_set_is_viewed_request = avito_job.ApplicationsSetIsViewedRequest() # ApplicationsSetIsViewedRequest |  (optional)

    try:
        # Изменение статуса отклика 
        api_response = api_instance.applications_set_is_viewed(authorization, x_is_employee=x_is_employee, applications_set_is_viewed_request=applications_set_is_viewed_request)
        print("The response of JobApi->applications_set_is_viewed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_set_is_viewed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **x_is_employee** | **bool**| Предоставляет возможность менять статус отклика от имени сотрудника | [optional] 
 **applications_set_is_viewed_request** | [**ApplicationsSetIsViewedRequest**](ApplicationsSetIsViewedRequest.md)|  | [optional] 

### Return type

[**SetApplicationsisVewedResult**](SetApplicationsisVewedResult.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_webhook_delete**
> ApplicationsWebhookDelete200Response applications_webhook_delete(authorization, url=url)

Отключение уведомлений по откликам (webhook) 

Отписка от уведомлений о создании и обновлении откликов на вакансии. Если авторизация происходит от имени приложения, отписка от вебхука будет для приложения


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.applications_webhook_delete200_response import ApplicationsWebhookDelete200Response
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    url = 'url_example' # str | URL, на который отправляются уведомления (optional)

    try:
        # Отключение уведомлений по откликам (webhook) 
        api_response = api_instance.applications_webhook_delete(authorization, url=url)
        print("The response of JobApi->applications_webhook_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_webhook_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **url** | **str**| URL, на который отправляются уведомления | [optional] 

### Return type

[**ApplicationsWebhookDelete200Response**](ApplicationsWebhookDelete200Response.md)

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

# **applications_webhook_get**
> WebhookSubscribeRequestBody applications_webhook_get(authorization)

Получение информации о подписках (webhook) 

Получение информации по существующим подпискам на создание и обновление откликов. Будет возвращен самый старый активный вебхук. Если авторизация происходит от имени приложения, будет возвращен вебхук приложения


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.webhook_subscribe_request_body import WebhookSubscribeRequestBody
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации

    try:
        # Получение информации о подписках (webhook) 
        api_response = api_instance.applications_webhook_get(authorization)
        print("The response of JobApi->applications_webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_webhook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 

### Return type

[**WebhookSubscribeRequestBody**](WebhookSubscribeRequestBody.md)

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

# **applications_webhook_put**
> WebhookSubscribeRequestBody applications_webhook_put(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)

Включение уведомлений по откликам (webhook) 

Подписка на уведомления о создании и обновлении откликов на вакансии. Если авторизация происходит от имени приложения, вебхук будет привязан к приложению. Исключение:
  - изменение сотрудника относящегося к объявлению (employee_id)

Важно: 
  Проверьте доступность url, при его недоступности из контура Авито webhook не будет создан/перезаписан.
  Если url недоступен больше месяца, то он удаляется и на него не придут новые уведомления.
  Список адресов с которых идут запросы по url IP 185.89.12.0/22, 146.158.48.0/21, 185.79.237.224/28 и 87.245.204.32/28.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.webhook_subscribe_request_body import WebhookSubscribeRequestBody
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    webhook_subscribe_request_body = avito_job.WebhookSubscribeRequestBody() # WebhookSubscribeRequestBody |  (optional)

    try:
        # Включение уведомлений по откликам (webhook) 
        api_response = api_instance.applications_webhook_put(authorization, webhook_subscribe_request_body=webhook_subscribe_request_body)
        print("The response of JobApi->applications_webhook_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_webhook_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **webhook_subscribe_request_body** | [**WebhookSubscribeRequestBody**](WebhookSubscribeRequestBody.md)|  | [optional] 

### Return type

[**WebhookSubscribeRequestBody**](WebhookSubscribeRequestBody.md)

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

# **applications_webhooks_get**
> WebhooksSubscriptionResultList applications_webhooks_get()

Получение списка подписок (webhook) 

Получение списка активных подписок на создание и обновление откликов в хронологическом порядке от самого старого к самому новому. Если авторизация происходит от имени приложения, будут возвращены вебхуки приложения


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.webhooks_subscription_result_list import WebhooksSubscriptionResultList
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)

    try:
        # Получение списка подписок (webhook) 
        api_response = api_instance.applications_webhooks_get()
        print("The response of JobApi->applications_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->applications_webhooks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksSubscriptionResultList**](WebhooksSubscriptionResultList.md)

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

# **get_dict_by_id**
> List[GetDictByID200ResponseInner] get_dict_by_id(authorization, dictionary_id, x_is_employee=x_is_employee)

Получение доступных значений списка по ID словаря

Возвращает доступные значения по имени справочника. Значения с признаком deprecated не могут использоваться при создании и обновлении вакансий.

### Example


```python
import avito_job
from avito_job.models.get_dict_by_id200_response_inner import GetDictByID200ResponseInner
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)


# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    dictionary_id = 'business_area' # str | Идентификатор словаря
    x_is_employee = True # bool | Включает привилегии компании для сотрудника (optional)

    try:
        # Получение доступных значений списка по ID словаря
        api_response = api_instance.get_dict_by_id(authorization, dictionary_id, x_is_employee=x_is_employee)
        print("The response of JobApi->get_dict_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_dict_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **dictionary_id** | **str**| Идентификатор словаря | 
 **x_is_employee** | **bool**| Включает привилегии компании для сотрудника | [optional] 

### Return type

[**List[GetDictByID200ResponseInner]**](GetDictByID200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Внутренняя ошибка метода API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dicts**
> List[GetDicts200ResponseInner] get_dicts(authorization, x_is_employee=x_is_employee)

Получение списка доступных словарей

Возвращает все доступные словари (Заменяет существующие списки)

### Example


```python
import avito_job
from avito_job.models.get_dicts200_response_inner import GetDicts200ResponseInner
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)


# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    x_is_employee = True # bool | Включает привилегии компании для сотрудника (optional)

    try:
        # Получение списка доступных словарей
        api_response = api_instance.get_dicts(authorization, x_is_employee=x_is_employee)
        print("The response of JobApi->get_dicts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_dicts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **x_is_employee** | **bool**| Включает привилегии компании для сотрудника | [optional] 

### Return type

[**List[GetDicts200ResponseInner]**](GetDicts200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ с массивом категорий |  -  |
**500** | Внутренняя ошибка метода API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_get_contacts**
> ResumeContacts resume_get_contacts(authorization, resume_id, x_is_employee=x_is_employee)

Доступ к контактным данным соискателя 

Для получения контактов пользователя необходимо приобрести пакет просмотров в [личном кабинете](https://www.avito.ru/paid-services/contact-packages/cvs). Если резюме было получено из отклика, контакты предоставляются без списания из пакета просмотров.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.resume_contacts import ResumeContacts
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    resume_id = 56 # int | Идентификатор резюме
    x_is_employee = True # bool | Сотрудник компании может получить информацию о резюме приобретенных компанией (optional)

    try:
        # Доступ к контактным данным соискателя 
        api_response = api_instance.resume_get_contacts(authorization, resume_id, x_is_employee=x_is_employee)
        print("The response of JobApi->resume_get_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->resume_get_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **resume_id** | **int**| Идентификатор резюме | 
 **x_is_employee** | **bool**| Сотрудник компании может получить информацию о резюме приобретенных компанией | [optional] 

### Return type

[**ResumeContacts**](ResumeContacts.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**402** | Требуется пополнение пакета просмотров резюме |  -  |
**403** | Требуется верификация работодателя |  -  |
**404** | Резюме не найдено |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_get_item**
> Resume20 resume_get_item(authorization, resume_id, x_is_employee=x_is_employee, fields=fields, params=params, photos=photos)

Просмотр данных резюме 

По умолчанию fields и params выводятся все. Если указана только часть полей - остальные поля будут отсутствовать в ответе.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.resume20 import Resume20
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    resume_id = 56 # int | Идентификатор резюме
    x_is_employee = True # bool | Включает привилегии компании для сотрудника, получает доступ к резюме от имени компании (optional)
    fields = 'title,description,salary' # str | Поля основного тела ответа (можно указать несколько значений через запятую). По умолчанию отображаются все поля. (optional)
    params = 'address,age' # str | Дополнительные поля, которые входят в params (можно указать несколько значений через запятую). По умолчанию отображаются все поля. (optional)
    photos = False # bool | Признак того, нужно ли отдавать картинки, по умолчанию false (optional) (default to False)

    try:
        # Просмотр данных резюме 
        api_response = api_instance.resume_get_item(authorization, resume_id, x_is_employee=x_is_employee, fields=fields, params=params, photos=photos)
        print("The response of JobApi->resume_get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->resume_get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **resume_id** | **int**| Идентификатор резюме | 
 **x_is_employee** | **bool**| Включает привилегии компании для сотрудника, получает доступ к резюме от имени компании | [optional] 
 **fields** | **str**| Поля основного тела ответа (можно указать несколько значений через запятую). По умолчанию отображаются все поля. | [optional] 
 **params** | **str**| Дополнительные поля, которые входят в params (можно указать несколько значений через запятую). По умолчанию отображаются все поля. | [optional] 
 **photos** | **bool**| Признак того, нужно ли отдавать картинки, по умолчанию false | [optional] [default to False]

### Return type

[**Resume20**](Resume20.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**404** | Резюме не найдено |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resumes_get**
> ResumesGet200Response resumes_get(authorization, x_is_employee=x_is_employee, per_page=per_page, page=page, cursor=cursor, fields=fields, query=query, location=location, specialization=specialization, schedule=schedule, business_trip_readiness=business_trip_readiness, relocation_readiness=relocation_readiness, gender=gender, age_min=age_min, age_max=age_max, education_level=education_level, experience_min=experience_min, experience_max=experience_max, salary_min=salary_min, salary_max=salary_max, updated_at=updated_at, updated_from=updated_from, updated_to=updated_to, nationality=nationality, driver_licence=driver_licence, driver_licence_category=driver_licence_category, driving_experience=driving_experience, own_transport=own_transport, medical_book=medical_book)

Поиск резюме 

### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.resumes_get200_response import ResumesGet200Response
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    x_is_employee = True # bool | Включает привилегии компании для сотрудника (optional)
    per_page = 25 # int | Количество записей на странице (положительное число от 1 до 100) (optional) (default to 25)
    page = 1 # int | Номер страницы (положительное число больше 0, произведение page на per_page не должно превышать 5000) (optional) (default to 1)
    cursor = 56 # int | Курсор поиска (если не указан, будет начат новый поиск и его курсор будет возвращен в ответе) (optional)
    fields = 'title,specialization,total_experience,salary' # str | Поля ответа (можно указать несколько значений через запятую) (optional)
    query = 'оператор call-центра' # str | Поисковая фраза (optional)
    location = 637640 # int | Идентификатор региона поиска (можно указать несколько значений через запятую) <br> Метод принимает идентификаторы сущностей Region и City из [справочника](http://autoload.avito.ru/format/Locations.xml).  (optional)
    specialization = 56 # int | Идентификатор сферы деятельности (можно указать несколько значений через запятую) <br> Возможные значения: - 10166 - IT, интернет, телеком - 10167 - Медицина, фармацевтика - 10168 - Продажи - 10169 - Страхование - 10170 - Транспорт, логистика - 10171 - Образование, наука - 10172 - Строительство - 10173 - Туризм, рестораны - 10174 - Фитнес, салоны красоты - 10175 - Без опыта, студенты - 10180 - Автомобильный бизнес - 10181 - Бухгалтерия, финансы - 10182 - Высший менеджмент - 10183 - Госслужба, НКО - 10184 - ЖКХ, эксплуатация - 10185 - Искусство, развлечения - 10186 - Консультирование - 10187 - Маркетинг, реклама, PR - 10188 - Охрана, безопасность - 10189 - Управление персоналом - 10190 - Юриспруденция - 10191 - Административная работа - 10192 - Банки, инвестиции - 10193 - Производство, сырьё, с/х - 16844 - Домашний персонал - 2804251 - Курьерская доставка - 2804250 - Такси  (optional)
    schedule = 'remote' # str | График работы (можно указать несколько значений через запятую) <br> Возможные значения: - partial-day - Неполный рабочий день - full-day - Полный рабочий день - fly-in-fly-out - Вахтовый метод - flexible - Гибкий график - shift - Сменный график - remote - Удаленная работа  (optional)
    business_trip_readiness = 'business_trip_readiness_example' # str | Готовность к командировкам (можно указать несколько значений через запятую) <br> Возможные значения: - ready - Готов - never - Не готов - sometimes - Иногда  (optional)
    relocation_readiness = 'relocation_readiness_example' # str | Готовность к переезду (можно указать несколько значений через запятую) <br> Возможные значения: - possible - Возможен - never - Невозможен  (optional)
    gender = 'gender_example' # str | Пол (можно указать несколько значений через запятую) <br> Возможные значения: - female - Женщина - male - Мужчина  (optional)
    age_min = 14 # int | Минимальный возраст (включительно, положительное число от 14 до 99) (optional) (default to 14)
    age_max = 99 # int | Максимальный возраст (включительно, положительное число от 18 до 99) (optional) (default to 99)
    education_level = 'unfinished-higher' # str | Уровень образования (можно указать несколько значений через запятую) <br> Возможные значения: - higher - Высшее - unfinished-higher - Неоконченное высшее - secondary - Среднее - special-secondary - Среднее специальное  (optional)
    experience_min = 0 # int | Минимальный стаж работы (включительно, положительное число от 0 до 50) (optional) (default to 0)
    experience_max = 50 # int | Максимальный стаж работы (включительно, положительное число от 0 до 50) (optional) (default to 50)
    salary_min = 0 # int | Минимальный размер заработной платы (включительно, положительное число) (optional) (default to 0)
    salary_max = 25000 # int | Максимальный размер заработной платы (включительно, положительное число) (optional)
    updated_at = '2013-10-20T19:20:30+01:00' # datetime | Дата последнего обновления (от updated_at до текущей даты) (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Дата последнего обновления (от updated_at) (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Дата последнего обновления (до updated_at) (optional)
    nationality = 56 # int | Идентификатор гражданства(можно указать несколько значений через запятую)</br> см. идентификаторы гражданства в [справочнике](https://www.avito.st/s/openapi/catalog_nationality.xml)</br> Распространенные значения: - 15973 - Россия - 15974 - Украина - 15975 - Белоруссия - 15979 - Азербайджан - 15985 - Армения - 16020 - Грузия - 15976 - Казахстан - 16046 - Киргизия - 16082 - Молдавия - 16129 - Таджикистан - 16140 - Узбекистан  (optional)
    driver_licence = 'driver_licence_example' # str | Водительское удостоверение <br> Возможные значения: - yes - Удостоверение есть - no - Удостоверения нет  (optional)
    driver_licence_category = 'driver_licence_category_example' # str | Категория водительского удостоверения (можно указать несколько значений через запятую) <br> Возможные значения:   - a   - b   - be   - c   - ce   - d   - de   - m   - tm   - tb  (optional)
    driving_experience = 'driving_experience_example' # str | Стаж вождения (можно указать несколько значений через запятую) <br> Возможные значения:   - less-than-three-years - Стаж вождения меньше трех лет   - more-than-three-years - Стаж вождения больше трех лет  (optional)
    own_transport = 'own_transport_example' # str | Свой транспорт (можно указать несколько значений через запятую) <br> Возможные значения:   - no - Нет   - car - Легковое авто   - cargo-car - Грузовое авто   - bike - Мотоцикл   - scooter - Мопед  (optional)
    medical_book = 'medical_book_example' # str | Медкнижка <br> Возможные значения:   - yes - Медкнижка есть   - no - Медкнижки нет  (optional)

    try:
        # Поиск резюме 
        api_response = api_instance.resumes_get(authorization, x_is_employee=x_is_employee, per_page=per_page, page=page, cursor=cursor, fields=fields, query=query, location=location, specialization=specialization, schedule=schedule, business_trip_readiness=business_trip_readiness, relocation_readiness=relocation_readiness, gender=gender, age_min=age_min, age_max=age_max, education_level=education_level, experience_min=experience_min, experience_max=experience_max, salary_min=salary_min, salary_max=salary_max, updated_at=updated_at, updated_from=updated_from, updated_to=updated_to, nationality=nationality, driver_licence=driver_licence, driver_licence_category=driver_licence_category, driving_experience=driving_experience, own_transport=own_transport, medical_book=medical_book)
        print("The response of JobApi->resumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->resumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **x_is_employee** | **bool**| Включает привилегии компании для сотрудника | [optional] 
 **per_page** | **int**| Количество записей на странице (положительное число от 1 до 100) | [optional] [default to 25]
 **page** | **int**| Номер страницы (положительное число больше 0, произведение page на per_page не должно превышать 5000) | [optional] [default to 1]
 **cursor** | **int**| Курсор поиска (если не указан, будет начат новый поиск и его курсор будет возвращен в ответе) | [optional] 
 **fields** | **str**| Поля ответа (можно указать несколько значений через запятую) | [optional] 
 **query** | **str**| Поисковая фраза | [optional] 
 **location** | **int**| Идентификатор региона поиска (можно указать несколько значений через запятую) &lt;br&gt; Метод принимает идентификаторы сущностей Region и City из [справочника](http://autoload.avito.ru/format/Locations.xml).  | [optional] 
 **specialization** | **int**| Идентификатор сферы деятельности (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - 10166 - IT, интернет, телеком - 10167 - Медицина, фармацевтика - 10168 - Продажи - 10169 - Страхование - 10170 - Транспорт, логистика - 10171 - Образование, наука - 10172 - Строительство - 10173 - Туризм, рестораны - 10174 - Фитнес, салоны красоты - 10175 - Без опыта, студенты - 10180 - Автомобильный бизнес - 10181 - Бухгалтерия, финансы - 10182 - Высший менеджмент - 10183 - Госслужба, НКО - 10184 - ЖКХ, эксплуатация - 10185 - Искусство, развлечения - 10186 - Консультирование - 10187 - Маркетинг, реклама, PR - 10188 - Охрана, безопасность - 10189 - Управление персоналом - 10190 - Юриспруденция - 10191 - Административная работа - 10192 - Банки, инвестиции - 10193 - Производство, сырьё, с/х - 16844 - Домашний персонал - 2804251 - Курьерская доставка - 2804250 - Такси  | [optional] 
 **schedule** | **str**| График работы (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - partial-day - Неполный рабочий день - full-day - Полный рабочий день - fly-in-fly-out - Вахтовый метод - flexible - Гибкий график - shift - Сменный график - remote - Удаленная работа  | [optional] 
 **business_trip_readiness** | **str**| Готовность к командировкам (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - ready - Готов - never - Не готов - sometimes - Иногда  | [optional] 
 **relocation_readiness** | **str**| Готовность к переезду (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - possible - Возможен - never - Невозможен  | [optional] 
 **gender** | **str**| Пол (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - female - Женщина - male - Мужчина  | [optional] 
 **age_min** | **int**| Минимальный возраст (включительно, положительное число от 14 до 99) | [optional] [default to 14]
 **age_max** | **int**| Максимальный возраст (включительно, положительное число от 18 до 99) | [optional] [default to 99]
 **education_level** | **str**| Уровень образования (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - higher - Высшее - unfinished-higher - Неоконченное высшее - secondary - Среднее - special-secondary - Среднее специальное  | [optional] 
 **experience_min** | **int**| Минимальный стаж работы (включительно, положительное число от 0 до 50) | [optional] [default to 0]
 **experience_max** | **int**| Максимальный стаж работы (включительно, положительное число от 0 до 50) | [optional] [default to 50]
 **salary_min** | **int**| Минимальный размер заработной платы (включительно, положительное число) | [optional] [default to 0]
 **salary_max** | **int**| Максимальный размер заработной платы (включительно, положительное число) | [optional] 
 **updated_at** | **datetime**| Дата последнего обновления (от updated_at до текущей даты) | [optional] 
 **updated_from** | **datetime**| Дата последнего обновления (от updated_at) | [optional] 
 **updated_to** | **datetime**| Дата последнего обновления (до updated_at) | [optional] 
 **nationality** | **int**| Идентификатор гражданства(можно указать несколько значений через запятую)&lt;/br&gt; см. идентификаторы гражданства в [справочнике](https://www.avito.st/s/openapi/catalog_nationality.xml)&lt;/br&gt; Распространенные значения: - 15973 - Россия - 15974 - Украина - 15975 - Белоруссия - 15979 - Азербайджан - 15985 - Армения - 16020 - Грузия - 15976 - Казахстан - 16046 - Киргизия - 16082 - Молдавия - 16129 - Таджикистан - 16140 - Узбекистан  | [optional] 
 **driver_licence** | **str**| Водительское удостоверение &lt;br&gt; Возможные значения: - yes - Удостоверение есть - no - Удостоверения нет  | [optional] 
 **driver_licence_category** | **str**| Категория водительского удостоверения (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения:   - a   - b   - be   - c   - ce   - d   - de   - m   - tm   - tb  | [optional] 
 **driving_experience** | **str**| Стаж вождения (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения:   - less-than-three-years - Стаж вождения меньше трех лет   - more-than-three-years - Стаж вождения больше трех лет  | [optional] 
 **own_transport** | **str**| Свой транспорт (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения:   - no - Нет   - car - Легковое авто   - cargo-car - Грузовое авто   - bike - Мотоцикл   - scooter - Мопед  | [optional] 
 **medical_book** | **str**| Медкнижка &lt;br&gt; Возможные значения:   - yes - Медкнижка есть   - no - Медкнижки нет  | [optional] 

### Return type

[**ResumesGet200Response**](ResumesGet200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_vacancy**
> SearchVacancy200Response search_vacancy(authorization, per_page=per_page, page=page, location=location, business_area=business_area)

Поиск вакансий 

### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.search_vacancy200_response import SearchVacancy200Response
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    per_page = 25 # int | Количество записей на странице (положительное число от 10 до 100) (optional) (default to 25)
    page = 1 # int | Номер страницы (положительное число больше 0, произведение page на per_page не должно превышать 5000) (optional) (default to 1)
    location = 637640 # int | Идентификатор региона поиска (можно указать несколько значений через запятую) <br> Метод принимает идентификаторы сущностей Region и City из [справочника](http://autoload.avito.ru/format/Locations.xml).  (optional)
    business_area = 3278315 # int | Идентификатор сферы деятельности  <br> Получить актуальный список доступных значений можно из справочника `business_area` через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). <br> Статичный [справочник](https://www.avito.st/s/openapi/catalog-business-area.xml) объявлен устаревшим и более не будет использоваться.  <br>  (optional)

    try:
        # Поиск вакансий 
        api_response = api_instance.search_vacancy(authorization, per_page=per_page, page=page, location=location, business_area=business_area)
        print("The response of JobApi->search_vacancy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_vacancy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **per_page** | **int**| Количество записей на странице (положительное число от 10 до 100) | [optional] [default to 25]
 **page** | **int**| Номер страницы (положительное число больше 0, произведение page на per_page не должно превышать 5000) | [optional] [default to 1]
 **location** | **int**| Идентификатор региона поиска (можно указать несколько значений через запятую) &lt;br&gt; Метод принимает идентификаторы сущностей Region и City из [справочника](http://autoload.avito.ru/format/Locations.xml).  | [optional] 
 **business_area** | **int**| Идентификатор сферы деятельности  &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;business_area&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-business-area.xml) объявлен устаревшим и более не будет использоваться.  &lt;br&gt;  | [optional] 

### Return type

[**SearchVacancy200Response**](SearchVacancy200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**204** | Отсутствуют данные по запросу |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Доступ запрещен |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancies_get_by_ids**
> List[Vacancy20] vacancies_get_by_ids(authorization, vacancies_get_by_ids_body, x_is_employee=x_is_employee)

Просмотр данных вакансий 

По умолчанию fields и params выводятся все. Если указана только часть полей - остальные поля будут отсутствовать в ответе.
Для просмотра данных необходимо быть владельцем вакансии.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancies_get_by_ids_body import VacanciesGetByIdsBody
from avito_job.models.vacancy20 import Vacancy20
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancies_get_by_ids_body = {"fields":["title"],"ids":[12342348,12342349],"params":["business_area","schedule"]} # VacanciesGetByIdsBody | 
    x_is_employee = True # bool | Сотрудник компании получает информацию по вакансиям, которую он опубликовал для компании (optional)

    try:
        # Просмотр данных вакансий 
        api_response = api_instance.vacancies_get_by_ids(authorization, vacancies_get_by_ids_body, x_is_employee=x_is_employee)
        print("The response of JobApi->vacancies_get_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancies_get_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancies_get_by_ids_body** | [**VacanciesGetByIdsBody**](VacanciesGetByIdsBody.md)|  | 
 **x_is_employee** | **bool**| Сотрудник компании получает информацию по вакансиям, которую он опубликовал для компании | [optional] 

### Return type

[**List[Vacancy20]**](Vacancy20.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Пользователь не владелец объявления |  -  |
**404** | Вакансия не найдена |  -  |
**429** | Превышено допустимое количество запросов |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_archive**
> vacancy_archive(authorization, vacancy_id, x_is_employee=x_is_employee, vacancy_archive=vacancy_archive)

Остановка публикации вакансии

Снимает с публикации объявление в категории Вакансии.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_archive import VacancyArchive
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_id = 56 # int | Идентификатор вакансии на сайте
    x_is_employee = True # bool | Сотрудник компании может остановить публикацию только для своих вакансий (optional)
    vacancy_archive = {"employee_id":12342348} # VacancyArchive |  (optional)

    try:
        # Остановка публикации вакансии
        api_instance.vacancy_archive(authorization, vacancy_id, x_is_employee=x_is_employee, vacancy_archive=vacancy_archive)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_id** | **int**| Идентификатор вакансии на сайте | 
 **x_is_employee** | **bool**| Сотрудник компании может остановить публикацию только для своих вакансий | [optional] 
 **vacancy_archive** | [**VacancyArchive**](VacancyArchive.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Успешный ответ |  -  |
**400** | Oшибка в поле запроса |  -  |
**401** | Требуется аутентификация |  -  |
**402** | Oшибка оплаты |  -  |
**403** | Остановка публикации вакансий недоступно |  -  |
**404** | Вакансия не найдена |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_auto_renewal**
> vacancy_auto_renewal(authorization, vacancy_uuid, vacancy_auto_renewal, x_is_employee=x_is_employee)

Автопродление вакансии v2

Включает или выключает автопродление вакансии. Если вакансия в архиве, то при включении автопродления вакансия будет автоматически поднята из архива.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_auto_renewal import VacancyAutoRenewal
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_uuid = 'vacancy_uuid_example' # str | UUID Идентификатор вакансии для V2 ручек (возвращается ручкой [Публикация вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyCreateV2) ) 
    vacancy_auto_renewal = {"auto_renewal":true} # VacancyAutoRenewal | 
    x_is_employee = True # bool | Включает привилегии компании для сотрудника, позволяет включать автопродление вакансий принадлежащих сотруднику опубликованных от имени компании (optional)

    try:
        # Автопродление вакансии v2
        api_instance.vacancy_auto_renewal(authorization, vacancy_uuid, vacancy_auto_renewal, x_is_employee=x_is_employee)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_auto_renewal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_uuid** | **str**| UUID Идентификатор вакансии для V2 ручек (возвращается ручкой [Публикация вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyCreateV2) )  | 
 **vacancy_auto_renewal** | [**VacancyAutoRenewal**](VacancyAutoRenewal.md)|  | 
 **x_is_employee** | **bool**| Включает привилегии компании для сотрудника, позволяет включать автопродление вакансий принадлежащих сотруднику опубликованных от имени компании | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**404** | вакансия не найдена |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_create**
> VacancyCreateResult vacancy_create(authorization, vacancy_create, x_is_employee=x_is_employee)

Публикация вакансии

Для публикации вакансии необходимо приобрести тариф в [личном кабинете](https://www.avito.ru/paid-services/listing-fees).


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_create import VacancyCreate
from avito_job.models.vacancy_create_result import VacancyCreateResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_create = {"address":"Москва","age":{"from":65,"to":16},"age_preferences":["olderThan45","withHealthProblems"],"allow_messages":true,"apply_processing":{"additional_questions":["experience","age","citizenship"],"apply_type":"with_assistant"},"billing_type":"package","business_area":7,"citizenship":["rus","blr"],"contacts":{"name":"менеджер","phone":{"city":"201","country":"+7","number":"1001158"}},"description":"описание","employment":"partial","experience":{"id":"moreThan1"},"is_remote":true,"is_side_job":false,"name":"объявление","payout_frequency":{"id":"dailyPay"},"profession":3201667,"schedule":{"id":"flyInFlyOut"}} # VacancyCreate | 
    x_is_employee = True # bool | Вакансия будет публиковаться от имени сотрудника компании, к которой он привязан. (optional)

    try:
        # Публикация вакансии
        api_response = api_instance.vacancy_create(authorization, vacancy_create, x_is_employee=x_is_employee)
        print("The response of JobApi->vacancy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_create** | [**VacancyCreate**](VacancyCreate.md)|  | 
 **x_is_employee** | **bool**| Вакансия будет публиковаться от имени сотрудника компании, к которой он привязан. | [optional] 

### Return type

[**VacancyCreateResult**](VacancyCreateResult.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Успешный ответ |  * Location - Заголовок будет содержать ссылку на добавленную вакансию. <br>  |
**400** | Oшибка в поле вакансии |  -  |
**401** | Требуется аутентификация |  -  |
**402** | Oшибка оплаты |  -  |
**403** | Создание вакансий недоступно |  -  |
**404** | Ресурс не найден |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_create_v2**
> VacancyV2CreateResult vacancy_create_v2(authorization, vacancy_v2_create, x_is_employee=x_is_employee)

Публикация вакансии v2

Для публикации вакансии необходимо приобрести тариф в [личном кабинете](https://www.avito.ru/paid-services/listing-fees).
Для проверки статуса публикации используйте полученный идентификатор в [методе получения статуса](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyGetStatuses).


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_v2_create import VacancyV2Create
from avito_job.models.vacancy_v2_create_result import VacancyV2CreateResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_v2_create = {"age":{"from":65,"to":16},"age_preferences":["olderThan45","withHealthProblems"],"apply_processing":{"additional_questions":["experience","age","citizenship"],"apply_type":"with_assistant"},"billing_type":"packageOrSingle","business_area":7,"citizenship":["rus","blr"],"contacts":{"allow_messages":true,"name":"менеджер","phone":"+72011001158"},"delivery_method":["car","bike"],"description":"описание","driving_experience":"moreThan10","driving_license_category":["B","C","M"],"employment":"partial","experience":"moreThan1","is_company_car":true,"is_remote":false,"is_side_job":true,"location":{"address":{"house":"д.1","locality":"Москва","street":"ул. Лесная"},"coordinates":{"latitude":55.778644,"longitude":37.587901}},"payout_frequency":"dailyPay","profession":3201667,"programs":["chastyeVyplaty"],"salary":{"from":1000,"to":2000},"schedule":"flyInFlyOut","title":"объявление"} # VacancyV2Create | 
    x_is_employee = True # bool | Вакансия будет публиковаться от имени сотрудника компании, к которой он привязан. (optional)

    try:
        # Публикация вакансии v2
        api_response = api_instance.vacancy_create_v2(authorization, vacancy_v2_create, x_is_employee=x_is_employee)
        print("The response of JobApi->vacancy_create_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_create_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_v2_create** | [**VacancyV2Create**](VacancyV2Create.md)|  | 
 **x_is_employee** | **bool**| Вакансия будет публиковаться от имени сотрудника компании, к которой он привязан. | [optional] 

### Return type

[**VacancyV2CreateResult**](VacancyV2CreateResult.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Успешный ответ |  -  |
**400** | Oшибка в поле вакансии |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Создание вакансий недоступно |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_get_item**
> Vacancy20 vacancy_get_item(authorization, vacancy_id, x_is_employee=x_is_employee, fields=fields, params=params)

Просмотр данных вакансии 

По умолчанию fields и params выводятся все. Если указана только часть полей - остальные поля будут отсутствовать в ответе.
Для просмотра данных необходимо быть владельцем вакансии.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy20 import Vacancy20
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_id = 56 # int | Идентификатор вакансии
    x_is_employee = True # bool | Сотрудник компании получает информацию по вакансии, которую он опубликовал для компании (optional)
    fields = 'title,description,salary' # str | Поля основного тела ответа (можно указать несколько значений через запятую). По умолчанию отображаются все поля. (optional)
    params = 'address,schedule' # str | Дополнительные поля, которые входят в params (можно указать несколько значений через запятую). По умолчанию отображаются все поля. deprecated значения manufacturing_type, industry_type, programs, warehouse_functionality (optional)

    try:
        # Просмотр данных вакансии 
        api_response = api_instance.vacancy_get_item(authorization, vacancy_id, x_is_employee=x_is_employee, fields=fields, params=params)
        print("The response of JobApi->vacancy_get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_id** | **int**| Идентификатор вакансии | 
 **x_is_employee** | **bool**| Сотрудник компании получает информацию по вакансии, которую он опубликовал для компании | [optional] 
 **fields** | **str**| Поля основного тела ответа (можно указать несколько значений через запятую). По умолчанию отображаются все поля. | [optional] 
 **params** | **str**| Дополнительные поля, которые входят в params (можно указать несколько значений через запятую). По умолчанию отображаются все поля. deprecated значения manufacturing_type, industry_type, programs, warehouse_functionality | [optional] 

### Return type

[**Vacancy20**](Vacancy20.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Пользователь не владелец объявления |  -  |
**404** | Вакансия не найдена |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_get_statuses**
> List[VacancyStatusesResultInner] vacancy_get_statuses(authorization, vacancy_statuses_body, x_is_employee=x_is_employee)

Получение статуса публикации вакансий V2

Получение списка статусов процесса публикации и модерации вакансий.
В запросе используйте идентификатор, полученный [методе
публикации вакансии v2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyCreateV2)


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_statuses_body import VacancyStatusesBody
from avito_job.models.vacancy_statuses_result_inner import VacancyStatusesResultInner
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_statuses_body = avito_job.VacancyStatusesBody() # VacancyStatusesBody | 
    x_is_employee = True # bool | Сотрудник компании получает информацию о статусе публикации вакансии, которую он опубликовал для компании (optional)

    try:
        # Получение статуса публикации вакансий V2
        api_response = api_instance.vacancy_get_statuses(authorization, vacancy_statuses_body, x_is_employee=x_is_employee)
        print("The response of JobApi->vacancy_get_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_get_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_statuses_body** | [**VacancyStatusesBody**](VacancyStatusesBody.md)|  | 
 **x_is_employee** | **bool**| Сотрудник компании получает информацию о статусе публикации вакансии, которую он опубликовал для компании | [optional] 

### Return type

[**List[VacancyStatusesResultInner]**](VacancyStatusesResultInner.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**400** | Oшибка в формате запроса |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Пользователь не авторизован для этой операции |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_prolongate**
> vacancy_prolongate(authorization, vacancy_id, vacancy_prolongate, x_is_employee=x_is_employee)

Реактивация вакансии

Реактивирует объявление в категории Вакансии. Необходимо приобрести тариф в [личном кабинете](https://www.avito.ru/paid-services/listing-fees).


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_prolongate import VacancyProlongate
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_id = 56 # int | Идентификатор вакансии на сайте
    vacancy_prolongate = {"billing_type":"package"} # VacancyProlongate | 
    x_is_employee = True # bool | Сотрудник компании может реактивировать только свою вакансию (optional)

    try:
        # Реактивация вакансии
        api_instance.vacancy_prolongate(authorization, vacancy_id, vacancy_prolongate, x_is_employee=x_is_employee)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_prolongate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_id** | **int**| Идентификатор вакансии на сайте | 
 **vacancy_prolongate** | [**VacancyProlongate**](VacancyProlongate.md)|  | 
 **x_is_employee** | **bool**| Сотрудник компании может реактивировать только свою вакансию | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Успешный ответ |  -  |
**400** | Oшибка в поле вакансии |  -  |
**401** | Требуется аутентификация |  -  |
**402** | Oшибка оплаты |  -  |
**403** | Активация вакансий недоступна |  -  |
**404** | Вакансия не найдена |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_update**
> vacancy_update(authorization, vacancy_id, vacancy_update, x_is_employee=x_is_employee)

Редактирование вакансии

Редактирует объявление в категории Вакансии. Необходимо приобрести тариф в [личном кабинете](https://www.avito.ru/paid-services/listing-fees).


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_update import VacancyUpdate
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_id = 56 # int | Идентификатор вакансии на сайте
    vacancy_update = {"address":"Москва","age_preferences":["olderThan45","withHealthProblems"],"allow_messages":true,"apply_processing":{"apply_type":"only_with_resume"},"billing_type":"package","contacts":{"name":"менеджер","phone":{"city":"201","country":"+7","number":"1001158"}},"description":"описание","experience":{"id":"moreThan1"},"is_remote":false,"is_side_job":true,"name":"объявление","payout_frequency":{"id":"dailyPay"},"profession":3201667} # VacancyUpdate | 
    x_is_employee = True # bool | Сотрудник компании может редактировать только свои вакансии. (optional)

    try:
        # Редактирование вакансии
        api_instance.vacancy_update(authorization, vacancy_id, vacancy_update, x_is_employee=x_is_employee)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_id** | **int**| Идентификатор вакансии на сайте | 
 **vacancy_update** | [**VacancyUpdate**](VacancyUpdate.md)|  | 
 **x_is_employee** | **bool**| Сотрудник компании может редактировать только свои вакансии. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Успешный ответ |  -  |
**400** | Oшибка в поле вакансии |  -  |
**401** | Требуется аутентификация |  -  |
**402** | Oшибка оплаты |  -  |
**403** | Редактирование вакансий недоступно |  -  |
**404** | Редактируемая вакансия не найдена |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vacancy_update_v2**
> VacancyV2CreateResult vacancy_update_v2(authorization, vacancy_uuid, vacancy_v2_create, x_is_employee=x_is_employee)

Редактирование вакансии v2

Редактирует объявление в категории Вакансии. Необходимо приобрести тариф в [личном кабинете](https://www.avito.ru/paid-services/listing-fees).


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_job
from avito_job.models.vacancy_v2_create import VacancyV2Create
from avito_job.models.vacancy_v2_create_result import VacancyV2CreateResult
from avito_job.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.avito.ru
# See configuration.py for a list of all supported configuration parameters.
configuration = avito_job.Configuration(
    host = "https://api.avito.ru"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with avito_job.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avito_job.JobApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vacancy_uuid = 'vacancy_uuid_example' # str | UUID Идентификатор вакансии для V2 ручек (возвращается ручкой [Публикация вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyCreateV2) ) 
    vacancy_v2_create = {"age_preferences":["olderThan45","withHealthProblems"],"apply_processing":{"apply_type":"only_with_resume"},"billing_type":"packageOrSingle","business_area":7,"contacts":{"allow_messages":true,"name":"менеджер","phone":72011001158},"delivery_method":["car","bike"],"description":"описание <strong>c тегами</strong>","driving_experience":"moreThan10","driving_license_category":["B","C","M"],"employment":"partial","experience":"moreThan1","is_company_car":true,"is_remote":true,"is_side_job":true,"location":{"address":{"house":"д.1","locality":"Москва","street":"ул. Лесная"},"coordinates":{"latitude":55.778644,"longitude":37.587901}},"payout_frequency":"dailyPay","profession":3201667,"programs":["chastyeVyplaty"],"salary":{"from":1000,"to":2000},"schedule":"flyInFlyOut","title":"объявление"} # VacancyV2Create | 
    x_is_employee = True # bool | Сотрудник компании может редактировать только свои вакансии. (optional)

    try:
        # Редактирование вакансии v2
        api_response = api_instance.vacancy_update_v2(authorization, vacancy_uuid, vacancy_v2_create, x_is_employee=x_is_employee)
        print("The response of JobApi->vacancy_update_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->vacancy_update_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **vacancy_uuid** | **str**| UUID Идентификатор вакансии для V2 ручек (возвращается ручкой [Публикация вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyCreateV2) )  | 
 **vacancy_v2_create** | [**VacancyV2Create**](VacancyV2Create.md)|  | 
 **x_is_employee** | **bool**| Сотрудник компании может редактировать только свои вакансии. | [optional] 

### Return type

[**VacancyV2CreateResult**](VacancyV2CreateResult.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Успешный ответ |  -  |
**400** | Oшибка в поле вакансии |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Создание вакансий недоступно |  -  |
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

