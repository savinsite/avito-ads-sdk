# GetApplicationsByIdsResultAppliesInnerPrevalidation

Статус и результат превалидации кандидата

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**summary** | [**List[PrevalidationAnswer]**](PrevalidationAnswer.md) | Выжимка превалидации. Массив ответов на вопросы | [optional] 

## Example

```python
from avito_job.models.get_applications_by_ids_result_applies_inner_prevalidation import GetApplicationsByIdsResultAppliesInnerPrevalidation

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsByIdsResultAppliesInnerPrevalidation from a JSON string
get_applications_by_ids_result_applies_inner_prevalidation_instance = GetApplicationsByIdsResultAppliesInnerPrevalidation.from_json(json)
# print the JSON string representation of the object
print(GetApplicationsByIdsResultAppliesInnerPrevalidation.to_json())

# convert the object into a dict
get_applications_by_ids_result_applies_inner_prevalidation_dict = get_applications_by_ids_result_applies_inner_prevalidation_instance.to_dict()
# create an instance of GetApplicationsByIdsResultAppliesInnerPrevalidation from a dict
get_applications_by_ids_result_applies_inner_prevalidation_from_dict = GetApplicationsByIdsResultAppliesInnerPrevalidation.from_dict(get_applications_by_ids_result_applies_inner_prevalidation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


