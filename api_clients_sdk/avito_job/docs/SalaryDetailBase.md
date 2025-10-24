# SalaryDetailBase

Оклад

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | **str** | Премия. Не более 70 символов. | [optional] 
**range** | [**SalaryBaseRange**](SalaryBaseRange.md) |  | [optional] 

## Example

```python
from avito_job.models.salary_detail_base import SalaryDetailBase

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryDetailBase from a JSON string
salary_detail_base_instance = SalaryDetailBase.from_json(json)
# print the JSON string representation of the object
print(SalaryDetailBase.to_json())

# convert the object into a dict
salary_detail_base_dict = salary_detail_base_instance.to_dict()
# create an instance of SalaryDetailBase from a dict
salary_detail_base_from_dict = SalaryDetailBase.from_dict(salary_detail_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


