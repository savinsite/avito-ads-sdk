# ActivationForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ActivationForbiddenErrorError**](ActivationForbiddenErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.activation_forbidden_error import ActivationForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationForbiddenError from a JSON string
activation_forbidden_error_instance = ActivationForbiddenError.from_json(json)
# print the JSON string representation of the object
print(ActivationForbiddenError.to_json())

# convert the object into a dict
activation_forbidden_error_dict = activation_forbidden_error_instance.to_dict()
# create an instance of ActivationForbiddenError from a dict
activation_forbidden_error_from_dict = ActivationForbiddenError.from_dict(activation_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


