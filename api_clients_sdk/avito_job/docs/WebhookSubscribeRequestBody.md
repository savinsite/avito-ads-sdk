# WebhookSubscribeRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | сгенерированный ключ | 
**url** | **str** | URL на который будут отправляться уведомления | 

## Example

```python
from avito_job.models.webhook_subscribe_request_body import WebhookSubscribeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscribeRequestBody from a JSON string
webhook_subscribe_request_body_instance = WebhookSubscribeRequestBody.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscribeRequestBody.to_json())

# convert the object into a dict
webhook_subscribe_request_body_dict = webhook_subscribe_request_body_instance.to_dict()
# create an instance of WebhookSubscribeRequestBody from a dict
webhook_subscribe_request_body_from_dict = WebhookSubscribeRequestBody.from_dict(webhook_subscribe_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


