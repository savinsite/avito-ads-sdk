# AnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **date** | Дата (в формате YYYY-MM-DD), с которой (включительно) надо получить статистику | 
**date_to** | **date** | Дата (в формате YYYY-MM-DD), по которую (включительно) надо получить статистику | 
**filter** | [**AnalyticsRequestFilter**](AnalyticsRequestFilter.md) |  | [optional] 
**grouping** | [**Groupings**](Groupings.md) |  | 
**limit** | **int** | Инструмент пагинации для ограничения количества сущностей в response; | 
**metrics** | **List[str]** | Набор доступных показателей, которые должны присутствовать в ответе | 
**offset** | **int** | инструмент пагинации или смещение, с которого начинается выборка данных; | 
**sort** | [**AnalyticsRequestSort**](AnalyticsRequestSort.md) |  | [optional] 

## Example

```python
from avito_ads.models.analytics_request import AnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRequest from a JSON string
analytics_request_instance = AnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyticsRequest.to_json())

# convert the object into a dict
analytics_request_dict = analytics_request_instance.to_dict()
# create an instance of AnalyticsRequest from a dict
analytics_request_from_dict = AnalyticsRequest.from_dict(analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


