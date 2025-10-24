# ChatContext

Сопутствующая к чату информация, несвязанная с мессенджером напрямую

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип контекста, определяет значение и смысл других полей в объекте контекста | [optional] 
**value** | [**ChatContextValue**](ChatContextValue.md) |  | [optional] 

## Example

```python
from avito_messenger.models.chat_context import ChatContext

# TODO update the JSON string below
json = "{}"
# create an instance of ChatContext from a JSON string
chat_context_instance = ChatContext.from_json(json)
# print the JSON string representation of the object
print(ChatContext.to_json())

# convert the object into a dict
chat_context_dict = chat_context_instance.to_dict()
# create an instance of ChatContext from a dict
chat_context_from_dict = ChatContext.from_dict(chat_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


