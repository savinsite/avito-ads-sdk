# avito_ads.ItemApi

All URIs are relative to *https://api.avito.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_vas**](ItemApi.md#apply_vas) | **PUT** /core/v2/items/{itemId}/vas/ | Применение услуг продвижения
[**get_item_info**](ItemApi.md#get_item_info) | **GET** /core/v1/accounts/{user_id}/items/{item_id}/ | Получение информации по объявлению
[**get_items_info**](ItemApi.md#get_items_info) | **GET** /core/v1/items | Получение информации по объявлениям
[**item_analytics**](ItemApi.md#item_analytics) | **POST** /stats/v2/accounts/{user_id}/items | Получение статистических показателей по профилю
[**item_stats_shallow**](ItemApi.md#item_stats_shallow) | **POST** /stats/v1/accounts/{user_id}/items | Получение статистики по списку объявлений
[**post_calls_stats**](ItemApi.md#post_calls_stats) | **POST** /core/v1/accounts/{user_id}/calls/stats/ | Получение статистики по звонкам
[**put_item_vas**](ItemApi.md#put_item_vas) | **PUT** /core/v1/accounts/{user_id}/items/{item_id}/vas | Применение дополнительных услуг
[**put_item_vas_package_v2**](ItemApi.md#put_item_vas_package_v2) | **PUT** /core/v2/accounts/{user_id}/items/{item_id}/vas_packages | Применение пакета дополнительных услуг
[**vas_prices**](ItemApi.md#vas_prices) | **POST** /core/v1/accounts/{userId}/vas/prices | Получение информации о стоимости услуг продвижения и доступных значках


# **apply_vas**
> Dict[str, ApplyVasResp] apply_vas(item_id, authorization, apply_vas_request=apply_vas_request)

Применение услуг продвижения

С помощью этого метода вы можете применить к опубликованному объявлению одну или несколько услуг продвижения (например, «XL-объявление», «Выделение цветом» и «До 10 раз больше просмотров на 7 дней»). В рамках одного запроса услуга может быть применена только один раз. 

Если для вашего объявления доступны значки (такие как «Без ДТП», «Срочно», «1 владелец»), при подключении услуги «XL-объявление» вы можете передать их список (не более трёх значков). В этом случае добавьте соответствующую услугу на 1, 2 или 3 значка.

[Подробнее об услугах продвижения](https://support.avito.ru/partitions/131)

Чтобы получить список доступных услуг и значков,  используйте метод `/core/v1/accounts/{userId}/vas/prices`.

Если заказ сформирован успешно, в ответ вы получите уникальные идентификаторы операций покупки для каждой из применяемых услуг. Позже эти идентификаторы можно будет использовать, чтобы узнать статус выполнения заказа.

В случае некорректного запроса метод вернет код ответа 400 и структуру, содержащую поле `code`. Возможные коды ошибок:
  - **1001** – один или несколько заголовков неправильно передаются;
  - **1002** – ошибка в URL;
  - **1003** – неверный идентификатор объявления из запроса;
  - **1004** – JSON из тела запроса не соответствует схеме или список идентификаторов услуг пустой;
  - **1005** – объявление, к которому вы хотите применить услуги, неактивно;
  - **1006** – неправильное количество выбранных значков для объявления.
Убедитесь, что в списке идентификаторов услуг есть услуга для покупки значков и она совпадает с количеством выбранных значков.
      - stickerpack_x1 – 1 значок
      - stickerpack_x2 – 2 значка
      - stickerpack_x3 – 3 значка
  - **1007** – некоторые из выбранных услуг не могут быть применены;
  - **1008** – в объявлении появились обязательные поля, которые нужно заполнить.
Отредактируйте объявление и попробуйте применить услугу снова.
  - **1009** – в кошельке не хватает средств для покупки услуг;
  - **1010** – вы пытались купить больше одной услуги увеличения просмотров;
  - **1011** – вы пытались купить значки, недоступные для выбранного объявления.

В случае внутренней ошибки на стороне Авито вернётся код ответа 500 и структура, содержащая поле `code`. Возможные коды ошибок:
  - **1000** – ошибка на стороне Авито, попробуйте позже или [напишите в поддержку](https://support.avito.ru/request/659?eventData[contextId]=117);

**Важно:** если ответ пришёл без кода ошибки или его значения нет в списке выше — возможно, услуга всё-таки была куплена. Подождите несколько минут: услуга продвижения появится в списке применённых, а если нет — попробуйте оформить её снова.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.apply_vas_request import ApplyVasRequest
from avito_ads.models.apply_vas_resp import ApplyVasResp
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
    api_instance = avito_ads.ItemApi(api_client)
    item_id = 56 # int | Идентификатор объявления на сайте
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    apply_vas_request = avito_ads.ApplyVasRequest() # ApplyVasRequest |  (optional)

    try:
        # Применение услуг продвижения
        api_response = api_instance.apply_vas(item_id, authorization, apply_vas_request=apply_vas_request)
        print("The response of ItemApi->apply_vas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->apply_vas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Идентификатор объявления на сайте | 
 **authorization** | **str**| Токен для авторизации | 
 **apply_vas_request** | [**ApplyVasRequest**](ApplyVasRequest.md)|  | [optional] 

### Return type

[**Dict[str, ApplyVasResp]**](ApplyVasResp.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**500** | Ответ с ошибкой |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_info**
> ItemInfoAvito get_item_info(user_id, item_id, authorization)

Получение информации по объявлению

Возвращает данные об объявлении - его статус, список примененных услуг Максимальное количество запросов в минуту - 500
**Внимание:** для получения статистики объявления должен использоваться метод:
[получение статистики по списку объявлений](#operation/itemStatsShallow)


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.item_info_avito import ItemInfoAvito
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Номер пользователя в Личном кабинете Авито
    item_id = 56 # int | Идентификатор объявления на сайте
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации

    try:
        # Получение информации по объявлению
        api_response = api_instance.get_item_info(user_id, item_id, authorization)
        print("The response of ItemApi->get_item_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->get_item_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Номер пользователя в Личном кабинете Авито | 
 **item_id** | **int**| Идентификатор объявления на сайте | 
 **authorization** | **str**| Токен для авторизации | 

### Return type

[**ItemInfoAvito**](ItemInfoAvito.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**429** | Превышено допустимое количество запросов |  -  |
**0** | Информация об ошибке |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_info**
> ItemsInfoWithCategoryAvito get_items_info(authorization, per_page=per_page, page=page, status=status, updated_at_from=updated_at_from, category=category)

Получение информации по объявлениям

Возвращает список объявлений авторизованного пользователя - статус, категорию и ссылку на сайте.
**Внимание! В настоящий момент этот метод не работает с объявлениями [сотрудников](https://pro.avito.ru/employees).** Он позволяет получить объявления только для пользователя, который указан владельцем этого объявления. В случае сотрудника это будет главный аккаунт компании, для авторизованного сотрудника вернётся пустой список объявлений.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.items_info_with_category_avito import ItemsInfoWithCategoryAvito
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
    api_instance = avito_ads.ItemApi(api_client)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    per_page = 25 # int | Количество записей на странице (целое число больше 0 и меньше 100) (optional) (default to 25)
    page = 1 # int | Номер страницы (целое число больше 0) (optional) (default to 1)
    status = active # str | Статус объявления на сайте (можно указать несколько значений через запятую) (optional) (default to active)
    updated_at_from = '2023-12-18' # str | Фильтр больше либо равно по дате обновления/редактирования объявления в формате YYYY-MM-DD (optional)
    category = 111 # int | Идентификатор категории объявления</br> см. возможные варианты категорий в [ справочнике ](https://www.avito.st/s/openapi/catalog-categories.xml)  (optional)

    try:
        # Получение информации по объявлениям
        api_response = api_instance.get_items_info(authorization, per_page=per_page, page=page, status=status, updated_at_from=updated_at_from, category=category)
        print("The response of ItemApi->get_items_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->get_items_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Токен для авторизации | 
 **per_page** | **int**| Количество записей на странице (целое число больше 0 и меньше 100) | [optional] [default to 25]
 **page** | **int**| Номер страницы (целое число больше 0) | [optional] [default to 1]
 **status** | **str**| Статус объявления на сайте (можно указать несколько значений через запятую) | [optional] [default to active]
 **updated_at_from** | **str**| Фильтр больше либо равно по дате обновления/редактирования объявления в формате YYYY-MM-DD | [optional] 
 **category** | **int**| Идентификатор категории объявления&lt;/br&gt; см. возможные варианты категорий в [ справочнике ](https://www.avito.st/s/openapi/catalog-categories.xml)  | [optional] 

### Return type

[**ItemsInfoWithCategoryAvito**](ItemsInfoWithCategoryAvito.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**0** | Информация об ошибке |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_analytics**
> AnalyticsResponse item_analytics(user_id, authorization, content_type, analytics_request)

Получение статистических показателей по профилю

Получение статистических показателей по профилю.
### Группировки показателей
Используйте группировки, чтобы получать конкретную статистику.  Например, можете запросить только общие значения показателей, а если нужны подробности, — значения показателей по каждому объявлению или за определённый период. Доступные группировки:

  - **totals** — по общему значению показателя за определённый период, без детализации;
  - **item** — по объявлениям;
  - **day** — по дням;
  - **week** — по неделям;
  - **month** — по месяцам.


### Доступные показатели по объявлениям
#### Основные

  - **views** - Просмотры. Сколько раз объявление показывалось в результатах поиска и рекомендациях. Несколько показов за сутки одному пользователю считаются как один.
  - **contacts** - Контакты. Количество пользователей, которые посмотрели ваш номер, написали в чат или откликнулись на скидку после рассылки. Несколько контактов за сутки от одного пользователя считаются как один.
    - **contactsShowPhone** - Посмотрели телефон. Количество пользователей, которые посмотрели ваш телефон или нажали «Позвонить». Несколько таких действий за сутки от одного пользователя считаются как один.
    - **contactsMessenger** - Написали в чат. Количество пользователей, которые написали вам. Несколько чатов за сутки от одного пользователя считаются как один.
    - **contactsShowPhoneAndMessenger** - Посмотрели телефон и написали в чат. Количество пользователей, которые и посмотрели ваш телефон, и написали в чат. Несколько таких действий за сутки от одного пользователя считаются как один.
    - **contactsSbcDiscount** - Откликнулись на скидку в чате. Количество пользователей, которые приняли ваше спецпредложение после рассылки.
  - **viewsToContactsConversion** - Конверсия из просмотров в контакты. Процент пользователей, которые после перехода в объявление посмотрели ваш телефон или написали в чат.
  - **favorites** - Добавили в избранное. Сколько раз объявление добавили в избранное.
  - **averageViewCost** - Средняя цена просмотра. Расходы на размещение и продвижение объявлений делятся на число просмотров.
  - **averageContactCost** - Средняя цена контакта. Расходы на размещение и продвижение объявлений делятся на число контактов.
  - **impressions** - Показы. Сколько раз объявление показывалось в результатах поиска и рекомендациях. Несколько показов за сутки одному пользователю считаются как один.
  - **impressionsToViewsConversion** - Конверсия из показов в просмотры. Процент пользователей, которые перешли в объявление после того, как оно показалось в результатах поиска и рекомендациях.


#### Целевые действия

  - **clickPackages**	- Целевые просмотры. Просмотры, которые оплачены из тарифа и считаются целевыми [по правилам Авито](https://www.avito.ru/legal/rules/paid_services/cost-per-action/#clicks).
  - **jobContacts** - Отклики на вакансии. Отклики, которые оплачены из тарифа и считаются целевыми [по правилам Авито](https://www.avito.ru/legal/rules/paid_services/cost-per-action/#clicks).


#### Заказы с Авито Доставкой

  - **viewsToOrderedItemsConversion** - Конверсия из просмотров в заказанные товары. Процент пользователей, которые после перехода в объявление заказали товар.
  - **orderedItems** - Заказано товаров. Количество товаров, которые заказали с Авито Доставкой.
  - **orderedItemsPrice** - Стоимость заказанных товаров в копейках. Общая стоимость заказов. Это сумма, которую вы получите на руки, если клиенты примут заказы.
  - **deliveredItems** - Доставлено товаров. Количество товаров, которые заказали с Авито Доставкой и уже приняли.
  - **deliveredItemsPrice** - Стоимость доставленных товаров в копейках. Общая стоимость заказов, которые покупатели приняли. Это сумма, которую вы получаете на руки.


#### Посуточная аренда

  - **bookingPlacedCount** - Получено заявок. Общее количество заявок на бронирование
  - **bookingPlacedPrice** - Стоимость полученных заявок в копейках. Общая стоимость бронирований. Это сумма, которую вы получите на руки, если гости заселятся.
  - **bookingApprovedCount** - Подтверждено заявок. Количество заявок на бронирование, которые вы подтвердили.
  - **bookingApprovedPrice** - Стоимость подтвержденных заявок в копейках. Общая стоимость бронирований, которые вы подтвердили. Это сумма, которую вы получите на руки, если гости заселятся.
  - **bookingAcceptedCount** - Заявки с заселением. Количество бронирований, по которым заселились гости. Заселение засчитывается в 15:00 по Москве на следующий день после заезда.
  - **bookingAcceptedPrice** - Стоимость заявок с заселением в копейках. Общая стоимость бронирований, по которым заселились гости. Это сумма, которую вы получаете на руки.


#### Расходы

  - **allSpending** - Все расходы в копейках. Сколько всего денег и бонусов вы потратили на объявления.
    - **spending** - Расходы на объявления в копейках. Сколько денег вы потратили на размещение, продвижение, целевые действия и комиссию.
      - **presenceSpending** - Расходы на размещение и целевые действия в копейках. Сколько денег вы потратили на размещения и целевые действия — просмотры, чаты, звонки и отклики.
      - **promoSpending** - Расходы на продвижение в копейках. Сколько денег вы потратили на продвижение и на услуги, которые влияют на внешний вид объявления.
      - **restSpending** - Остальные расходы в копейках. Сколько денег вы потратили на чат-ботов и услуги, которые система не смогла распознать.
      - **commission** - Комиссия в копейках. Какую комиссию вы заплатили за заказы с Авито Доставкой, которые приняли покупатели, а также за бронирования жилья.
    - **spendingBonus** - Списано бонусов на объявления. Сколько бонусов вы потратили на размещение, продвижение, целевые действия и комиссию.


#### Количество объявлений за период

  - **activeItems** - Активные объявления. Объявления, которые прошли проверку и появились в поиске.        
    - **newActiveItems** - Новые и опубликованные заново объявления. Сколько объявлений опубликовано впервые или повторно.
    - **oldActiveItems** - Активны с прошлого периода. Сколько объявлений остаются опубликованными с предыдущего периода.


### Примечания

  * Из ручки возвращается не более чем по 1000 сущностей. Вы можете использовать поля запроса limit и offset для регулировки выбранного диапазона.
  * Глубина данных статистики такого запроса ограничена 270 днями.
  * В случае недоступности метрики для пользователя она не приходит в ответе. 
  * Система позволяет делать не более одного запроса в минуту на данный метод.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.analytics_request import AnalyticsRequest
from avito_ads.models.analytics_response import AnalyticsResponse
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Идентификатор пользователя (клиента)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    content_type = 'application/json' # str | Тип данных запроса
    analytics_request = avito_ads.AnalyticsRequest() # AnalyticsRequest | 

    try:
        # Получение статистических показателей по профилю
        api_response = api_instance.item_analytics(user_id, authorization, content_type, analytics_request)
        print("The response of ItemApi->item_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **authorization** | **str**| Токен для авторизации | 
 **content_type** | **str**| Тип данных запроса | 
 **analytics_request** | [**AnalyticsRequest**](AnalyticsRequest.md)|  | 

### Return type

[**AnalyticsResponse**](AnalyticsResponse.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Неверный запрос |  -  |
**401** | Требуется аутентификация |  -  |
**403** | Доступ запрещен |  -  |
**429** | Слишком много запросов |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_stats_shallow**
> StatisticsResponse item_stats_shallow(user_id, authorization, content_type, statistics_shallow_request_body=statistics_shallow_request_body)

Получение статистики по списку объявлений

Получение счетчиков по переданному списку объявлений пользователя.

**Внимание:** в запросе может быть передано не более 200 идентификаторов объявлений.

**Внимание:** глубина такого запроса ограничена 270 днями.

### Счетчики
* ~~views - общее число просмотров объявления;~~ __DEPRECATED (будет удалено в апреле 2021 г.).__ Используйте поле uniqViews.
* uniqViews - число уникальных пользователей, просмотревших объявление;
* ~~contacts - число контактов [1];~~ __DEPRECATED (будет удалено в апреле 2021 г.).__ Используйте поле uniqContacts.
* uniqContacts - число уникальных пользователей, совершивших контакты [1];
* ~~favorites - число добавлений объявления в "избранное";~~ __DEPRECATED (будет удалено в апреле 2021 г.).__ Используйте поле uniqFavorites.
* uniqFavorites - число уникальных пользователей, добавивших объявление в "избранное".

### Группировка счетчиков
Счетчики могут быть сгруппированы [2] по:
* дням;
* неделям - в поле `date` соответствующей структуры будет первый день недели;
* месяцам - в поле `date` соответствующей структуры будет первый день месяца.

#### Период группировки
Период группировки передается в теле запроса в поле `periodGrouping`. Доступные значения этого поля:
* "day" (по умолчанию) - без группировки;
* "week" - суммирование счетчиков за неделю;
* "month" - суммирование счетчиков за месяц.

### Примечания
* [1]: Под контактом понимаются: запросы телефона продавца, начатый чат с продавцом по конкретному объявлению, отклик на резюме и пр.
* [2]: Группировка уникальных пользователей происходит только в рамках одного дня.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.statistics_response import StatisticsResponse
from avito_ads.models.statistics_shallow_request_body import StatisticsShallowRequestBody
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Идентификатор пользователя (клиента)
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    content_type = 'application/json' # str | Тип данных запроса
    statistics_shallow_request_body = avito_ads.StatisticsShallowRequestBody() # StatisticsShallowRequestBody | Набор параметров в теле запроса. (optional)

    try:
        # Получение статистики по списку объявлений
        api_response = api_instance.item_stats_shallow(user_id, authorization, content_type, statistics_shallow_request_body=statistics_shallow_request_body)
        print("The response of ItemApi->item_stats_shallow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->item_stats_shallow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Идентификатор пользователя (клиента) | 
 **authorization** | **str**| Токен для авторизации | 
 **content_type** | **str**| Тип данных запроса | 
 **statistics_shallow_request_body** | [**StatisticsShallowRequestBody**](StatisticsShallowRequestBody.md)| Набор параметров в теле запроса. | [optional] 

### Return type

[**StatisticsResponse**](StatisticsResponse.md)

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
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_calls_stats**
> CallsStatsResponse post_calls_stats(user_id, authorization, content_type, calls_stats_request)

Получение статистики по звонкам

Получение агрегированной статистики звонков, полученных пользователем


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.calls_stats_request import CallsStatsRequest
from avito_ads.models.calls_stats_response import CallsStatsResponse
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Номер пользователя в Личном кабинете Авито
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    content_type = 'application/json' # str | Тип данных запроса
    calls_stats_request = {"dateFrom":"2020-04-01","dateTo":"2020-04-08","itemIds":[1853257996]} # CallsStatsRequest | 

    try:
        # Получение статистики по звонкам
        api_response = api_instance.post_calls_stats(user_id, authorization, content_type, calls_stats_request)
        print("The response of ItemApi->post_calls_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_calls_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Номер пользователя в Личном кабинете Авито | 
 **authorization** | **str**| Токен для авторизации | 
 **content_type** | **str**| Тип данных запроса | 
 **calls_stats_request** | [**CallsStatsRequest**](CallsStatsRequest.md)|  | 

### Return type

[**CallsStatsResponse**](CallsStatsResponse.md)

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
**500** | Внутренняя ошибка метода API |  -  |
**503** | Метод API временно недоступен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_item_vas**
> VasApplyAvito put_item_vas(user_id, item_id, authorization, vas_id_request_body=vas_id_request_body)

Применение дополнительных услуг

**Внимание:** метод объявлен устаревшим и больше не поддерживается. Вместо него используйте метод `/core/v2/items/{itemId}/vas/`

Применение дополнительной услуги к объявлению, в ответе возвращает данные о примененной услуге и сумму списания.
[Более подробная информация по дополнительным услугам](https://support.avito.ru/sections/200009758)

**Внимание:** получение ошибки при выполнении этой операции не означает, что услуга точно не была куплена.
В этом случае рекомендуется подождать несколько минут и проверить, что услуга отсутствует в списке применённых, а только затем повторить попытку.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.vas_apply_avito import VasApplyAvito
from avito_ads.models.vas_id_request_body import VasIdRequestBody
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Номер пользователя в Личном кабинете Авито
    item_id = 56 # int | Идентификатор объявления на сайте
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    vas_id_request_body = {"vas_id":"highlight"} # VasIdRequestBody |  (optional)

    try:
        # Применение дополнительных услуг
        api_response = api_instance.put_item_vas(user_id, item_id, authorization, vas_id_request_body=vas_id_request_body)
        print("The response of ItemApi->put_item_vas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->put_item_vas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Номер пользователя в Личном кабинете Авито | 
 **item_id** | **int**| Идентификатор объявления на сайте | 
 **authorization** | **str**| Токен для авторизации | 
 **vas_id_request_body** | [**VasIdRequestBody**](VasIdRequestBody.md)|  | [optional] 

### Return type

[**VasApplyAvito**](VasApplyAvito.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**0** | Информация об ошибке |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_item_vas_package_v2**
> VasAmountAvito put_item_vas_package_v2(user_id, item_id, authorization, package_id_request_body_v2=package_id_request_body_v2)

Применение пакета дополнительных услуг

**Внимание:** метод объявлен устаревшим и больше не поддерживается. Вместо него используйте метод `/core/v2/items/{itemId}/vas/`

Применение пакета дополнительных услуг к объявлению, в ответе возвращает сумму списания.

**Внимание:** получение ошибки при выполнении этой операции не означает, что пакет точно не была куплен.
В этом случае рекомендуется подождать несколько минут и проверить, что пакет отсутствует в списке применённых, а только затем повторить попытку.


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.package_id_request_body_v2 import PackageIdRequestBodyV2
from avito_ads.models.vas_amount_avito import VasAmountAvito
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Номер пользователя в Личном кабинете Авито
    item_id = 56 # int | Идентификатор объявления на сайте
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    package_id_request_body_v2 = {"package_id":"x10_7"} # PackageIdRequestBodyV2 |  (optional)

    try:
        # Применение пакета дополнительных услуг
        api_response = api_instance.put_item_vas_package_v2(user_id, item_id, authorization, package_id_request_body_v2=package_id_request_body_v2)
        print("The response of ItemApi->put_item_vas_package_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->put_item_vas_package_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Номер пользователя в Личном кабинете Авито | 
 **item_id** | **int**| Идентификатор объявления на сайте | 
 **authorization** | **str**| Токен для авторизации | 
 **package_id_request_body_v2** | [**PackageIdRequestBodyV2**](PackageIdRequestBodyV2.md)|  | [optional] 

### Return type

[**VasAmountAvito**](VasAmountAvito.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**0** | Информация об ошибке |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vas_prices**
> VasPrices200Response vas_prices(user_id, authorization, prices_item_ids_request_body=prices_item_ids_request_body)

Получение информации о стоимости услуг продвижения и доступных значках

Возвращает в ответ список объектов со следующей структурой:
- `itemId` – идентификатор объявления
- `vas` – список объектов, которые содержат информацию о стоимости дополнительных услуг и пакетов дополнительных услуг для каждого объявления. Структура объекта:
  - `slug` – идентификатор услуги или пакета услуг:
    - `highlight` — [услуга продвижения "Выделить"](https://support.avito.ru/articles/200026858)
    - `xl` – [услуга продвижения "XL-объявление"](https://support.avito.ru/articles/685)
    - `stickerpack_x1` – [1 значок на XL-объявлении](https://support.avito.ru/articles/2450) 
    - `stickerpack_x2` – [2 значка на XL-объявлении](https://support.avito.ru/articles/2450)
    - `stickerpack_x3` – [3 значка на XL-объявлении](https://support.avito.ru/articles/2450)

    - `x2_1` – [пакет "до 2 раз больше просмотров на 1 день"](https://support.avito.ru/articles/1398)
    - `x2_7` – [пакет "до 2 раз больше просмотров на 7 дней"](https://support.avito.ru/articles/1398)
    - `x5_1` – [пакет "до 5 раз больше просмотров на 1 день"](https://support.avito.ru/articles/1398)
    - `x5_7` – [пакет "до 5 раз больше просмотров на 7 дней"](https://support.avito.ru/articles/1398)
    - `x10_1` – [пакет "до 10 раз больше просмотров на 1 день"](https://support.avito.ru/articles/1398)
    - `x10_7` – [пакет "до 10 раз больше просмотров на 7 дней"](https://support.avito.ru/articles/1398)
    - `x15_1` – [пакет "до 15 раз больше просмотров на 1 день"](https://support.avito.ru/articles/1398)
    - `x15_7` – [пакет "до 15 раз больше просмотров на 7 дней"](https://support.avito.ru/articles/1398)
    - `x20_1` – [пакет "до 20 раз больше просмотров на 1 день"](https://support.avito.ru/articles/1398)
    - `x20_7` – [пакет "до 20 раз больше просмотров на 7 дней"](https://support.avito.ru/articles/1398)

  - `price` – цена в рублях с учетом скидки

  - `priceOld` – цена в рублях до применения скидки

- `stickers` – список объектов которые содержат доступные для объявления  [значки](https://support.avito.ru/articles/2450)
  - `id` – идентификатор значка
  - `title` – название значка
  - `description` – описание значка


### Example

* OAuth Authentication (AuthorizationCode):
* OAuth Authentication (ClientCredentials):

```python
import avito_ads
from avito_ads.models.prices_item_ids_request_body import PricesItemIdsRequestBody
from avito_ads.models.vas_prices200_response import VasPrices200Response
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
    api_instance = avito_ads.ItemApi(api_client)
    user_id = 56 # int | Номер пользователя в Личном кабинете Авито
    authorization = 'Bearer ACCESS_TOKEN' # str | Токен для авторизации
    prices_item_ids_request_body = {"itemIds":[1234567,7654321]} # PricesItemIdsRequestBody | Набор идентификаторов объявлений на сайте (optional)

    try:
        # Получение информации о стоимости услуг продвижения и доступных значках
        api_response = api_instance.vas_prices(user_id, authorization, prices_item_ids_request_body=prices_item_ids_request_body)
        print("The response of ItemApi->vas_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->vas_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Номер пользователя в Личном кабинете Авито | 
 **authorization** | **str**| Токен для авторизации | 
 **prices_item_ids_request_body** | [**PricesItemIdsRequestBody**](PricesItemIdsRequestBody.md)| Набор идентификаторов объявлений на сайте | [optional] 

### Return type

[**VasPrices200Response**](VasPrices200Response.md)

### Authorization

[AuthorizationCode](../README.md#AuthorizationCode), [ClientCredentials](../README.md#ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешный ответ |  -  |
**0** | Информация об ошибке |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

