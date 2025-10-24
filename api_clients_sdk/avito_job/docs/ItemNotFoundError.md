# ItemNotFoundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ItemNotFoundErrorError**](ItemNotFoundErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.item_not_found_error import ItemNotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of ItemNotFoundError from a JSON string
item_not_found_error_instance = ItemNotFoundError.from_json(json)
# print the JSON string representation of the object
print(ItemNotFoundError.to_json())

# convert the object into a dict
item_not_found_error_dict = item_not_found_error_instance.to_dict()
# create an instance of ItemNotFoundError from a dict
item_not_found_error_from_dict = ItemNotFoundError.from_dict(item_not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


