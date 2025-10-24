# ItemsInfoWithCategoryAvito


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ItemsInfoWithCategoryAvitoMeta**](ItemsInfoWithCategoryAvitoMeta.md) |  | [optional] 
**resources** | [**List[ItemsInfoWithCategoryAvitoResourcesInner]**](ItemsInfoWithCategoryAvitoResourcesInner.md) |  | [optional] 

## Example

```python
from avito_ads.models.items_info_with_category_avito import ItemsInfoWithCategoryAvito

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsInfoWithCategoryAvito from a JSON string
items_info_with_category_avito_instance = ItemsInfoWithCategoryAvito.from_json(json)
# print the JSON string representation of the object
print(ItemsInfoWithCategoryAvito.to_json())

# convert the object into a dict
items_info_with_category_avito_dict = items_info_with_category_avito_instance.to_dict()
# create an instance of ItemsInfoWithCategoryAvito from a dict
items_info_with_category_avito_from_dict = ItemsInfoWithCategoryAvito.from_dict(items_info_with_category_avito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


