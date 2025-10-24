# ItemNotFoundErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.item_not_found_error_error import ItemNotFoundErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ItemNotFoundErrorError from a JSON string
item_not_found_error_error_instance = ItemNotFoundErrorError.from_json(json)
# print the JSON string representation of the object
print(ItemNotFoundErrorError.to_json())

# convert the object into a dict
item_not_found_error_error_dict = item_not_found_error_error_instance.to_dict()
# create an instance of ItemNotFoundErrorError from a dict
item_not_found_error_error_from_dict = ItemNotFoundErrorError.from_dict(item_not_found_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


