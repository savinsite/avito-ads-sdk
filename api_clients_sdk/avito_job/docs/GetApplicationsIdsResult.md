# GetApplicationsIdsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies** | [**List[GetApplicationsIdsResultAppliesInner]**](GetApplicationsIdsResultAppliesInner.md) | Список идентификаторов | [optional] 

## Example

```python
from avito_job.models.get_applications_ids_result import GetApplicationsIdsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsIdsResult from a JSON string
get_applications_ids_result_instance = GetApplicationsIdsResult.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsIdsResult.to_json())

# convert the object into a dict
get_applications_ids_result_dict = get_applications_ids_result_instance.to_dict()
# create an instance of GetApplicationsIdsResult from a dict
get_applications_ids_result_from_dict = GetApplicationsIdsResult.from_dict(get_applications_ids_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


