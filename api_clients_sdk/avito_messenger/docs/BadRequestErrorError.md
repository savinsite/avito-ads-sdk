# BadRequestErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_messenger.models.bad_request_error_error import BadRequestErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorError from a JSON string
bad_request_error_error_instance = BadRequestErrorError.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorError.to_json())

# convert the object into a dict
bad_request_error_error_dict = bad_request_error_error_instance.to_dict()
# create an instance of BadRequestErrorError from a dict
bad_request_error_error_from_dict = BadRequestErrorError.from_dict(bad_request_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


