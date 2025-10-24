# Vacancy20


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_details** | [**Vacancy20AddressDetails**](Vacancy20AddressDetails.md) |  | [optional] 
**description** | **str** | Описание вакансии | [optional] 
**id** | **int** | Идентификатор вакансии на сайте | [optional] 
**is_active** | **bool** | Активность вакансии | [optional] 
**params** | [**Vacancy20Params**](Vacancy20Params.md) |  | [optional] 
**salary** | **int** | Зарплата. Выводится при наличии | [optional] 
**start_time** | **str** | Дата публикации вакансии | [optional] 
**title** | **str** | Наименование вакансии | [optional] 
**update_time** | **str** | Дата последнего обновления вакансии | [optional] 
**url** | **str** | URL вакансии на сайте | [optional] 
**uuid** | **str** | Идентификатор вакансии | [optional] 

## Example

```python
from avito_job.models.vacancy20 import Vacancy20

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20 from a JSON string
vacancy20_instance = Vacancy20.from_json(json)
# print the JSON string representation of the object
print(Vacancy20.to_json())

# convert the object into a dict
vacancy20_dict = vacancy20_instance.to_dict()
# create an instance of Vacancy20 from a dict
vacancy20_from_dict = Vacancy20.from_dict(vacancy20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


