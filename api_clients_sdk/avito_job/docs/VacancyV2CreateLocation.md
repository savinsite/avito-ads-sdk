# VacancyV2CreateLocation

Геолокация вакансии (как минимум одно из значений)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**LocationAddress**](LocationAddress.md) |  | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create_location import VacancyV2CreateLocation

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2CreateLocation from a JSON string
vacancy_v2_create_location_instance = VacancyV2CreateLocation.from_json(json)
# print the JSON string representation of the object
print(VacancyV2CreateLocation.to_json())

# convert the object into a dict
vacancy_v2_create_location_dict = vacancy_v2_create_location_instance.to_dict()
# create an instance of VacancyV2CreateLocation from a dict
vacancy_v2_create_location_from_dict = VacancyV2CreateLocation.from_dict(vacancy_v2_create_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


