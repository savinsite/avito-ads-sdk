# StatisticsCountersInnerStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **int** | __DEPRECATED (будет удалено в апреле 2021 г.).__ __Используйте поле uniqContacts.__ Запросы контактов объявления.  | [optional] 
**var_date** | **date** | Дата (в формате YYYY-MM-DD), за которую посчитаны статистические счетчики. Для группировок по периодам - дата начала периода. | 
**favorites** | **int** | __DEPRECATED (будет удалено в апреле 2021 г.).__ __Используйте поле uniqFavorites.__ Добавления объявления в избранное | [optional] 
**uniq_contacts** | **int** | Уникальные пользователи, запрашивавшие контакты объявления | [optional] 
**uniq_favorites** | **int** | Уникальные пользователи, добавившие объявление в избранное | [optional] 
**uniq_views** | **int** | Уникальные пользователи, просматривавшие объявления | [optional] 
**views** | **int** | __DEPRECATED (будет удалено в апреле 2021 г.).__ __Используйте поле uniqViews.__ Просмотры объявления.  | [optional] 

## Example

```python
from avito_ads.models.statistics_counters_inner_stats_inner import StatisticsCountersInnerStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsCountersInnerStatsInner from a JSON string
statistics_counters_inner_stats_inner_instance = StatisticsCountersInnerStatsInner.from_json(json)
# print the JSON string representation of the object
print(StatisticsCountersInnerStatsInner.to_json())

# convert the object into a dict
statistics_counters_inner_stats_inner_dict = statistics_counters_inner_stats_inner_instance.to_dict()
# create an instance of StatisticsCountersInnerStatsInner from a dict
statistics_counters_inner_stats_inner_from_dict = StatisticsCountersInnerStatsInner.from_dict(statistics_counters_inner_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


