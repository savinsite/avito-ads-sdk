# SimplifiedVacancyAddressDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 

## Example

```python
from avito_job.models.simplified_vacancy_address_details import SimplifiedVacancyAddressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedVacancyAddressDetails from a JSON string
simplified_vacancy_address_details_instance = SimplifiedVacancyAddressDetails.from_json(json)
# print the JSON string representation of the object
print(SimplifiedVacancyAddressDetails.to_json())

# convert the object into a dict
simplified_vacancy_address_details_dict = simplified_vacancy_address_details_instance.to_dict()
# create an instance of SimplifiedVacancyAddressDetails from a dict
simplified_vacancy_address_details_from_dict = SimplifiedVacancyAddressDetails.from_dict(simplified_vacancy_address_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


