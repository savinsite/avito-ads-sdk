# VacancyStatusesResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор публикации вакансии в формате UUID | [optional] 
**last_action** | [**VacancyStatusesResultInnerLastAction**](VacancyStatusesResultInnerLastAction.md) |  | [optional] 
**vacancy** | [**VacancyStatusesResultInnerVacancy**](VacancyStatusesResultInnerVacancy.md) |  | [optional] 

## Example

```python
from avito_job.models.vacancy_statuses_result_inner import VacancyStatusesResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyStatusesResultInner from a JSON string
vacancy_statuses_result_inner_instance = VacancyStatusesResultInner.from_json(json)
# print the JSON string representation of the object
print(VacancyStatusesResultInner.to_json())

# convert the object into a dict
vacancy_statuses_result_inner_dict = vacancy_statuses_result_inner_instance.to_dict()
# create an instance of VacancyStatusesResultInner from a dict
vacancy_statuses_result_inner_from_dict = VacancyStatusesResultInner.from_dict(vacancy_statuses_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


