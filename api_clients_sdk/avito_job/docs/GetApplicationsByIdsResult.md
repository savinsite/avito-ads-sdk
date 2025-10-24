# GetApplicationsByIdsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies** | [**List[GetApplicationsByIdsResultAppliesInner]**](GetApplicationsByIdsResultAppliesInner.md) | Список откликов | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result import GetApplicationsByIdsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResult from a JSON string
get_applications_by_ids_result_instance = GetApplicationsByIdsResult.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResult.to_json())

# convert the object into a dict
get_applications_by_ids_result_dict = get_applications_by_ids_result_instance.to_dict()
# create an instance of GetApplicationsByIdsResult from a dict
get_applications_by_ids_result_from_dict = GetApplicationsByIdsResult.from_dict(get_applications_by_ids_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


