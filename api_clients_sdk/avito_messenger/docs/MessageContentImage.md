# MessageContentImage

Объект, описывающий изображение, для сообщения типа image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sizes** | **object** | объект ключ-значение, где ключи - строки в формате \&quot;ШxВ\&quot; (ширина, высота), а значения - ссылки на изображения | [optional] 

## Example

```python
from avito_messenger.models.message_content_image import MessageContentImage

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentImage from a JSON string
message_content_image_instance = MessageContentImage.from_json(json)
# print the JSON string representation of the object
print(MessageContentImage.to_json())

# convert the object into a dict
message_content_image_dict = message_content_image_instance.to_dict()
# create an instance of MessageContentImage from a dict
message_content_image_from_dict = MessageContentImage.from_dict(message_content_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


