# ServiceErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Описание ошибки | 

## Example

```python
from avito_messenger.models.service_error_error import ServiceErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceErrorError from a JSON string
service_error_error_instance = ServiceErrorError.from_json(json)
# print the JSON string representation of the object
print(ServiceErrorError.to_json())

# convert the object into a dict
service_error_error_dict = service_error_error_instance.to_dict()
# create an instance of ServiceErrorError from a dict
service_error_error_from_dict = ServiceErrorError.from_dict(service_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


