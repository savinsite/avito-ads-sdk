# Specialization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 

## Example

```python
from avito_job.models.specialization import Specialization

# TODO update the JSON string below
json = "{}"
# create an instance of Specialization from a JSON string
specialization_instance = Specialization.from_json(json)
# print the JSON string representation of the object
print(Specialization.to_json())

# convert the object into a dict
specialization_dict = specialization_instance.to_dict()
# create an instance of Specialization from a dict
specialization_from_dict = Specialization.from_dict(specialization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


