# PayloadStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип сообщения | [optional] 
**value** | [**WebhookMessage**](WebhookMessage.md) |  | [optional] 

## Example

```python
from avito_messenger.models.payload_struct import PayloadStruct

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadStruct from a JSON string
payload_struct_instance = PayloadStruct.from_json(json)
# print the JSON string representation of the object
print(PayloadStruct.to_json())

# convert the object into a dict
payload_struct_dict = payload_struct_instance.to_dict()
# create an instance of PayloadStruct from a dict
payload_struct_from_dict = PayloadStruct.from_dict(payload_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


