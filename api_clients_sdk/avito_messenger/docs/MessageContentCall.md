# MessageContentCall

Объект, описывающий звонок, для сообщения типа call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**target_user_id** | **int** |  | [optional] 

## Example

```python
from avito_messenger.models.message_content_call import MessageContentCall

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentCall from a JSON string
message_content_call_instance = MessageContentCall.from_json(json)
# print the JSON string representation of the object
print(MessageContentCall.to_json())

# convert the object into a dict
message_content_call_dict = message_content_call_instance.to_dict()
# create an instance of MessageContentCall from a dict
message_content_call_from_dict = MessageContentCall.from_dict(message_content_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


