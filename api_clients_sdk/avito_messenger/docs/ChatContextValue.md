# ChatContextValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID объявления | [optional] 
**images** | [**ChatContextValueImages**](ChatContextValueImages.md) |  | [optional] 
**price_string** | **str** | Цена в объявлении, с указанием валюты | [optional] 
**status_id** | **int** | Статус объявления, например 20 — объявление удалено | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** | Ссылка на объявление | [optional] 
**user_id** | **int** | ID автора объявления | [optional] 

## Example

```python
from avito_messenger.models.chat_context_value import ChatContextValue

# TODO update the JSON string below
json = "{}"
# create an instance of ChatContextValue from a JSON string
chat_context_value_instance = ChatContextValue.from_json(json)
# print the JSON string representation of the object
print(ChatContextValue.to_json())

# convert the object into a dict
chat_context_value_dict = chat_context_value_instance.to_dict()
# create an instance of ChatContextValue from a dict
chat_context_value_from_dict = ChatContextValue.from_dict(chat_context_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


