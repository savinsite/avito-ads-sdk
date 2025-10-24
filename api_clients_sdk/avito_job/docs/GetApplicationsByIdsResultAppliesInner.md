# GetApplicationsByIdsResultAppliesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicant** | [**GetApplicationsByIdsResultAppliesInnerApplicant**](GetApplicationsByIdsResultAppliesInnerApplicant.md) |  | [optional] 
**contacts** | [**GetApplicationsByIdsResultAppliesInnerContacts**](GetApplicationsByIdsResultAppliesInnerContacts.md) |  | [optional] 
**created_at** | **str** | Дата создания отклика | [optional] 
**employee_id** | **int** | Идентификатор сотрудника разместившего вакансию | [optional] 
**enriched_properties** | [**EnrichedProperties**](EnrichedProperties.md) |  | [optional] 
**id** | **str** | Идентификатор отклика | [optional] 
**is_viewed** | **bool** | Отклик просмотрен | [optional] 
**negotiation_id** | **int** | Идентификатор отклика старого формата | [optional] 
**prevalidation** | [**GetApplicationsByIdsResultAppliesInnerPrevalidation**](GetApplicationsByIdsResultAppliesInnerPrevalidation.md) |  | [optional] 
**price** | [**GetApplicationsByIdsResultAppliesInnerPrice**](GetApplicationsByIdsResultAppliesInnerPrice.md) |  | [optional] 
**type** | **str** | Тип отклика  Возможные значения:  - \&quot;by_phone\&quot; - отклик через просмотр телефона  - \&quot;by_chat\&quot; - отклик через чат  | [optional] 
**updated_at** | **str** | Дата обновления отклика | [optional] 
**vacancy_id** | **int** | Идентификатор вакансии на сайте Авито | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner import GetApplicationsByIdsResultAppliesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInner from a JSON string
get_applications_by_ids_result_applies_inner_instance = GetApplicationsByIdsResultAppliesInner.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInner.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_dict = get_applications_by_ids_result_applies_inner_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInner from a dict
get_applications_by_ids_result_applies_inner_from_dict = GetApplicationsByIdsResultAppliesInner.from_dict(get_applications_by_ids_result_applies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


