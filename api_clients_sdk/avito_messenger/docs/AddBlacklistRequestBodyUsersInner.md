# AddBlacklistRequestBodyUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AddBlacklistRequestBodyUsersInnerContext**](AddBlacklistRequestBodyUsersInnerContext.md) |  | [optional] 
**user_id** | **int** | id пользователя которого хотим заблокировать | [optional] 

## Example

```python
from avito_messenger.models.add_blacklist_request_body_users_inner import AddBlacklistRequestBodyUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddBlacklistRequestBodyUsersInner from a JSON string
add_blacklist_request_body_users_inner_instance = AddBlacklistRequestBodyUsersInner.from_json(json)
# print the JSON string representation of the object
print(AddBlacklistRequestBodyUsersInner.to_json())

# convert the object into a dict
add_blacklist_request_body_users_inner_dict = add_blacklist_request_body_users_inner_instance.to_dict()
# create an instance of AddBlacklistRequestBodyUsersInner from a dict
add_blacklist_request_body_users_inner_from_dict = AddBlacklistRequestBodyUsersInner.from_dict(add_blacklist_request_body_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


