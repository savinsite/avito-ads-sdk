# PurchasingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**PurchasingErrorError**](PurchasingErrorError.md) |  | [optional] 

## Example

```python
from avito_job.models.purchasing_error import PurchasingError

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasingError from a JSON string
purchasing_error_instance = PurchasingError.from_json(json)
# print the JSON string representation of the object
print(PurchasingError.to_json())

# convert the object into a dict
purchasing_error_dict = purchasing_error_instance.to_dict()
# create an instance of PurchasingError from a dict
purchasing_error_from_dict = PurchasingError.from_dict(purchasing_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


