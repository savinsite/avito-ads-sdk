# PurchasingErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | 
**message** | **str** | Сообщение об ошибке | 

## Example

```python
from avito_job.models.purchasing_error_error import PurchasingErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasingErrorError from a JSON string
purchasing_error_error_instance = PurchasingErrorError.from_json(json)
# print the JSON string representation of the object
print(PurchasingErrorError.to_json())

# convert the object into a dict
purchasing_error_error_dict = purchasing_error_error_instance.to_dict()
# create an instance of PurchasingErrorError from a dict
purchasing_error_error_from_dict = PurchasingErrorError.from_dict(purchasing_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


