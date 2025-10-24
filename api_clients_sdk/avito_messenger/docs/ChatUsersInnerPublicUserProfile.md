# ChatUsersInnerPublicUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | [**ChatUsersInnerPublicUserProfileAvatar**](ChatUsersInnerPublicUserProfileAvatar.md) |  | [optional] 
**item_id** | **int** | ID объявления, выложенного пользователем | [optional] 
**url** | **str** | Ссылка на профиль пользователя в Авито | [optional] 
**user_id** | **int** | Уникальный ID пользователя. Обратите внимание на хэширование | [optional] 

## Example

```python
from avito_messenger.models.chat_users_inner_public_user_profile import ChatUsersInnerPublicUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUsersInnerPublicUserProfile from a JSON string
chat_users_inner_public_user_profile_instance = ChatUsersInnerPublicUserProfile.from_json(json)
# print the JSON string representation of the object
print(ChatUsersInnerPublicUserProfile.to_json())

# convert the object into a dict
chat_users_inner_public_user_profile_dict = chat_users_inner_public_user_profile_instance.to_dict()
# create an instance of ChatUsersInnerPublicUserProfile from a dict
chat_users_inner_public_user_profile_from_dict = ChatUsersInnerPublicUserProfile.from_dict(chat_users_inner_public_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


