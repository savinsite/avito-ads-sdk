# CreationForbiddenErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.creation_forbidden_error_error import CreationForbiddenErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of CreationForbiddenErrorError from a JSON string
creation_forbidden_error_error_instance = CreationForbiddenErrorError.from_json(json)
# print the JSON string representation of the object
print(CreationForbiddenErrorError.to_json())

# convert the object into a dict
creation_forbidden_error_error_dict = creation_forbidden_error_error_instance.to_dict()
# create an instance of CreationForbiddenErrorError from a dict
creation_forbidden_error_error_from_dict = CreationForbiddenErrorError.from_dict(creation_forbidden_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


