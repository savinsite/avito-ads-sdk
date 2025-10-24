# VacancyAutoRenewal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renewal** | **bool** |  | [optional] 

## Example

```python
from avito_job.models.vacancy_auto_renewal import VacancyAutoRenewal

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyAutoRenewal from a JSON string
vacancy_auto_renewal_instance = VacancyAutoRenewal.from_json(json)
# print the JSON string representation of the object
print(VacancyAutoRenewal.to_json())

# convert the object into a dict
vacancy_auto_renewal_dict = vacancy_auto_renewal_instance.to_dict()
# create an instance of VacancyAutoRenewal from a dict
vacancy_auto_renewal_from_dict = VacancyAutoRenewal.from_dict(vacancy_auto_renewal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


