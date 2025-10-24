# ApplicationsGetByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from avito_job.models.applications_get_by_ids_request import ApplicationsGetByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsGetByIdsRequest from a JSON string
applications_get_by_ids_request_instance = ApplicationsGetByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationsGetByIdsRequest.to_json())

# convert the object into a dict
applications_get_by_ids_request_dict = applications_get_by_ids_request_instance.to_dict()
# create an instance of ApplicationsGetByIdsRequest from a dict
applications_get_by_ids_request_from_dict = ApplicationsGetByIdsRequest.from_dict(applications_get_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


