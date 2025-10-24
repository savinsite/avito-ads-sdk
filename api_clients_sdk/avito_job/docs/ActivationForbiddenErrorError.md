# ActivationForbiddenErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.activation_forbidden_error_error import ActivationForbiddenErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationForbiddenErrorError from a JSON string
activation_forbidden_error_error_instance = ActivationForbiddenErrorError.from_json(json)
# print the JSON string representation of the object
print(ActivationForbiddenErrorError.to_json())

# convert the object into a dict
activation_forbidden_error_error_dict = activation_forbidden_error_error_instance.to_dict()
# create an instance of ActivationForbiddenErrorError from a dict
activation_forbidden_error_error_from_dict = ActivationForbiddenErrorError.from_dict(activation_forbidden_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


