# VasResp

Информация об услугах и пакетах дополнительных услуг для переданного списка объявлений

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** | Цена со скидкой | 
**price_old** | **int** | Цена до применения скидки | 
**slug** | **str** | Идентификатор услуги или пакета услуг | 

## Example

```python
from avito_ads.models.vas_resp import VasResp

# TODO update the JSON string below
json = "{}"
# create an instance of VasResp from a JSON string
vas_resp_instance = VasResp.from_json(json)
# print the JSON string representation of the object
print(VasResp.to_json())

# convert the object into a dict
vas_resp_dict = vas_resp_instance.to_dict()
# create an instance of VasResp from a dict
vas_resp_from_dict = VasResp.from_dict(vas_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


