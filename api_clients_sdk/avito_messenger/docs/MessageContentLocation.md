# MessageContentLocation

Объект, описывающий геометку, для сообщения типа location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_location import MessageContentLocation

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentLocation from a JSON string
message_content_location_instance = MessageContentLocation.from_json(json)
# print the JSON string representation of the object
print(MessageContentLocation.to_json())

# convert the object into a dict
message_content_location_dict = message_content_location_instance.to_dict()
# create an instance of MessageContentLocation from a dict
message_content_location_from_dict = MessageContentLocation.from_dict(message_content_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


