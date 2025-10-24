# StatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**result** | [**StatisticsResponseResult**](StatisticsResponseResult.md) |  | [optional] 

## Example

```python
from avito_ads.models.statistics_response import StatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsResponse from a JSON string
statistics_response_instance = StatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(StatisticsResponse.to_json())

# convert the object into a dict
statistics_response_dict = statistics_response_instance.to_dict()
# create an instance of StatisticsResponse from a dict
statistics_response_from_dict = StatisticsResponse.from_dict(statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


