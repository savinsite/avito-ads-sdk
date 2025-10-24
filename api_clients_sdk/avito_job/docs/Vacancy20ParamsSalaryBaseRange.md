# Vacancy20ParamsSalaryBaseRange

Блок с размером оклада. Все поля опциональны и выводятся при наличии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Нижняя граница оклада. Выводится при наличии | [optional] 
**to** | **int** | Верхняя граница оклада. Выводится при наличии | [optional] 

## Example

```python
from avito_job.models.vacancy20_params_salary_base_range import Vacancy20ParamsSalaryBaseRange

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20ParamsSalaryBaseRange from a JSON string
vacancy20_params_salary_base_range_instance = Vacancy20ParamsSalaryBaseRange.from_json(json)
# print the JSON string representation of the object
print(Vacancy20ParamsSalaryBaseRange.to_json())

# convert the object into a dict
vacancy20_params_salary_base_range_dict = vacancy20_params_salary_base_range_instance.to_dict()
# create an instance of Vacancy20ParamsSalaryBaseRange from a dict
vacancy20_params_salary_base_range_from_dict = Vacancy20ParamsSalaryBaseRange.from_dict(vacancy20_params_salary_base_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


