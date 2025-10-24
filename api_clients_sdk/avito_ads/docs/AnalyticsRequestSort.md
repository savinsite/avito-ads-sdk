# AnalyticsRequestSort

Сортировка по заданному показателю

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Показатель статистики, по которому нужно отсортировать; | 
**order** | **str** | Порядок сортировки (asc, desc); | 

## Example

```python
from avito_ads.models.analytics_request_sort import AnalyticsRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRequestSort from a JSON string
analytics_request_sort_instance = AnalyticsRequestSort.from_json(json)
# print the JSON string representation of the object
print(AnalyticsRequestSort.to_json())

# convert the object into a dict
analytics_request_sort_dict = analytics_request_sort_instance.to_dict()
# create an instance of AnalyticsRequestSort from a dict
analytics_request_sort_from_dict = AnalyticsRequestSort.from_dict(analytics_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


