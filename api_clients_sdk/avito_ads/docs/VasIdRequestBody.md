# VasIdRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vas_id** | **str** | Идентификатор услуги, возможные его варианты значения: - &#x60;highlight&#x60; — [выделение объявления](https://support.avito.ru/articles/200026858) - &#x60;xl&#x60; – [XL-объявление](https://support.avito.ru/articles/685)  | 

## Example

```python
from avito_ads.models.vas_id_request_body import VasIdRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of VasIdRequestBody from a JSON string
vas_id_request_body_instance = VasIdRequestBody.from_json(json)
# print the JSON string representation of the object
print(VasIdRequestBody.to_json())

# convert the object into a dict
vas_id_request_body_dict = vas_id_request_body_instance.to_dict()
# create an instance of VasIdRequestBody from a dict
vas_id_request_body_from_dict = VasIdRequestBody.from_dict(vas_id_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


