# GetDicts200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Описание категории | [optional] 
**id** | **str** | Уникальный идентификатор категории | [optional] 

## Example

```python
from avito_job.models.get_dicts200_response_inner import GetDicts200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDicts200ResponseInner from a JSON string
get_dicts200_response_inner_instance = GetDicts200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetDicts200ResponseInner.to_json())

# convert the object into a dict
get_dicts200_response_inner_dict = get_dicts200_response_inner_instance.to_dict()
# create an instance of GetDicts200ResponseInner from a dict
get_dicts200_response_inner_from_dict = GetDicts200ResponseInner.from_dict(get_dicts200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


