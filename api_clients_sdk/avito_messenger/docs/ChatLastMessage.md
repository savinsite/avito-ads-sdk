# ChatLastMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **int** | Ссылка на профиль пользователя в Авито | [optional] 
**content** | [**MessageContent**](MessageContent.md) |  | [optional] 
**created** | **int** | Unix-timestamp времени отправки сообщения | [optional] 
**direction** | **str** | \&quot;in\&quot; для входящих сообщений, \&quot;out\&quot; для исходящих | [optional] 
**id** | **str** | Уникальный идентификатор сообщения | [optional] 
**type** | **str** | Тип контента в сообщений | [optional] 

## Example

```python
from avito_messenger.models.chat_last_message import ChatLastMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatLastMessage from a JSON string
chat_last_message_instance = ChatLastMessage.from_json(json)
# print the JSON string representation of the object
print(ChatLastMessage.to_json())

# convert the object into a dict
chat_last_message_dict = chat_last_message_instance.to_dict()
# create an instance of ChatLastMessage from a dict
chat_last_message_from_dict = ChatLastMessage.from_dict(chat_last_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


