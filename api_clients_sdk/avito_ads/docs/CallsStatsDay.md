# CallsStatsDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answered** | **int** | Отвеченные звонки | [optional] 
**calls** | **int** | Звонки всего | [optional] 
**var_date** | **str** | Дата (YYYY-MM-DD) | [optional] 
**new** | **int** | Новые звонки | [optional] 
**new_answered** | **int** | Новые и одновременно отвеченные звонки | [optional] 

## Example

```python
from avito_ads.models.calls_stats_day import CallsStatsDay

# TODO update the JSON string below
json = "{}"
# create an instance of CallsStatsDay from a JSON string
calls_stats_day_instance = CallsStatsDay.from_json(json)
# print the JSON string representation of the object
print(CallsStatsDay.to_json())

# convert the object into a dict
calls_stats_day_dict = calls_stats_day_instance.to_dict()
# create an instance of CallsStatsDay from a dict
calls_stats_day_from_dict = CallsStatsDay.from_dict(calls_stats_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


