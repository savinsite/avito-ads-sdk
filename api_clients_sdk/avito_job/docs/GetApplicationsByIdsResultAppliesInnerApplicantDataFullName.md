# GetApplicationsByIdsResultAppliesInnerApplicantDataFullName

Детали ФИО

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Имя | [optional] 
**last_name** | **str** | Фамилия | [optional] 
**patronymic** | **str** | Отчество, если указано | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_applicant_data_full_name import GetApplicationsByIdsResultAppliesInnerApplicantDataFullName

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicantDataFullName from a JSON string
get_applications_by_ids_result_applies_inner_applicant_data_full_name_instance = GetApplicationsByIdsResultAppliesInnerApplicantDataFullName.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerApplicantDataFullName.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_applicant_data_full_name_dict = get_applications_by_ids_result_applies_inner_applicant_data_full_name_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerApplicantDataFullName from a dict
get_applications_by_ids_result_applies_inner_applicant_data_full_name_from_dict = GetApplicationsByIdsResultAppliesInnerApplicantDataFullName.from_dict(get_applications_by_ids_result_applies_inner_applicant_data_full_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


