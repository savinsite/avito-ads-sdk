# VacancyStatusesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from avito_job.models.vacancy_statuses_body import VacancyStatusesBody

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyStatusesBody from a JSON string
vacancy_statuses_body_instance = VacancyStatusesBody.from_json(json)
# print the JSON string representation of the object
print(VacancyStatusesBody.to_json())

# convert the object into a dict
vacancy_statuses_body_dict = vacancy_statuses_body_instance.to_dict()
# create an instance of VacancyStatusesBody from a dict
vacancy_statuses_body_from_dict = VacancyStatusesBody.from_dict(vacancy_statuses_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


