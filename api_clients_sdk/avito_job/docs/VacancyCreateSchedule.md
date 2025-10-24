# VacancyCreateSchedule

Режим работы <br> Возможные значения:   - flyInFlyOut - Вахта   - fixed - Фиксированный   - flexible - Гибкий   - shift - Сменный  deprecated значения fiveDay, sixDay, partTime, fullDay и remote будут заменены на fixed flyInFlyOut - Вахта, при выборе данного режима работы, адрес вакансии может быть только \"Город\", если адрес передается полноценный, то улица будет отрезана и адрес будет до \"Города\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from avito_job.models.vacancy_create_schedule import VacancyCreateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyCreateSchedule from a JSON string
vacancy_create_schedule_instance = VacancyCreateSchedule.from_json(json)
# print the JSON string representation of the object
print(VacancyCreateSchedule.to_json())

# convert the object into a dict
vacancy_create_schedule_dict = vacancy_create_schedule_instance.to_dict()
# create an instance of VacancyCreateSchedule from a dict
vacancy_create_schedule_from_dict = VacancyCreateSchedule.from_dict(vacancy_create_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


