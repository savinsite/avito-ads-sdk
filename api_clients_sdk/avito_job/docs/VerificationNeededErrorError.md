# VerificationNeededErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_job.models.verification_needed_error_error import VerificationNeededErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationNeededErrorError from a JSON string
verification_needed_error_error_instance = VerificationNeededErrorError.from_json(json)
# print the JSON string representation of the object
print(VerificationNeededErrorError.to_json())

# convert the object into a dict
verification_needed_error_error_dict = verification_needed_error_error_instance.to_dict()
# create an instance of VerificationNeededErrorError from a dict
verification_needed_error_error_from_dict = VerificationNeededErrorError.from_dict(verification_needed_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


