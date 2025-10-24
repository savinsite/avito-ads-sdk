# MessageContentLink

Объект, описывающий ссылку, для сообщения типа link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | [**MessageContentLinkPreview**](MessageContentLinkPreview.md) |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_link import MessageContentLink

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentLink from a JSON string
message_content_link_instance = MessageContentLink.from_json(json)
# print the JSON string representation of the object
print(MessageContentLink.to_json())

# convert the object into a dict
message_content_link_dict = message_content_link_instance.to_dict()
# create an instance of MessageContentLink from a dict
message_content_link_from_dict = MessageContentLink.from_dict(message_content_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


