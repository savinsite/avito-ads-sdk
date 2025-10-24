# PostSendImageMessage200ResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**PostSendImageMessage200ResponseContentImage**](PostSendImageMessage200ResponseContentImage.md) |  | [optional] 

## Example

```python
from avito_messenger.models.post_send_image_message200_response_content import PostSendImageMessage200ResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendImageMessage200ResponseContent from a JSON string
post_send_image_message200_response_content_instance = PostSendImageMessage200ResponseContent.from_json(json)
# print the JSON string representation of the object
print(PostSendImageMessage200ResponseContent.to_json())

# convert the object into a dict
post_send_image_message200_response_content_dict = post_send_image_message200_response_content_instance.to_dict()
# create an instance of PostSendImageMessage200ResponseContent from a dict
post_send_image_message200_response_content_from_dict = PostSendImageMessage200ResponseContent.from_dict(post_send_image_message200_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


