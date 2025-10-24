# VerificationNeededError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**VerificationNeededErrorError**](VerificationNeededErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.verification_needed_error import VerificationNeededError

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationNeededError from a JSON string
verification_needed_error_instance = VerificationNeededError.from_json(json)
# print the JSON string representation of the object
print(VerificationNeededError.to_json())

# convert the object into a dict
verification_needed_error_dict = verification_needed_error_instance.to_dict()
# create an instance of VerificationNeededError from a dict
verification_needed_error_from_dict = VerificationNeededError.from_dict(verification_needed_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


