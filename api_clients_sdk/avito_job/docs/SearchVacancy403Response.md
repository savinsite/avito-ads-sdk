# SearchVacancy403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SearchVacancy403ResponseError**](SearchVacancy403ResponseError.md) |  | [optional] 

## Example

```python
from avito_job.models.search_vacancy403_response import SearchVacancy403Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVacancy403Response from a JSON string
search_vacancy403_response_instance = SearchVacancy403Response.from_json(json)
# print the JSON string representation of the object
print(SearchVacancy403Response.to_json())

# convert the object into a dict
search_vacancy403_response_dict = search_vacancy403_response_instance.to_dict()
# create an instance of SearchVacancy403Response from a dict
search_vacancy403_response_from_dict = SearchVacancy403Response.from_dict(search_vacancy403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


