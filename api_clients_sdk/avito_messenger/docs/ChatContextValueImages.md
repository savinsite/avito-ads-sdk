# ChatContextValueImages

Изображения с карточки объявления

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Число изображений | [optional] 
**main** | [**ChatContextValueImagesMain**](ChatContextValueImagesMain.md) |  | [optional] 

## Example

```python
from avito_messenger.models.chat_context_value_images import ChatContextValueImages

# TODO update the JSON string below
json = "{}"
# create an instance of ChatContextValueImages from a JSON string
chat_context_value_images_instance = ChatContextValueImages.from_json(json)
# print the JSON string representation of the object
print(ChatContextValueImages.to_json())

# convert the object into a dict
chat_context_value_images_dict = chat_context_value_images_instance.to_dict()
# create an instance of ChatContextValueImages from a dict
chat_context_value_images_from_dict = ChatContextValueImages.from_dict(chat_context_value_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


