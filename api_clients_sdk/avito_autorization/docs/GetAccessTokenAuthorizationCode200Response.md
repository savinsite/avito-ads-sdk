# GetAccessTokenAuthorizationCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Ключ для временной авторизации в системе | [optional] 
**expires_in** | **float** | Время жизни ключа в секундах | [optional] 
**refresh_token** | **str** | Ключ для обновления токена доступа | [optional] 
**scope** | **str** | Полученный скоуп | [optional] 
**token_type** | **str** | Тип ключа авторизации | [optional] 

## Example

```python
from avito_autorization.models.get_access_token_authorization_code200_response import GetAccessTokenAuthorizationCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessTokenAuthorizationCode200Response from a JSON string
get_access_token_authorization_code200_response_instance = GetAccessTokenAuthorizationCode200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccessTokenAuthorizationCode200Response.to_json())

# convert the object into a dict
get_access_token_authorization_code200_response_dict = get_access_token_authorization_code200_response_instance.to_dict()
# create an instance of GetAccessTokenAuthorizationCode200Response from a dict
get_access_token_authorization_code200_response_from_dict = GetAccessTokenAuthorizationCode200Response.from_dict(get_access_token_authorization_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


