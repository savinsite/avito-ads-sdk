# Vacancy20AddressDetailsCoordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Широта | [optional] 
**longitude** | **float** | Долгота | [optional] 

## Example

```python
from avito_job.models.vacancy20_address_details_coordinates import Vacancy20AddressDetailsCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20AddressDetailsCoordinates from a JSON string
vacancy20_address_details_coordinates_instance = Vacancy20AddressDetailsCoordinates.from_json(json)
# print the JSON string representation of the object
print(Vacancy20AddressDetailsCoordinates.to_json())

# convert the object into a dict
vacancy20_address_details_coordinates_dict = vacancy20_address_details_coordinates_instance.to_dict()
# create an instance of Vacancy20AddressDetailsCoordinates from a dict
vacancy20_address_details_coordinates_from_dict = Vacancy20AddressDetailsCoordinates.from_dict(vacancy20_address_details_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


