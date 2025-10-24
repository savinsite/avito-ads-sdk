# PostSendImageMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **int** |  | [optional] 
**content** | [**PostSendImageMessage200ResponseContent**](PostSendImageMessage200ResponseContent.md) |  | [optional] 
**created** | **int** |  | [optional] 
**direction** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from avito_messenger.models.post_send_image_message200_response import PostSendImageMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendImageMessage200Response from a JSON string
post_send_image_message200_response_instance = PostSendImageMessage200Response.from_json(json)
# print the JSON string representation of the object
print(PostSendImageMessage200Response.to_json())

# convert the object into a dict
post_send_image_message200_response_dict = post_send_image_message200_response_instance.to_dict()
# create an instance of PostSendImageMessage200Response from a dict
post_send_image_message200_response_from_dict = PostSendImageMessage200Response.from_dict(post_send_image_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


