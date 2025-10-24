# VasApplyAvito


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Сумма списания за применение услуги | [optional] 
**vas** | [**InfoVas**](InfoVas.md) |  | [optional] 

## Example

```python
from avito_ads.models.vas_apply_avito import VasApplyAvito

# TODO update the JSON string below
json = "{}"
# create an instance of VasApplyAvito from a JSON string
vas_apply_avito_instance = VasApplyAvito.from_json(json)
# print the JSON string representation of the object
print(VasApplyAvito.to_json())

# convert the object into a dict
vas_apply_avito_dict = vas_apply_avito_instance.to_dict()
# create an instance of VasApplyAvito from a dict
vas_apply_avito_from_dict = VasApplyAvito.from_dict(vas_apply_avito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


