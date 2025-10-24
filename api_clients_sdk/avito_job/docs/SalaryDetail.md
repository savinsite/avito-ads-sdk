# SalaryDetail

Подробная информация по заработной плате

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**SalaryDetailBase**](SalaryDetailBase.md) |  | [optional] 
**paid_period** | [**PaidPeriod**](PaidPeriod.md) |  | [optional] 
**taxes** | [**Taxes**](Taxes.md) |  | [optional] 

## Example

```python
from avito_job.models.salary_detail import SalaryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryDetail from a JSON string
salary_detail_instance = SalaryDetail.from_json(json)
# print the JSON string representation of the object
print(SalaryDetail.to_json())

# convert the object into a dict
salary_detail_dict = salary_detail_instance.to_dict()
# create an instance of SalaryDetail from a dict
salary_detail_from_dict = SalaryDetail.from_dict(salary_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


