# Resume20ParamsEducationListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**education_stop** | **str** | Дата окончания учебного заведения | [optional] 
**institution** | **str** | Наименование учебного заведения | [optional] 
**specialty** | **str** | Специальность | [optional] 

## Example

```python
from avito_job.models.resume20_params_education_list_inner import Resume20ParamsEducationListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Resume20ParamsEducationListInner from a JSON string
resume20_params_education_list_inner_instance = Resume20ParamsEducationListInner.from_json(json)
# print the JSON string representation of the object
print(Resume20ParamsEducationListInner.to_json())

# convert the object into a dict
resume20_params_education_list_inner_dict = resume20_params_education_list_inner_instance.to_dict()
# create an instance of Resume20ParamsEducationListInner from a dict
resume20_params_education_list_inner_from_dict = Resume20ParamsEducationListInner.from_dict(resume20_params_education_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


