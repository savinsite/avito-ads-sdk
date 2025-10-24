# SimplifiedVacancy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_details** | [**SimplifiedVacancyAddressDetails**](SimplifiedVacancyAddressDetails.md) |  | [optional] 
**business_area** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**profession** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from avito_job.models.simplified_vacancy import SimplifiedVacancy

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedVacancy from a JSON string
simplified_vacancy_instance = SimplifiedVacancy.from_json(json)
# print the JSON string representation of the object
print(SimplifiedVacancy.to_json())

# convert the object into a dict
simplified_vacancy_dict = simplified_vacancy_instance.to_dict()
# create an instance of SimplifiedVacancy from a dict
simplified_vacancy_from_dict = SimplifiedVacancy.from_dict(simplified_vacancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


