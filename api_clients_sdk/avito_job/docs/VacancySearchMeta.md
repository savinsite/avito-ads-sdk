# VacancySearchMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [readonly] 
**pages** | **int** |  | [optional] [readonly] 
**per_page** | **int** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.vacancy_search_meta import VacancySearchMeta

# TODO update the JSON string below
json = "{}"
# create an instance of VacancySearchMeta from a JSON string
vacancy_search_meta_instance = VacancySearchMeta.from_json(json)
# print the JSON string representation of the object
print(VacancySearchMeta.to_json())

# convert the object into a dict
vacancy_search_meta_dict = vacancy_search_meta_instance.to_dict()
# create an instance of VacancySearchMeta from a dict
vacancy_search_meta_from_dict = VacancySearchMeta.from_dict(vacancy_search_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


