# RefreshAccessTokenAuthorizationCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Новый ключ для временной авторизации в системе | [optional] 
**expires_in** | **float** | Время жизни ключа в секундах | [optional] 
**refresh_token** | **str** | Новый ключ для обновления токена доступа | [optional] 
**scope** | **str** | Полученный скоуп | [optional] 
**token_type** | **str** | Тип ключа авторизации | [optional] 

## Example

```python
from avito_autorization.models.refresh_access_token_authorization_code200_response import RefreshAccessTokenAuthorizationCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshAccessTokenAuthorizationCode200Response from a JSON string
refresh_access_token_authorization_code200_response_instance = RefreshAccessTokenAuthorizationCode200Response.from_json(json)
# print the JSON string representation of the object
print(RefreshAccessTokenAuthorizationCode200Response.to_json())

# convert the object into a dict
refresh_access_token_authorization_code200_response_dict = refresh_access_token_authorization_code200_response_instance.to_dict()
# create an instance of RefreshAccessTokenAuthorizationCode200Response from a dict
refresh_access_token_authorization_code200_response_from_dict = RefreshAccessTokenAuthorizationCode200Response.from_dict(refresh_access_token_authorization_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


