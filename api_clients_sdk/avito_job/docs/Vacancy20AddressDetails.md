# Vacancy20AddressDetails

Детали адреса вакансии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Полный адрес | [optional] 
**city** | **str** | Город | [optional] 
**coordinates** | [**Vacancy20AddressDetailsCoordinates**](Vacancy20AddressDetailsCoordinates.md) |  | [optional] 
**province** | **str** | Область, например \&quot;Новосибирская область\&quot; или \&quot;Санкт-Петербург\&quot; для больших городов | [optional] 

## Example

```python
from avito_job.models.vacancy20_address_details import Vacancy20AddressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20AddressDetails from a JSON string
vacancy20_address_details_instance = Vacancy20AddressDetails.from_json(json)
# print the JSON string representation of the object
print(Vacancy20AddressDetails.to_json())

# convert the object into a dict
vacancy20_address_details_dict = vacancy20_address_details_instance.to_dict()
# create an instance of Vacancy20AddressDetails from a dict
vacancy20_address_details_from_dict = Vacancy20AddressDetails.from_dict(vacancy20_address_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


