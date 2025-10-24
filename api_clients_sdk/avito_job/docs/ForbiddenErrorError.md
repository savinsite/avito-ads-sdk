# ForbiddenErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_job.models.forbidden_error_error import ForbiddenErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenErrorError from a JSON string
forbidden_error_error_instance = ForbiddenErrorError.from_json(json)
# print the JSON string representation of the object
print(ForbiddenErrorError.to_json())

# convert the object into a dict
forbidden_error_error_dict = forbidden_error_error_instance.to_dict()
# create an instance of ForbiddenErrorError from a dict
forbidden_error_error_from_dict = ForbiddenErrorError.from_dict(forbidden_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


