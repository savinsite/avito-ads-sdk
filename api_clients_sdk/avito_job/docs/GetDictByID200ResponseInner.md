# GetDictByID200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | Указывает, является ли значение устаревшим. Устаревшие значения могут использоваться только при чтении ранее созданных вакансий | [optional] 
**id** | **int** | Уникальный идентификатор | [optional] 
**name** | **str** | Название | [optional] 

## Example

```python
from avito_job.models.get_dict_by_id200_response_inner import GetDictByID200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictByID200ResponseInner from a JSON string
get_dict_by_id200_response_inner_instance = GetDictByID200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetDictByID200ResponseInner.to_json())

# convert the object into a dict
get_dict_by_id200_response_inner_dict = get_dict_by_id200_response_inner_instance.to_dict()
# create an instance of GetDictByID200ResponseInner from a dict
get_dict_by_id200_response_inner_from_dict = GetDictByID200ResponseInner.from_dict(get_dict_by_id200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


