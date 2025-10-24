# ValidatingErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**fields** | **object** | Информация об ошибке валидации параметров в формате ключ-значение | [optional] 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_ads.models.validating_error_error import ValidatingErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingErrorError from a JSON string
validating_error_error_instance = ValidatingErrorError.from_json(json)
# print the JSON string representation of the object
print(ValidatingErrorError.to_json())

# convert the object into a dict
validating_error_error_dict = validating_error_error_instance.to_dict()
# create an instance of ValidatingErrorError from a dict
validating_error_error_from_dict = ValidatingErrorError.from_dict(validating_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


