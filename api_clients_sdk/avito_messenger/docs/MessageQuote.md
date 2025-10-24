# MessageQuote

цитируемое сообщение

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **int** |  | [optional] 
**content** | [**MessageContent**](MessageContent.md) |  | [optional] 
**created** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.message_quote import MessageQuote

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQuote from a JSON string
message_quote_instance = MessageQuote.from_json(json)
# print the JSON string representation of the object
print(MessageQuote.to_json())

# convert the object into a dict
message_quote_dict = message_quote_instance.to_dict()
# create an instance of MessageQuote from a dict
message_quote_from_dict = MessageQuote.from_dict(message_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


