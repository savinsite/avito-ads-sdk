# Resume20ParamsLanguageListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Язык | [optional] 
**language_level** | **str** | Уровень владения языком | [optional] 

## Example

```python
from avito_job.models.resume20_params_language_list_inner import Resume20ParamsLanguageListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Resume20ParamsLanguageListInner from a JSON string
resume20_params_language_list_inner_instance = Resume20ParamsLanguageListInner.from_json(json)
# print the JSON string representation of the object
print(Resume20ParamsLanguageListInner.to_json())

# convert the object into a dict
resume20_params_language_list_inner_dict = resume20_params_language_list_inner_instance.to_dict()
# create an instance of Resume20ParamsLanguageListInner from a dict
resume20_params_language_list_inner_from_dict = Resume20ParamsLanguageListInner.from_dict(resume20_params_language_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


