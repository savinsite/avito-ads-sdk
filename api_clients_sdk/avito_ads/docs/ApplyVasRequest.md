# ApplyVasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slugs** | **List[str]** | Список идентификаторов услуг | 
**stickers** | **List[int]** | Список значков | [optional] 

## Example

```python
from avito_ads.models.apply_vas_request import ApplyVasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyVasRequest from a JSON string
apply_vas_request_instance = ApplyVasRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyVasRequest.to_json())

# convert the object into a dict
apply_vas_request_dict = apply_vas_request_instance.to_dict()
# create an instance of ApplyVasRequest from a dict
apply_vas_request_from_dict = ApplyVasRequest.from_dict(apply_vas_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


