# NotFoundErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_ads.models.not_found_error_error import NotFoundErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundErrorError from a JSON string
not_found_error_error_instance = NotFoundErrorError.from_json(json)
# print the JSON string representation of the object
print(NotFoundErrorError.to_json())

# convert the object into a dict
not_found_error_error_dict = not_found_error_error_instance.to_dict()
# create an instance of NotFoundErrorError from a dict
not_found_error_error_from_dict = NotFoundErrorError.from_dict(not_found_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


