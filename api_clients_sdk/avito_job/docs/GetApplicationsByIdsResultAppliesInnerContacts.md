# GetApplicationsByIdsResultAppliesInnerContacts

Контакты соискателя

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**GetApplicationsByIdsResultAppliesInnerContactsChat**](GetApplicationsByIdsResultAppliesInnerContactsChat.md) |  | [optional] 
**phones** | [**List[GetApplicationsByIdsResultAppliesInnerContactsPhonesInner]**](GetApplicationsByIdsResultAppliesInnerContactsPhonesInner.md) |  | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_contacts import GetApplicationsByIdsResultAppliesInnerContacts

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerContacts from a JSON string
get_applications_by_ids_result_applies_inner_contacts_instance = GetApplicationsByIdsResultAppliesInnerContacts.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerContacts.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_contacts_dict = get_applications_by_ids_result_applies_inner_contacts_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerContacts from a dict
get_applications_by_ids_result_applies_inner_contacts_from_dict = GetApplicationsByIdsResultAppliesInnerContacts.from_dict(get_applications_by_ids_result_applies_inner_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


