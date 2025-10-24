# CallsStatsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | [**List[CallsStatsDay]**](CallsStatsDay.md) | Массив статистики звонков объявления в разрезе дней | [optional] 
**employee_id** | **int** | Идентификатор сотрудника в сервисе иерархии аккаунтов (0 означает, что звонок не аттрибуцирован до сотрудника) | 
**item_id** | **int** | Идентификатор объявления (0 означает, что звонок не аттрибуцирован до объявления) | 

## Example

```python
from avito_ads.models.calls_stats_item import CallsStatsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CallsStatsItem from a JSON string
calls_stats_item_instance = CallsStatsItem.from_json(json)
# print the JSON string representation of the object
print(CallsStatsItem.to_json())

# convert the object into a dict
calls_stats_item_dict = calls_stats_item_instance.to_dict()
# create an instance of CallsStatsItem from a dict
calls_stats_item_from_dict = CallsStatsItem.from_dict(calls_stats_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


