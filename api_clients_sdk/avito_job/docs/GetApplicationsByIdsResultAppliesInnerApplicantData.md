# GetApplicationsByIdsResultAppliesInnerApplicantData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **str** | Дата рождения | [optional] 
**citizenship** | **str** | Гражданство | [optional] 
**education** | [**EducationLevel**](EducationLevel.md) |  | [optional] 
**full_name** | [**GetApplicationsByIdsResultAppliesInnerApplicantDataFullName**](GetApplicationsByIdsResultAppliesInnerApplicantDataFullName.md) |  | [optional] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**name** | **str** | ФИО | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_applicant_data import GetApplicationsByIdsResultAppliesInnerApplicantData

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicantData from a JSON string
get_applications_by_ids_result_applies_inner_applicant_data_instance = GetApplicationsByIdsResultAppliesInnerApplicantData.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerApplicantData.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_applicant_data_dict = get_applications_by_ids_result_applies_inner_applicant_data_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicantData from a dict
get_applications_by_ids_result_applies_inner_applicant_data_from_dict = GetApplicationsByIdsResultAppliesInnerApplicantData.from_dict(get_applications_by_ids_result_applies_inner_applicant_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


