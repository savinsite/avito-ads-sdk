# ValidatingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ValidatingErrorError**](ValidatingErrorError.md) |  | [optional] 

## Example

```python
from avito_ads.models.validating_error import ValidatingError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingError from a JSON string
validating_error_instance = ValidatingError.from_json(json)
# print the JSON string representation of the object
print(ValidatingError.to_json())

# convert the object into a dict
validating_error_dict = validating_error_instance.to_dict()
# create an instance of ValidatingError from a dict
validating_error_from_dict = ValidatingError.from_dict(validating_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


