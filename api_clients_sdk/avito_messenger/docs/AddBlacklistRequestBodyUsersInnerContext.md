# AddBlacklistRequestBodyUsersInnerContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** |  | [optional] 
**reason_id** | **int** | причина, по которой блокируем пользователя, 1 - спам, 2 - мошенничество, 3 - оскорбления и хамство, 4 - другая причина | [optional] 

## Example

```python
from avito_messenger.models.add_blacklist_request_body_users_inner_context import AddBlacklistRequestBodyUsersInnerContext

# TODO update the JSON string below
json = "{}"
# create an instance of AddBlacklistRequestBodyUsersInnerContext from a JSON string
add_blacklist_request_body_users_inner_context_instance = AddBlacklistRequestBodyUsersInnerContext.from_json(json)
# print the JSON string representation of the object
print(AddBlacklistRequestBodyUsersInnerContext.to_json())

# convert the object into a dict
add_blacklist_request_body_users_inner_context_dict = add_blacklist_request_body_users_inner_context_instance.to_dict()
# create an instance of AddBlacklistRequestBodyUsersInnerContext from a dict
add_blacklist_request_body_users_inner_context_from_dict = AddBlacklistRequestBodyUsersInnerContext.from_dict(add_blacklist_request_body_users_inner_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


