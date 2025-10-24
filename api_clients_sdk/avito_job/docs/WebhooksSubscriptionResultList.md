# WebhooksSubscriptionResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | [**List[WebhookSubscribeRequestBody]**](WebhookSubscribeRequestBody.md) | список вебхуков | 

## Example

```python
from avito_job.models.webhooks_subscription_result_list import WebhooksSubscriptionResultList

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSubscriptionResultList from a JSON string
webhooks_subscription_result_list_instance = WebhooksSubscriptionResultList.from_json(json)
# print the JSON string representation of the object
print(WebhooksSubscriptionResultList.to_json())

# convert the object into a dict
webhooks_subscription_result_list_dict = webhooks_subscription_result_list_instance.to_dict()
# create an instance of WebhooksSubscriptionResultList from a dict
webhooks_subscription_result_list_from_dict = WebhooksSubscriptionResultList.from_dict(webhooks_subscription_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


