# UpdatePriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**UpdatePriceResponseResult**](UpdatePriceResponseResult.md) |  | 

## Example

```python
from avito_ads.models.update_price_response import UpdatePriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePriceResponse from a JSON string
update_price_response_instance = UpdatePriceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePriceResponse.to_json())

# convert the object into a dict
update_price_response_dict = update_price_response_instance.to_dict()
# create an instance of UpdatePriceResponse from a dict
update_price_response_from_dict = UpdatePriceResponse.from_dict(update_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


