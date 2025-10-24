# AuthErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_messenger.models.auth_error_error import AuthErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthErrorError from a JSON string
auth_error_error_instance = AuthErrorError.from_json(json)
# print the JSON string representation of the object
print(AuthErrorError.to_json())

# convert the object into a dict
auth_error_error_dict = auth_error_error_instance.to_dict()
# create an instance of AuthErrorError from a dict
auth_error_error_from_dict = AuthErrorError.from_dict(auth_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


