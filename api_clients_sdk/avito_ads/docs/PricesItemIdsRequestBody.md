# PricesItemIdsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[int]** | Набор идентификаторов объявлений на сайте | 

## Example

```python
from avito_ads.models.prices_item_ids_request_body import PricesItemIdsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of PricesItemIdsRequestBody from a JSON string
prices_item_ids_request_body_instance = PricesItemIdsRequestBody.from_json(json)
# print the JSON string representation of the object
print(PricesItemIdsRequestBody.to_json())

# convert the object into a dict
prices_item_ids_request_body_dict = prices_item_ids_request_body_instance.to_dict()
# create an instance of PricesItemIdsRequestBody from a dict
prices_item_ids_request_body_from_dict = PricesItemIdsRequestBody.from_dict(prices_item_ids_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


