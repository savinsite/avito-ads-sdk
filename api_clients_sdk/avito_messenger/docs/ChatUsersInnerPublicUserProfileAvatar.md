# ChatUsersInnerPublicUserProfileAvatar

Фотография пользователя (аватар)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**images** | [**ChatUsersInnerPublicUserProfileAvatarImages**](ChatUsersInnerPublicUserProfileAvatarImages.md) |  | [optional] 

## Example

```python
from avito_messenger.models.chat_users_inner_public_user_profile_avatar import ChatUsersInnerPublicUserProfileAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUsersInnerPublicUserProfileAvatar from a JSON string
chat_users_inner_public_user_profile_avatar_instance = ChatUsersInnerPublicUserProfileAvatar.from_json(json)
# print the JSON string representation of the object
print(ChatUsersInnerPublicUserProfileAvatar.to_json())

# convert the object into a dict
chat_users_inner_public_user_profile_avatar_dict = chat_users_inner_public_user_profile_avatar_instance.to_dict()
# create an instance of ChatUsersInnerPublicUserProfileAvatar from a dict
chat_users_inner_public_user_profile_avatar_from_dict = ChatUsersInnerPublicUserProfileAvatar.from_dict(chat_users_inner_public_user_profile_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


