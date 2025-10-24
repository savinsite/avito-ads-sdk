# StatisticsShallowRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Дата (в формате YYYY-MM-DD), с которой (включительно) надо получить статистику | 
**date_to** | **str** | Дата (в формате YYYY-MM-DD), по которую (включительно) надо получить статистику | 
**fields** | **List[str]** | Набор счетчиков, которые должны присутствовать в ответе | [optional] 
**item_ids** | **List[int]** | Набор идентификаторов объявлений на сайте | 
**period_grouping** | [**StatisticsPeriodGrouping**](StatisticsPeriodGrouping.md) |  | [optional] 

## Example

```python
from avito_ads.models.statistics_shallow_request_body import StatisticsShallowRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsShallowRequestBody from a JSON string
statistics_shallow_request_body_instance = StatisticsShallowRequestBody.from_json(json)
# print the JSON string representation of the object
print(StatisticsShallowRequestBody.to_json())

# convert the object into a dict
statistics_shallow_request_body_dict = statistics_shallow_request_body_instance.to_dict()
# create an instance of StatisticsShallowRequestBody from a dict
statistics_shallow_request_body_from_dict = StatisticsShallowRequestBody.from_dict(statistics_shallow_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


