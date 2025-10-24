# Vacancy20ParamsSalary

Блок с вилкой зарплаты. Все поля опциональны и выводятся при наличии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Нижняя граница зарплаты. Выводится при наличии | [optional] 
**to** | **int** | Верхняя граница зарплаты. Выводится при наличии | [optional] 

## Example

```python
from avito_job.models.vacancy20_params_salary import Vacancy20ParamsSalary

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20ParamsSalary from a JSON string
vacancy20_params_salary_instance = Vacancy20ParamsSalary.from_json(json)
# print the JSON string representation of the object
print(Vacancy20ParamsSalary.to_json())

# convert the object into a dict
vacancy20_params_salary_dict = vacancy20_params_salary_instance.to_dict()
# create an instance of Vacancy20ParamsSalary from a dict
vacancy20_params_salary_from_dict = Vacancy20ParamsSalary.from_dict(vacancy20_params_salary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


