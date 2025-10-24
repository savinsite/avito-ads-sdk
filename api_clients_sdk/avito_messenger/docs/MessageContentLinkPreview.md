# MessageContentLinkPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**images** | **object** | объект ключ-значение, где ключи - строки в формате \&quot;ШxВ\&quot; (ширина, высота), а значения - ссылки на изображения | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_link_preview import MessageContentLinkPreview

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentLinkPreview from a JSON string
message_content_link_preview_instance = MessageContentLinkPreview.from_json(json)
# print the JSON string representation of the object
print(MessageContentLinkPreview.to_json())

# convert the object into a dict
message_content_link_preview_dict = message_content_link_preview_instance.to_dict()
# create an instance of MessageContentLinkPreview from a dict
message_content_link_preview_from_dict = MessageContentLinkPreview.from_dict(message_content_link_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


