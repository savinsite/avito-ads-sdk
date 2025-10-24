# Resume20ParamsExperienceListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | Наименование организации | [optional] 
**position** | **str** | Занимаемая должность | [optional] 
**responsibilities** | **str** | Должностные обязанности | [optional] 
**work_finish** | **date** | Дата увольнения (при отсутствии считать, что работает по настоящее время) | [optional] 
**work_start** | **date** | Дата приема на работу | [optional] 

## Example

```python
from avito_job.models.resume20_params_experience_list_inner import Resume20ParamsExperienceListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Resume20ParamsExperienceListInner from a JSON string
resume20_params_experience_list_inner_instance = Resume20ParamsExperienceListInner.from_json(json)
# print the JSON string representation of the object
print(Resume20ParamsExperienceListInner.to_json())

# convert the object into a dict
resume20_params_experience_list_inner_dict = resume20_params_experience_list_inner_instance.to_dict()
# create an instance of Resume20ParamsExperienceListInner from a dict
resume20_params_experience_list_inner_from_dict = Resume20ParamsExperienceListInner.from_dict(resume20_params_experience_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


