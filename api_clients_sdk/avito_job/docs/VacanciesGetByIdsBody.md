# VacanciesGetByIdsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** | Поля для основного тела ответа | [optional] 
**ids** | **List[int]** | Идентификаторы вакансий на сайте | 
**params** | **List[str]** | Дополнительные поля, которые входят в params (можно указать несколько значений через запятую). По умолчанию отображаются все поля. deprecated значения manufacturing_type, industry_type, programs, warehouse_functionality | [optional] 

## Example

```python
from avito_job.models.vacancies_get_by_ids_body import VacanciesGetByIdsBody

# TODO update the JSON string below
json = "{}"
# create an instance of VacanciesGetByIdsBody from a JSON string
vacancies_get_by_ids_body_instance = VacanciesGetByIdsBody.from_json(json)
# print the JSON string representation of the object
print(VacanciesGetByIdsBody.to_json())

# convert the object into a dict
vacancies_get_by_ids_body_dict = vacancies_get_by_ids_body_instance.to_dict()
# create an instance of VacanciesGetByIdsBody from a dict
vacancies_get_by_ids_body_from_dict = VacanciesGetByIdsBody.from_dict(vacancies_get_by_ids_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


