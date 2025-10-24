# VacancyStatusesResultInnerVacancy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор опубликованной вакансии на Авито | [optional] 
**moderation_status** | **str** | Статус модерации вакансии на Авито. Может отсутствовать, если процесс модерации вакансии еще не начался &lt;br&gt; Возможные значения:    - in_progress - вакансия в процессе модерации   - allowed - вакансия разрешена на модерации   - blocked - вакансия заблокирована на модерации   - rejected - вакансия отклонена на модерации  | [optional] 
**reasons** | **object** | Расширенное описание статуса | [optional] 
**status** | **str** | Статус вакансии на Авито | [optional] 
**url** | **str** | URL вакансии | [optional] 

## Example

```python
from avito_job.models.vacancy_statuses_result_inner_vacancy import VacancyStatusesResultInnerVacancy

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyStatusesResultInnerVacancy from a JSON string
vacancy_statuses_result_inner_vacancy_instance = VacancyStatusesResultInnerVacancy.from_json(json)
# print the JSON string representation of the object
print(VacancyStatusesResultInnerVacancy.to_json())

# convert the object into a dict
vacancy_statuses_result_inner_vacancy_dict = vacancy_statuses_result_inner_vacancy_instance.to_dict()
# create an instance of VacancyStatusesResultInnerVacancy from a dict
vacancy_statuses_result_inner_vacancy_from_dict = VacancyStatusesResultInnerVacancy.from_dict(vacancy_statuses_result_inner_vacancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


