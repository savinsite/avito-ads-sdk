# VacancyV2CreateSalary

Блок с вилкой зарплаты

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Нижняя граница зарплаты, рублей в месяц | [optional] 
**to** | **int** | Верхняя граница зарплаты, рублей в месяц | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create_salary import VacancyV2CreateSalary

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2CreateSalary from a JSON string
vacancy_v2_create_salary_instance = VacancyV2CreateSalary.from_json(json)
# print the JSON string representation of the object
print(VacancyV2CreateSalary.to_json())

# convert the object into a dict
vacancy_v2_create_salary_dict = vacancy_v2_create_salary_instance.to_dict()
# create an instance of VacancyV2CreateSalary from a dict
vacancy_v2_create_salary_from_dict = VacancyV2CreateSalary.from_dict(vacancy_v2_create_salary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


