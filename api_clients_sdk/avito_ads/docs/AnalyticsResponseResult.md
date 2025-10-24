# AnalyticsResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_total_count** | **int** |  | [optional] 
**groupings** | [**List[AnalyticsResponseResultGroupingsInner]**](AnalyticsResponseResultGroupingsInner.md) |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from avito_ads.models.analytics_response_result import AnalyticsResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsResponseResult from a JSON string
analytics_response_result_instance = AnalyticsResponseResult.from_json(json)
# print the JSON string representation of the object
print(AnalyticsResponseResult.to_json())

# convert the object into a dict
analytics_response_result_dict = analytics_response_result_instance.to_dict()
# create an instance of AnalyticsResponseResult from a dict
analytics_response_result_from_dict = AnalyticsResponseResult.from_dict(analytics_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


