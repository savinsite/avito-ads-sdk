# BadRequestShortError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Причина возникновения ошибки (может не присутствовать) | [optional] 
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Ключ поля | [optional] 

## Example

```python
from avito_job.models.bad_request_short_error import BadRequestShortError

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestShortError from a JSON string
bad_request_short_error_instance = BadRequestShortError.from_json(json)
# print the JSON string representation of the object
print(BadRequestShortError.to_json())

# convert the object into a dict
bad_request_short_error_dict = bad_request_short_error_instance.to_dict()
# create an instance of BadRequestShortError from a dict
bad_request_short_error_from_dict = BadRequestShortError.from_dict(bad_request_short_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


