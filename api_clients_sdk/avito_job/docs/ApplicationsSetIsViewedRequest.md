# ApplicationsSetIsViewedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies** | [**List[ApplicationsSetIsViewedRequestAppliesInner]**](ApplicationsSetIsViewedRequestAppliesInner.md) | Список откликов | [optional] 

## Example

```python
from avito_job.models.applications_set_is_viewed_request import ApplicationsSetIsViewedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsSetIsViewedRequest from a JSON string
applications_set_is_viewed_request_instance = ApplicationsSetIsViewedRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationsSetIsViewedRequest.to_json())

# convert the object into a dict
applications_set_is_viewed_request_dict = applications_set_is_viewed_request_instance.to_dict()
# create an instance of ApplicationsSetIsViewedRequest from a dict
applications_set_is_viewed_request_from_dict = ApplicationsSetIsViewedRequest.from_dict(applications_set_is_viewed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


