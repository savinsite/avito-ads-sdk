# ApplicationsSetIsViewedRequestAppliesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отклика | 
**is_viewed** | **bool** | Фильтр откликов по статусу просмотренности | 

## Example

```python
from avito_job.models.applications_set_is_viewed_request_applies_inner import ApplicationsSetIsViewedRequestAppliesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsSetIsViewedRequestAppliesInner from a JSON string
applications_set_is_viewed_request_applies_inner_instance = ApplicationsSetIsViewedRequestAppliesInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationsSetIsViewedRequestAppliesInner.to_json())

# convert the object into a dict
applications_set_is_viewed_request_applies_inner_dict = applications_set_is_viewed_request_applies_inner_instance.to_dict()
# create an instance of ApplicationsSetIsViewedRequestAppliesInner from a dict
applications_set_is_viewed_request_applies_inner_from_dict = ApplicationsSetIsViewedRequestAppliesInner.from_dict(applications_set_is_viewed_request_applies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


