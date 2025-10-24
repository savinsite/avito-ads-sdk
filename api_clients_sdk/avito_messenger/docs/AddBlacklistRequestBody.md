# AddBlacklistRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[AddBlacklistRequestBodyUsersInner]**](AddBlacklistRequestBodyUsersInner.md) |  | [optional] 

## Example

```python
from avito_messenger.models.add_blacklist_request_body import AddBlacklistRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddBlacklistRequestBody from a JSON string
add_blacklist_request_body_instance = AddBlacklistRequestBody.from_json(json)
# print the JSON string representation of the object
print(AddBlacklistRequestBody.to_json())

# convert the object into a dict
add_blacklist_request_body_dict = add_blacklist_request_body_instance.to_dict()
# create an instance of AddBlacklistRequestBody from a dict
add_blacklist_request_body_from_dict = AddBlacklistRequestBody.from_dict(add_blacklist_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


