# ItemInfoAvito


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoload_item_id** | **str** | [Идентификатор объявления](https://autoload.avito.ru/format/realty/#Id) из файла автозагрузки | [optional] 
**finish_time** | **datetime** | Дата завершения объявления | [optional] 
**start_time** | **datetime** | Дата создания объявления | [optional] 
**status** | **str** | Статус объявления на сайте | [optional] 
**url** | **str** | URL-адрес объявления | [optional] 
**vas** | [**List[InfoVas]**](InfoVas.md) | Список примененных платных услуг | [optional] 

## Example

```python
from avito_ads.models.item_info_avito import ItemInfoAvito

# TODO update the JSON string below
json = "{}"
# create an instance of ItemInfoAvito from a JSON string
item_info_avito_instance = ItemInfoAvito.from_json(json)
# print the JSON string representation of the object
print(ItemInfoAvito.to_json())

# convert the object into a dict
item_info_avito_dict = item_info_avito_instance.to_dict()
# create an instance of ItemInfoAvito from a dict
item_info_avito_from_dict = ItemInfoAvito.from_dict(item_info_avito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


