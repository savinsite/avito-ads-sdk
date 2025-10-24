# VacancyUpdateSalaryRange

Блок с вилкой зарплаты, если заполнен одновременно с salary, то имеет приоритет

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Нижняя граница зарплаты, рублей в месяц | [optional] 
**to** | **int** | Верхняя граница зарплаты, рублей в месяц | [optional] 

## Example

```python
from avito_job.models.vacancy_update_salary_range import VacancyUpdateSalaryRange

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyUpdateSalaryRange from a JSON string
vacancy_update_salary_range_instance = VacancyUpdateSalaryRange.from_json(json)
# print the JSON string representation of the object
print(VacancyUpdateSalaryRange.to_json())

# convert the object into a dict
vacancy_update_salary_range_dict = vacancy_update_salary_range_instance.to_dict()
# create an instance of VacancyUpdateSalaryRange from a dict
vacancy_update_salary_range_from_dict = VacancyUpdateSalaryRange.from_dict(vacancy_update_salary_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


