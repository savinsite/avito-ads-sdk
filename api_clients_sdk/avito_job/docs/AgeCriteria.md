# AgeCriteria

Возраст кандидата.  Если выберите значения, в данных кандидата будет отметка, что кандидат соответствует этому критерию или нет.  Кандидаты не увидят этого в вакансии. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [optional] 
**to** | **int** |  | [optional] 

## Example

```python
from avito_job.models.age_criteria import AgeCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AgeCriteria from a JSON string
age_criteria_instance = AgeCriteria.from_json(json)
# print the JSON string representation of the object
print(AgeCriteria.to_json())

# convert the object into a dict
age_criteria_dict = age_criteria_instance.to_dict()
# create an instance of AgeCriteria from a dict
age_criteria_from_dict = AgeCriteria.from_dict(age_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


