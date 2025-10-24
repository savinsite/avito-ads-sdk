# StoppingForbiddenErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.stopping_forbidden_error_error import StoppingForbiddenErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of StoppingForbiddenErrorError from a JSON string
stopping_forbidden_error_error_instance = StoppingForbiddenErrorError.from_json(json)
# print the JSON string representation of the object
print(StoppingForbiddenErrorError.to_json())

# convert the object into a dict
stopping_forbidden_error_error_dict = stopping_forbidden_error_error_instance.to_dict()
# create an instance of StoppingForbiddenErrorError from a dict
stopping_forbidden_error_error_from_dict = StoppingForbiddenErrorError.from_dict(stopping_forbidden_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


