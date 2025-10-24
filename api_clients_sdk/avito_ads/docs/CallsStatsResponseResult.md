# CallsStatsResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CallsStatsItem]**](CallsStatsItem.md) | Массив статистики по объявлениям | 

## Example

```python
from avito_ads.models.calls_stats_response_result import CallsStatsResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of CallsStatsResponseResult from a JSON string
calls_stats_response_result_instance = CallsStatsResponseResult.from_json(json)
# print the JSON string representation of the object
print(CallsStatsResponseResult.to_json())

# convert the object into a dict
calls_stats_response_result_dict = calls_stats_response_result_instance.to_dict()
# create an instance of CallsStatsResponseResult from a dict
calls_stats_response_result_from_dict = CallsStatsResponseResult.from_dict(calls_stats_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


