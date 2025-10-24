# PostWebhookV3201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Уникальный идентификатор сообщения webhooks | [optional] 
**payload** | [**PayloadStruct**](PayloadStruct.md) |  | [optional] 
**timestamp** | **int** | Unix-timestamp времени отправки сообщения webhooks | [optional] 
**version** | **str** | Версия webhooks | [optional] 

## Example

```python
from avito_messenger.models.post_webhook_v3201_response import PostWebhookV3201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebhookV3201Response from a JSON string
post_webhook_v3201_response_instance = PostWebhookV3201Response.from_json(json)
# print the JSON string representation of the object
print(PostWebhookV3201Response.to_json())

# convert the object into a dict
post_webhook_v3201_response_dict = post_webhook_v3201_response_instance.to_dict()
# create an instance of PostWebhookV3201Response from a dict
post_webhook_v3201_response_from_dict = PostWebhookV3201Response.from_dict(post_webhook_v3201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


