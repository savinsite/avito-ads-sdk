# SetApplicationsisVewedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies** | [**List[SetApplicationsisVewedResultAppliesInner]**](SetApplicationsisVewedResultAppliesInner.md) | Список идентификаторов откликов и статусов их просмотренности после обновления | [optional] 

## Example

```python
from avito_job.models.set_applicationsis_vewed_result import SetApplicationsisVewedResult

# TODO update the JSON string below
json = "{}"
# create an instance of SetApplicationsisVewedResult from a JSON string
set_applicationsis_vewed_result_instance = SetApplicationsisVewedResult.from_json(json)
# print the JSON string representation of the object
print(SetApplicationsisVewedResult.to_json())

# convert the object into a dict
set_applicationsis_vewed_result_dict = set_applicationsis_vewed_result_instance.to_dict()
# create an instance of SetApplicationsisVewedResult from a dict
set_applicationsis_vewed_result_from_dict = SetApplicationsisVewedResult.from_dict(set_applicationsis_vewed_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


