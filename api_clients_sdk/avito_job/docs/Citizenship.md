# Citizenship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.citizenship import Citizenship

# TODO update the JSON string below
json = "{}"
# create an instance of Citizenship from a JSON string
citizenship_instance = Citizenship.from_json(json)
# print the JSON string representation of the object
print(Citizenship.to_json())

# convert the object into a dict
citizenship_dict = citizenship_instance.to_dict()
# create an instance of Citizenship from a dict
citizenship_from_dict = Citizenship.from_dict(citizenship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


