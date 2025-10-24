# CallsStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Начальная дата периода (YYYY-MM-DD) | 
**date_to** | **str** | Конечная дата периода (YYYY-MM-DD) | 
**item_ids** | **List[int]** | Идентификаторы объявлений | [optional] 

## Example

```python
from avito_ads.models.calls_stats_request import CallsStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallsStatsRequest from a JSON string
calls_stats_request_instance = CallsStatsRequest.from_json(json)
# print the JSON string representation of the object
print(CallsStatsRequest.to_json())

# convert the object into a dict
calls_stats_request_dict = calls_stats_request_instance.to_dict()
# create an instance of CallsStatsRequest from a dict
calls_stats_request_from_dict = CallsStatsRequest.from_dict(calls_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


