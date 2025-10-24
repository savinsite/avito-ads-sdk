# VasAmountAvito


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Сумма списания за применение услуги или пакета | [optional] 

## Example

```python
from avito_ads.models.vas_amount_avito import VasAmountAvito

# TODO update the JSON string below
json = "{}"
# create an instance of VasAmountAvito from a JSON string
vas_amount_avito_instance = VasAmountAvito.from_json(json)
# print the JSON string representation of the object
print(VasAmountAvito.to_json())

# convert the object into a dict
vas_amount_avito_dict = vas_amount_avito_instance.to_dict()
# create an instance of VasAmountAvito from a dict
vas_amount_avito_from_dict = VasAmountAvito.from_dict(vas_amount_avito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


