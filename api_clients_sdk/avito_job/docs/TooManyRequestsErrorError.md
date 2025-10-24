# TooManyRequestsErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 

## Example

```python
from avito_job.models.too_many_requests_error_error import TooManyRequestsErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyRequestsErrorError from a JSON string
too_many_requests_error_error_instance = TooManyRequestsErrorError.from_json(json)
# print the JSON string representation of the object
print(TooManyRequestsErrorError.to_json())

# convert the object into a dict
too_many_requests_error_error_dict = too_many_requests_error_error_instance.to_dict()
# create an instance of TooManyRequestsErrorError from a dict
too_many_requests_error_error_from_dict = TooManyRequestsErrorError.from_dict(too_many_requests_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


