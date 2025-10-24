# ChatUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Уникальный ID пользователя. Обратите внимание на хэширование | [optional] 
**name** | **str** | Имя пользователя | [optional] 
**public_user_profile** | [**ChatUsersInnerPublicUserProfile**](ChatUsersInnerPublicUserProfile.md) |  | [optional] 

## Example

```python
from avito_messenger.models.chat_users_inner import ChatUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUsersInner from a JSON string
chat_users_inner_instance = ChatUsersInner.from_json(json)
# print the JSON string representation of the object
print(ChatUsersInner.to_json())

# convert the object into a dict
chat_users_inner_dict = chat_users_inner_instance.to_dict()
# create an instance of ChatUsersInner from a dict
chat_users_inner_from_dict = ChatUsersInner.from_dict(chat_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


