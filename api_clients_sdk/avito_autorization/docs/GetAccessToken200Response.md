# GetAccessToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Ключ для временной авторизации в системе | [optional] 
**expires_in** | **float** | Время жизни ключа в секундах | [optional] 
**token_type** | **str** | Тип ключа авторизации | [optional] 

## Example

```python
from avito_autorization.models.get_access_token200_response import GetAccessToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessToken200Response from a JSON string
get_access_token200_response_instance = GetAccessToken200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccessToken200Response.to_json())

# convert the object into a dict
get_access_token200_response_dict = get_access_token200_response_instance.to_dict()
# create an instance of GetAccessToken200Response from a dict
get_access_token200_response_from_dict = GetAccessToken200Response.from_dict(get_access_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


