# SendMessageRequestBodyMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Текст сообщения (максимум 1000 символов) | [optional] 

## Example

```python
from avito_messenger.models.send_message_request_body_message import SendMessageRequestBodyMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequestBodyMessage from a JSON string
send_message_request_body_message_instance = SendMessageRequestBodyMessage.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequestBodyMessage.to_json())

# convert the object into a dict
send_message_request_body_message_dict = send_message_request_body_message_instance.to_dict()
# create an instance of SendMessageRequestBodyMessage from a dict
send_message_request_body_message_from_dict = SendMessageRequestBodyMessage.from_dict(send_message_request_body_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


