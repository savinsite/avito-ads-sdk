# WebhookMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **int** | ID пользователя, отправившего сообщение | [optional] 
**chat_id** | **str** | Уникальный идентификатор чата, куда отправлено сообщение | [optional] 
**chat_type** | **str** | Тип чата (u2i - чат по объявлению, u2u - чат по профилю пользователя) | [optional] 
**content** | [**MessageContent**](MessageContent.md) |  | [optional] 
**created** | **int** | Unix-timestamp времени создания сообщения | [optional] 
**id** | **str** | Уникальный идентификатор сообщения | [optional] 
**item_id** | **int** | ID объявления, актуально только для чатов с типом u2i | [optional] 
**published_at** | **str** | Время публикации сообщения в формате RFC3339 в UTC | [optional] 
**read** | **int** | Unix-timestamp времени прочтения, если сообщение уже прочитано | [optional] 
**type** | **str** | Тип сообщения | [optional] 
**user_id** | **int** | ID пользователя, получившего сообщение. Это всегда аккаунт, на который зарегистрирован вебхук | [optional] 

## Example

```python
from avito_messenger.models.webhook_message import WebhookMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessage from a JSON string
webhook_message_instance = WebhookMessage.from_json(json)
# print the JSON string representation of the object
print(WebhookMessage.to_json())

# convert the object into a dict
webhook_message_dict = webhook_message_instance.to_dict()
# create an instance of WebhookMessage from a dict
webhook_message_from_dict = WebhookMessage.from_dict(webhook_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


