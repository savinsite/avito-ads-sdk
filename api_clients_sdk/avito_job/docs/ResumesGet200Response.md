# ResumesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResumeSearchMeta**](ResumeSearchMeta.md) |  | [optional] 
**resumes** | [**List[SimplifiedResume]**](SimplifiedResume.md) |  | [optional] 

## Example

```python
from avito_job.models.resumes_get200_response import ResumesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ResumesGet200Response from a JSON string
resumes_get200_response_instance = ResumesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ResumesGet200Response.to_json())

# convert the object into a dict
resumes_get200_response_dict = resumes_get200_response_instance.to_dict()
# create an instance of ResumesGet200Response from a dict
resumes_get200_response_from_dict = ResumesGet200Response.from_dict(resumes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


