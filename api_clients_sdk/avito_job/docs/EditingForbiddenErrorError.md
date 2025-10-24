# EditingForbiddenErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.editing_forbidden_error_error import EditingForbiddenErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of EditingForbiddenErrorError from a JSON string
editing_forbidden_error_error_instance = EditingForbiddenErrorError.from_json(json)
# print the JSON string representation of the object
print(EditingForbiddenErrorError.to_json())

# convert the object into a dict
editing_forbidden_error_error_dict = editing_forbidden_error_error_instance.to_dict()
# create an instance of EditingForbiddenErrorError from a dict
editing_forbidden_error_error_from_dict = EditingForbiddenErrorError.from_dict(editing_forbidden_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


