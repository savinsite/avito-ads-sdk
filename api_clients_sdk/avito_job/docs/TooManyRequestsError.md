# TooManyRequestsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**TooManyRequestsErrorError**](TooManyRequestsErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.too_many_requests_error import TooManyRequestsError

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyRequestsError from a JSON string
too_many_requests_error_instance = TooManyRequestsError.from_json(json)
# print the JSON string representation of the object
print(TooManyRequestsError.to_json())

# convert the object into a dict
too_many_requests_error_dict = too_many_requests_error_instance.to_dict()
# create an instance of TooManyRequestsError from a dict
too_many_requests_error_from_dict = TooManyRequestsError.from_dict(too_many_requests_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


