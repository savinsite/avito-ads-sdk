# ResumeContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.resume_contact import ResumeContact

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeContact from a JSON string
resume_contact_instance = ResumeContact.from_json(json)
# print the JSON string representation of the object
print(ResumeContact.to_json())

# convert the object into a dict
resume_contact_dict = resume_contact_instance.to_dict()
# create an instance of ResumeContact from a dict
resume_contact_from_dict = ResumeContact.from_dict(resume_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


