# VacancyV2CreateHierarchy

employee_id - Идентификатор сотрудника на Авито. Если этот параметр указан, то с баланса сотрудника в Avito Pro будет списано размещение. Использовать параметр можно только с billing_type равным package. Сотрудник должен быть в активен. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | Идентификатор сотрудника на Авито | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create_hierarchy import VacancyV2CreateHierarchy

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2CreateHierarchy from a JSON string
vacancy_v2_create_hierarchy_instance = VacancyV2CreateHierarchy.from_json(json)
# print the JSON string representation of the object
print(VacancyV2CreateHierarchy.to_json())

# convert the object into a dict
vacancy_v2_create_hierarchy_dict = vacancy_v2_create_hierarchy_instance.to_dict()
# create an instance of VacancyV2CreateHierarchy from a dict
vacancy_v2_create_hierarchy_from_dict = VacancyV2CreateHierarchy.from_dict(vacancy_v2_create_hierarchy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


