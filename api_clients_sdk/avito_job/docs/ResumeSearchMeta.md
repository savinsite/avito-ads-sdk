# ResumeSearchMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **int** |  | [optional] [readonly] 
**page** | **int** |  | [optional] [readonly] 
**pages** | **int** |  | [optional] [readonly] 
**per_page** | **int** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.resume_search_meta import ResumeSearchMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeSearchMeta from a JSON string
resume_search_meta_instance = ResumeSearchMeta.from_json(json)
# print the JSON string representation of the object
print(ResumeSearchMeta.to_json())

# convert the object into a dict
resume_search_meta_dict = resume_search_meta_instance.to_dict()
# create an instance of ResumeSearchMeta from a dict
resume_search_meta_from_dict = ResumeSearchMeta.from_dict(resume_search_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


