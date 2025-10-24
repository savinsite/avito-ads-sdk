# BadRequestOnVacancy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 

## Example

```python
from avito_job.models.bad_request_on_vacancy import BadRequestOnVacancy

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestOnVacancy from a JSON string
bad_request_on_vacancy_instance = BadRequestOnVacancy.from_json(json)
# print the JSON string representation of the object
print(BadRequestOnVacancy.to_json())

# convert the object into a dict
bad_request_on_vacancy_dict = bad_request_on_vacancy_instance.to_dict()
# create an instance of BadRequestOnVacancy from a dict
bad_request_on_vacancy_from_dict = BadRequestOnVacancy.from_dict(bad_request_on_vacancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


