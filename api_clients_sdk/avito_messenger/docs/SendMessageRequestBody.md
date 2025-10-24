# SendMessageRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**SendMessageRequestBodyMessage**](SendMessageRequestBodyMessage.md) |  | [optional] 
**type** | **str** | Тип сообщения | [optional] 

## Example

```python
from avito_messenger.models.send_message_request_body import SendMessageRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequestBody from a JSON string
send_message_request_body_instance = SendMessageRequestBody.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequestBody.to_json())

# convert the object into a dict
send_message_request_body_dict = send_message_request_body_instance.to_dict()
# create an instance of SendMessageRequestBody from a dict
send_message_request_body_from_dict = SendMessageRequestBody.from_dict(send_message_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


