# MessageContent

Для сообщений типов \"appCall\" \"file\" \"video\" возвращается empty object (данные типы не поддерживаются)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call** | [**MessageContentCall**](MessageContentCall.md) |  | [optional] 
**flow_id** | **str** | Идентификатор чат-бота, отправившего сообщение, для сообщений типа system | [optional] 
**image** | [**MessageContentImage**](MessageContentImage.md) |  | [optional] 
**item** | [**MessageContentItem**](MessageContentItem.md) |  | [optional] 
**link** | [**MessageContentLink**](MessageContentLink.md) |  | [optional] 
**location** | [**MessageContentLocation**](MessageContentLocation.md) |  | [optional] 
**text** | **str** | Текст сообщения, для сообщения типа text | [optional] 
**voice** | [**MessageContentVoice**](MessageContentVoice.md) |  | [optional] 

## Example

```python
from avito_messenger.models.message_content import MessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContent from a JSON string
message_content_instance = MessageContent.from_json(json)
# print the JSON string representation of the object
print(MessageContent.to_json())

# convert the object into a dict
message_content_dict = message_content_instance.to_dict()
# create an instance of MessageContent from a dict
message_content_from_dict = MessageContent.from_dict(message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


