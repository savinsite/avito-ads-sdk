# GetApplicationsIdsResultAppliesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Дата создания отклика | [optional] 
**id** | **str** | Идентификатор отклика | [optional] 
**updated_at** | **str** | Дата обновления отклика | [optional] 

## Example

```python
from avito_job.models.get_applications_ids_result_applies_inner import GetApplicationsIdsResultAppliesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsIdsResultAppliesInner from a JSON string
get_applications_ids_result_applies_inner_instance = GetApplicationsIdsResultAppliesInner.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsIdsResultAppliesInner.to_json())

# convert the object into a dict
get_applications_ids_result_applies_inner_dict = get_applications_ids_result_applies_inner_instance.to_dict()
# create an instance of GetApplicationsIdsResultAppliesInner from a dict
get_applications_ids_result_applies_inner_from_dict = GetApplicationsIdsResultAppliesInner.from_dict(get_applications_ids_result_applies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


