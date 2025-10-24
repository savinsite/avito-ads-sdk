# ServiceUnavailableErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Описание ошибки | 

## Example

```python
from avito_messenger.models.service_unavailable_error_error import ServiceUnavailableErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUnavailableErrorError from a JSON string
service_unavailable_error_error_instance = ServiceUnavailableErrorError.from_json(json)
# print the JSON string representation of the object
print(ServiceUnavailableErrorError.to_json())

# convert the object into a dict
service_unavailable_error_error_dict = service_unavailable_error_error_instance.to_dict()
# create an instance of ServiceUnavailableErrorError from a dict
service_unavailable_error_error_from_dict = ServiceUnavailableErrorError.from_dict(service_unavailable_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


