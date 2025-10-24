# ServiceUnavailableError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ServiceUnavailableErrorError**](ServiceUnavailableErrorError.md) |  | [optional] 

## Example

```python
from avito_ads.models.service_unavailable_error import ServiceUnavailableError

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUnavailableError from a JSON string
service_unavailable_error_instance = ServiceUnavailableError.from_json(json)
# print the JSON string representation of the object
print(ServiceUnavailableError.to_json())

# convert the object into a dict
service_unavailable_error_dict = service_unavailable_error_instance.to_dict()
# create an instance of ServiceUnavailableError from a dict
service_unavailable_error_from_dict = ServiceUnavailableError.from_dict(service_unavailable_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


