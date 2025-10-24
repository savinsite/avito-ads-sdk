# Vacancy20ParamsCoordinates

Координаты адреса вакансии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Широта | [optional] 
**longitude** | **float** | Долгота | [optional] 

## Example

```python
from avito_job.models.vacancy20_params_coordinates import Vacancy20ParamsCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20ParamsCoordinates from a JSON string
vacancy20_params_coordinates_instance = Vacancy20ParamsCoordinates.from_json(json)
# print the JSON string representation of the object
print(Vacancy20ParamsCoordinates.to_json())

# convert the object into a dict
vacancy20_params_coordinates_dict = vacancy20_params_coordinates_instance.to_dict()
# create an instance of Vacancy20ParamsCoordinates from a dict
vacancy20_params_coordinates_from_dict = Vacancy20ParamsCoordinates.from_dict(vacancy20_params_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


