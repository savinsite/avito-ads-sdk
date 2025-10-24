# StatisticsResponseResult

Статистические счетчики объявления

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StatisticsCountersInner]**](StatisticsCountersInner.md) |  | [optional] 

## Example

```python
from avito_ads.models.statistics_response_result import StatisticsResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsResponseResult from a JSON string
statistics_response_result_instance = StatisticsResponseResult.from_json(json)
# print the JSON string representation of the object
print(StatisticsResponseResult.to_json())

# convert the object into a dict
statistics_response_result_dict = statistics_response_result_instance.to_dict()
# create an instance of StatisticsResponseResult from a dict
statistics_response_result_from_dict = StatisticsResponseResult.from_dict(statistics_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


