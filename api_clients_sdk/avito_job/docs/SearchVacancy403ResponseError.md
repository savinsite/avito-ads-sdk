# SearchVacancy403ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | [optional] 
**message** | **str** | Текст ошибки | [optional] 

## Example

```python
from avito_job.models.search_vacancy403_response_error import SearchVacancy403ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVacancy403ResponseError from a JSON string
search_vacancy403_response_error_instance = SearchVacancy403ResponseError.from_json(json)
# print the JSON string representation of the object
print(SearchVacancy403ResponseError.to_json())

# convert the object into a dict
search_vacancy403_response_error_dict = search_vacancy403_response_error_instance.to_dict()
# create an instance of SearchVacancy403ResponseError from a dict
search_vacancy403_response_error_from_dict = SearchVacancy403ResponseError.from_dict(search_vacancy403_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


