# CallsStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CallsStatsResponseResult**](CallsStatsResponseResult.md) |  | [optional] 

## Example

```python
from avito_ads.models.calls_stats_response import CallsStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallsStatsResponse from a JSON string
calls_stats_response_instance = CallsStatsResponse.from_json(json)
# print the JSON string representation of the object
print(CallsStatsResponse.to_json())

# convert the object into a dict
calls_stats_response_dict = calls_stats_response_instance.to_dict()
# create an instance of CallsStatsResponse from a dict
calls_stats_response_from_dict = CallsStatsResponse.from_dict(calls_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


