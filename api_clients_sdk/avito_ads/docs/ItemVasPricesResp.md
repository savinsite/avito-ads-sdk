# ItemVasPricesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Идентификатор объявления на сайте | [optional] 
**stickers** | [**List[StickerResp]**](StickerResp.md) |  | [optional] 
**vas** | [**List[VasResp]**](VasResp.md) |  | 

## Example

```python
from avito_ads.models.item_vas_prices_resp import ItemVasPricesResp

# TODO update the JSON string below
json = "{}"
# create an instance of ItemVasPricesResp from a JSON string
item_vas_prices_resp_instance = ItemVasPricesResp.from_json(json)
# print the JSON string representation of the object
print(ItemVasPricesResp.to_json())

# convert the object into a dict
item_vas_prices_resp_dict = item_vas_prices_resp_instance.to_dict()
# create an instance of ItemVasPricesResp from a dict
item_vas_prices_resp_from_dict = ItemVasPricesResp.from_dict(item_vas_prices_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


