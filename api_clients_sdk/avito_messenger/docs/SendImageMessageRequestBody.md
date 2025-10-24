# SendImageMessageRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | Идентификатор загруженного изображения | 

## Example

```python
from avito_messenger.models.send_image_message_request_body import SendImageMessageRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SendImageMessageRequestBody from a JSON string
send_image_message_request_body_instance = SendImageMessageRequestBody.from_json(json)
# print the JSON string representation of the object
print(SendImageMessageRequestBody.to_json())

# convert the object into a dict
send_image_message_request_body_dict = send_image_message_request_body_instance.to_dict()
# create an instance of SendImageMessageRequestBody from a dict
send_image_message_request_body_from_dict = SendImageMessageRequestBody.from_dict(send_image_message_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


