# GetApplicationsByIdsResultAppliesInnerPrice

Цена целевого действия (копейки)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | **int** | Цена целевого действия в бонусах (копейки) | 
**real** | **int** | Цена целевого действия в реальных деньгах (копейки) | 
**total** | **int** | Общая цена целевого действия (копейки) | 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_price import GetApplicationsByIdsResultAppliesInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerPrice from a JSON string
get_applications_by_ids_result_applies_inner_price_instance = GetApplicationsByIdsResultAppliesInnerPrice.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerPrice.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_price_dict = get_applications_by_ids_result_applies_inner_price_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerPrice from a dict
get_applications_by_ids_result_applies_inner_price_from_dict = GetApplicationsByIdsResultAppliesInnerPrice.from_dict(get_applications_by_ids_result_applies_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


