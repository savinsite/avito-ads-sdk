# MessageContentVoice

Объект, описывающий голосовое сообщение, для сообщения типа voice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_id** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_voice import MessageContentVoice

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentVoice from a JSON string
message_content_voice_instance = MessageContentVoice.from_json(json)
# print the JSON string representation of the object
print(MessageContentVoice.to_json())

# convert the object into a dict
message_content_voice_dict = message_content_voice_instance.to_dict()
# create an instance of MessageContentVoice from a dict
message_content_voice_from_dict = MessageContentVoice.from_dict(message_content_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


