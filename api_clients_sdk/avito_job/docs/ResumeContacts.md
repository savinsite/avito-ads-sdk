# ResumeContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**already_bought** | **bool** |  | [optional] [readonly] 
**contacts** | [**List[ResumeContact]**](ResumeContact.md) |  | [optional] [readonly] 
**full_name** | [**GetApplicationsByIdsResultAppliesInnerApplicantDataFullName**](GetApplicationsByIdsResultAppliesInnerApplicantDataFullName.md) |  | [optional] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.resume_contacts import ResumeContacts

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeContacts from a JSON string
resume_contacts_instance = ResumeContacts.from_json(json)
# print the JSON string representation of the object
print(ResumeContacts.to_json())

# convert the object into a dict
resume_contacts_dict = resume_contacts_instance.to_dict()
# create an instance of ResumeContacts from a dict
resume_contacts_from_dict = ResumeContacts.from_dict(resume_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


