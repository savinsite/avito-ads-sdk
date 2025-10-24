# VacancyV2CreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор добавленной вакансии в формате UUID (в случае дубликата UUID не меняется). Используется для запросов в ручки: - [Получение статуса публикации вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyGetStatuses) - [Редактирование вакансии V2](https://developers.avito.ru/api-catalog/job/documentation#operation/vacancyUpdateV2)  | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create_result import VacancyV2CreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2CreateResult from a JSON string
vacancy_v2_create_result_instance = VacancyV2CreateResult.from_json(json)
# print the JSON string representation of the object
print(VacancyV2CreateResult.to_json())

# convert the object into a dict
vacancy_v2_create_result_dict = vacancy_v2_create_result_instance.to_dict()
# create an instance of VacancyV2CreateResult from a dict
vacancy_v2_create_result_from_dict = VacancyV2CreateResult.from_dict(vacancy_v2_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


