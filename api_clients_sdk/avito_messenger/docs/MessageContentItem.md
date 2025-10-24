# MessageContentItem

Объект, описывающий объявление, для сообщения типа item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** |  | [optional] 
**item_url** | **str** |  | [optional] 
**price_string** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_item import MessageContentItem

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentItem from a JSON string
message_content_item_instance = MessageContentItem.from_json(json)
# print the JSON string representation of the object
print(MessageContentItem.to_json())

# convert the object into a dict
message_content_item_dict = message_content_item_instance.to_dict()
# create an instance of MessageContentItem from a dict
message_content_item_from_dict = MessageContentItem.from_dict(message_content_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


