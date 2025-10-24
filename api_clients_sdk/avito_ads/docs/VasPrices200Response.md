# VasPrices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AuthErrorError**](AuthErrorError.md) |  | [optional] 

## Example

```python
from avito_ads.models.vas_prices200_response import VasPrices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VasPrices200Response from a JSON string
vas_prices200_response_instance = VasPrices200Response.from_json(json)
# print the JSON string representation of the object
print(VasPrices200Response.to_json())

# convert the object into a dict
vas_prices200_response_dict = vas_prices200_response_instance.to_dict()
# create an instance of VasPrices200Response from a dict
vas_prices200_response_from_dict = VasPrices200Response.from_dict(vas_prices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


