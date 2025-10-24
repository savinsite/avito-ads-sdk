# StoppingForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**StoppingForbiddenErrorError**](StoppingForbiddenErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.stopping_forbidden_error import StoppingForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of StoppingForbiddenError from a JSON string
stopping_forbidden_error_instance = StoppingForbiddenError.from_json(json)
# print the JSON string representation of the object
print(StoppingForbiddenError.to_json())

# convert the object into a dict
stopping_forbidden_error_dict = stopping_forbidden_error_instance.to_dict()
# create an instance of StoppingForbiddenError from a dict
stopping_forbidden_error_from_dict = StoppingForbiddenError.from_dict(stopping_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


