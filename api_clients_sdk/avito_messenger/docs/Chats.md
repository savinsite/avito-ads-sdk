# Chats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[Chat]**](Chat.md) | Список чатов | [optional] 

## Example

```python
from avito_messenger.models.chats import Chats

# TODO update the JSON string below
json = "{}"
# create an instance of Chats from a JSON string
chats_instance = Chats.from_json(json)
# print the JSON string representation of the object
print(Chats.to_json())

# convert the object into a dict
chats_dict = chats_instance.to_dict()
# create an instance of Chats from a dict
chats_from_dict = Chats.from_dict(chats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


