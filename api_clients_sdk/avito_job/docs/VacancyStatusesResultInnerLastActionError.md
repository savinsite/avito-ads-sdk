# VacancyStatusesResultInnerLastActionError

Ошибка в процессе публикации вакансии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from avito_job.models.vacancy_statuses_result_inner_last_action_error import VacancyStatusesResultInnerLastActionError

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyStatusesResultInnerLastActionError from a JSON string
vacancy_statuses_result_inner_last_action_error_instance = VacancyStatusesResultInnerLastActionError.from_json(json)
# print the JSON string representation of the object
print(VacancyStatusesResultInnerLastActionError.to_json())

# convert the object into a dict
vacancy_statuses_result_inner_last_action_error_dict = vacancy_statuses_result_inner_last_action_error_instance.to_dict()
# create an instance of VacancyStatusesResultInnerLastActionError from a dict
vacancy_statuses_result_inner_last_action_error_from_dict = VacancyStatusesResultInnerLastActionError.from_dict(vacancy_statuses_result_inner_last_action_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


