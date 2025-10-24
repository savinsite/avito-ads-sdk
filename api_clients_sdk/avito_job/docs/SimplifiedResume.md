# SimplifiedResume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**driver_licence** | [**DriverLicence**](DriverLicence.md) |  | [optional] 
**driver_licence_category** | **List[str]** |  | [optional] 
**driving_experience** | [**DrivingExperience**](DrivingExperience.md) |  | [optional] 
**education_level** | [**EducationLevel**](EducationLevel.md) |  | [optional] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**is_purchased** | **bool** |  | [optional] [readonly] 
**location** | [**Location**](Location.md) |  | [optional] 
**medical_book** | [**MedicalBook**](MedicalBook.md) |  | [optional] 
**nationality** | [**Citizenship**](Citizenship.md) |  | [optional] 
**own_transport** | [**OwnTransport**](OwnTransport.md) |  | [optional] 
**salary** | **float** |  | [optional] [readonly] 
**specialization** | [**Specialization**](Specialization.md) |  | [optional] 
**title** | **str** |  | [optional] [readonly] 
**total_experience** | **int** |  | [optional] [readonly] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from avito_job.models.simplified_resume import SimplifiedResume

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedResume from a JSON string
simplified_resume_instance = SimplifiedResume.from_json(json)
# print the JSON string representation of the object
print(SimplifiedResume.to_json())

# convert the object into a dict
simplified_resume_dict = simplified_resume_instance.to_dict()
# create an instance of SimplifiedResume from a dict
simplified_resume_from_dict = SimplifiedResume.from_dict(simplified_resume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


