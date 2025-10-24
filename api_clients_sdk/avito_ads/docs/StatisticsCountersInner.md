# StatisticsCountersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Идентификатор объявления | [optional] 
**stats** | [**List[StatisticsCountersInnerStatsInner]**](StatisticsCountersInnerStatsInner.md) |  | [optional] 

## Example

```python
from avito_ads.models.statistics_counters_inner import StatisticsCountersInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsCountersInner from a JSON string
statistics_counters_inner_instance = StatisticsCountersInner.from_json(json)
# print the JSON string representation of the object
print(StatisticsCountersInner.to_json())

# convert the object into a dict
statistics_counters_inner_dict = statistics_counters_inner_instance.to_dict()
# create an instance of StatisticsCountersInner from a dict
statistics_counters_inner_from_dict = StatisticsCountersInner.from_dict(statistics_counters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


