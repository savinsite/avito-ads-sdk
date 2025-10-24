# CreationForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**CreationForbiddenErrorError**](CreationForbiddenErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.creation_forbidden_error import CreationForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of CreationForbiddenError from a JSON string
creation_forbidden_error_instance = CreationForbiddenError.from_json(json)
# print the JSON string representation of the object
print(CreationForbiddenError.to_json())

# convert the object into a dict
creation_forbidden_error_dict = creation_forbidden_error_instance.to_dict()
# create an instance of CreationForbiddenError from a dict
creation_forbidden_error_from_dict = CreationForbiddenError.from_dict(creation_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


