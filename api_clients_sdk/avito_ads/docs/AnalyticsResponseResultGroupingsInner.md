# AnalyticsResponseResultGroupingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**metrics** | [**List[AnalyticsResponseResultGroupingsInnerMetricsInner]**](AnalyticsResponseResultGroupingsInnerMetricsInner.md) |  | [optional] 
**type** | [**Groupings**](Groupings.md) |  | [optional] 

## Example

```python
from avito_ads.models.analytics_response_result_groupings_inner import AnalyticsResponseResultGroupingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsResponseResultGroupingsInner from a JSON string
analytics_response_result_groupings_inner_instance = AnalyticsResponseResultGroupingsInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsResponseResultGroupingsInner.to_json())

# convert the object into a dict
analytics_response_result_groupings_inner_dict = analytics_response_result_groupings_inner_instance.to_dict()
# create an instance of AnalyticsResponseResultGroupingsInner from a dict
analytics_response_result_groupings_inner_from_dict = AnalyticsResponseResultGroupingsInner.from_dict(analytics_response_result_groupings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


