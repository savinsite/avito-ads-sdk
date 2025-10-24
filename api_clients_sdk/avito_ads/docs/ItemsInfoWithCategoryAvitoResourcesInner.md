# ItemsInfoWithCategoryAvitoResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Адрес объявления | [optional] 
**category** | [**ItemsInfoWithCategoryAvitoResourcesInnerCategory**](ItemsInfoWithCategoryAvitoResourcesInnerCategory.md) |  | [optional] 
**id** | **int** | Идентификатор объявления | [optional] 
**price** | **int** | Цена объявления (null значение означает, что цена не указана) | [optional] 
**status** | **str** | Статус объявления на сайте | [optional] 
**title** | **str** | Наименование объявления | [optional] 
**url** | **str** | URL-адрес объявления | [optional] 

## Example

```python
from avito_ads.models.items_info_with_category_avito_resources_inner import ItemsInfoWithCategoryAvitoResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsInfoWithCategoryAvitoResourcesInner from a JSON string
items_info_with_category_avito_resources_inner_instance = ItemsInfoWithCategoryAvitoResourcesInner.from_json(json)
# print the JSON string representation of the object
print(ItemsInfoWithCategoryAvitoResourcesInner.to_json())

# convert the object into a dict
items_info_with_category_avito_resources_inner_dict = items_info_with_category_avito_resources_inner_instance.to_dict()
# create an instance of ItemsInfoWithCategoryAvitoResourcesInner from a dict
items_info_with_category_avito_resources_inner_from_dict = ItemsInfoWithCategoryAvitoResourcesInner.from_dict(items_info_with_category_avito_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


