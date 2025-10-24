# ItemIdsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[int]** | Набор идентификаторов объявлений на сайте | 

## Example

```python
from avito_ads.models.item_ids_request_body import ItemIdsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ItemIdsRequestBody from a JSON string
item_ids_request_body_instance = ItemIdsRequestBody.from_json(json)
# print the JSON string representation of the object
print(ItemIdsRequestBody.to_json())

# convert the object into a dict
item_ids_request_body_dict = item_ids_request_body_instance.to_dict()
# create an instance of ItemIdsRequestBody from a dict
item_ids_request_body_from_dict = ItemIdsRequestBody.from_dict(item_ids_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


