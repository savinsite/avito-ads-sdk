# ItemsInfoWithCategoryAvitoMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Номер страницы | [optional] 
**per_page** | **int** | Количество записей на странице | [optional] 

## Example

```python
from avito_ads.models.items_info_with_category_avito_meta import ItemsInfoWithCategoryAvitoMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsInfoWithCategoryAvitoMeta from a JSON string
items_info_with_category_avito_meta_instance = ItemsInfoWithCategoryAvitoMeta.from_json(json)
# print the JSON string representation of the object
print(ItemsInfoWithCategoryAvitoMeta.to_json())

# convert the object into a dict
items_info_with_category_avito_meta_dict = items_info_with_category_avito_meta_instance.to_dict()
# create an instance of ItemsInfoWithCategoryAvitoMeta from a dict
items_info_with_category_avito_meta_from_dict = ItemsInfoWithCategoryAvitoMeta.from_dict(items_info_with_category_avito_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


