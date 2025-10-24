# BadRequestShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**BadRequestShortError**](BadRequestShortError.md) |  | [optional] 

## Example

```python
from avito_job.models.bad_request_short import BadRequestShort

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestShort from a JSON string
bad_request_short_instance = BadRequestShort.from_json(json)
# print the JSON string representation of the object
print(BadRequestShort.to_json())

# convert the object into a dict
bad_request_short_dict = bad_request_short_instance.to_dict()
# create an instance of BadRequestShort from a dict
bad_request_short_from_dict = BadRequestShort.from_dict(bad_request_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


