# VacancyArchive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **int** | employee_id - Идентификатор сотрудника на Авито. Сотрудник может останавливать только закрепленные за ним вакансии в Avito Pro. Сотрудник должен быть в активен.  | [optional] 

## Example

```python
from avito_job.models.vacancy_archive import VacancyArchive

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyArchive from a JSON string
vacancy_archive_instance = VacancyArchive.from_json(json)
# print the JSON string representation of the object
print(VacancyArchive.to_json())

# convert the object into a dict
vacancy_archive_dict = vacancy_archive_instance.to_dict()
# create an instance of VacancyArchive from a dict
vacancy_archive_from_dict = VacancyArchive.from_dict(vacancy_archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


