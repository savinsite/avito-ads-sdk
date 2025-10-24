# VacancyCreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор добавленной вакансии на сайте. | [optional] 
**url** | **str** | URL добавленной вакансии. | [optional] 
**uuid** | **str** | Идентификатор добавленной вакансии. | [optional] 

## Example

```python
from avito_job.models.vacancy_create_result import VacancyCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyCreateResult from a JSON string
vacancy_create_result_instance = VacancyCreateResult.from_json(json)
# print the JSON string representation of the object
print(VacancyCreateResult.to_json())

# convert the object into a dict
vacancy_create_result_dict = vacancy_create_result_instance.to_dict()
# create an instance of VacancyCreateResult from a dict
vacancy_create_result_from_dict = VacancyCreateResult.from_dict(vacancy_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


