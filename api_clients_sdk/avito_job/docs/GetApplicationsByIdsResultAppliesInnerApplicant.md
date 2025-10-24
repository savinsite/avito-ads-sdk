# GetApplicationsByIdsResultAppliesInnerApplicant

Данные соискателя

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetApplicationsByIdsResultAppliesInnerApplicantData**](GetApplicationsByIdsResultAppliesInnerApplicantData.md) |  | [optional] 
**id** | **str** |  | [optional] 
**resume_id** | **str** |  | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_applicant import GetApplicationsByIdsResultAppliesInnerApplicant

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicant from a JSON string
get_applications_by_ids_result_applies_inner_applicant_instance = GetApplicationsByIdsResultAppliesInnerApplicant.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerApplicant.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_applicant_dict = get_applications_by_ids_result_applies_inner_applicant_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicant from a dict
get_applications_by_ids_result_applies_inner_applicant_from_dict = GetApplicationsByIdsResultAppliesInnerApplicant.from_dict(get_applications_by_ids_result_applies_inner_applicant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


