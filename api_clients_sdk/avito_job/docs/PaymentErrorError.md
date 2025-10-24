# PaymentErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип ошибки | [optional] 
**value** | **str** | Значение ошибки | [optional] 

## Example

```python
from avito_job.models.payment_error_error import PaymentErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentErrorError from a JSON string
payment_error_error_instance = PaymentErrorError.from_json(json)
# print the JSON string representation of the object
print(PaymentErrorError.to_json())

# convert the object into a dict
payment_error_error_dict = payment_error_error_instance.to_dict()
# create an instance of PaymentErrorError from a dict
payment_error_error_from_dict = PaymentErrorError.from_dict(payment_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


