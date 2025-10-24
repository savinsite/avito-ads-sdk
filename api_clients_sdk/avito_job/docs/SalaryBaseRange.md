# SalaryBaseRange

Размер оклада. Оклад не может превышать заработную плату. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Нижняя граница оклада, рублей за paid_period | [optional] 
**to** | **int** | Верхняя граница оклада, рублей за paid_period | [optional] 

## Example

```python
from avito_job.models.salary_base_range import SalaryBaseRange

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryBaseRange from a JSON string
salary_base_range_instance = SalaryBaseRange.from_json(json)
# print the JSON string representation of the object
print(SalaryBaseRange.to_json())

# convert the object into a dict
salary_base_range_dict = salary_base_range_instance.to_dict()
# create an instance of SalaryBaseRange from a dict
salary_base_range_from_dict = SalaryBaseRange.from_dict(salary_base_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


