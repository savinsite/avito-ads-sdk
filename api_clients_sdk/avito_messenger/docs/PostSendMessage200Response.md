# PostSendMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**PostSendMessage200ResponseContent**](PostSendMessage200ResponseContent.md) |  | [optional] 
**created** | **int** |  | [optional] 
**direction** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.post_send_message200_response import PostSendMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendMessage200Response from a JSON string
post_send_message200_response_instance = PostSendMessage200Response.from_json(json)
# print the JSON string representation of the object
print(PostSendMessage200Response.to_json())

# convert the object into a dict
post_send_message200_response_dict = post_send_message200_response_instance.to_dict()
# create an instance of PostSendMessage200Response from a dict
post_send_message200_response_from_dict = PostSendMessage200Response.from_dict(post_send_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


