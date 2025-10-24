# VacancyStatusesResultInnerLastAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **str** | Время события | [optional] 
**error** | [**VacancyStatusesResultInnerLastActionError**](VacancyStatusesResultInnerLastActionError.md) |  | [optional] 
**status** | **str** | Статус процесса публикации вакансии | [optional] 

## Example

```python
from avito_job.models.vacancy_statuses_result_inner_last_action import VacancyStatusesResultInnerLastAction

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyStatusesResultInnerLastAction from a JSON string
vacancy_statuses_result_inner_last_action_instance = VacancyStatusesResultInnerLastAction.from_json(json)
# print the JSON string representation of the object
print(VacancyStatusesResultInnerLastAction.to_json())

# convert the object into a dict
vacancy_statuses_result_inner_last_action_dict = vacancy_statuses_result_inner_last_action_instance.to_dict()
# create an instance of VacancyStatusesResultInnerLastAction from a dict
vacancy_statuses_result_inner_last_action_from_dict = VacancyStatusesResultInnerLastAction.from_dict(vacancy_statuses_result_inner_last_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


