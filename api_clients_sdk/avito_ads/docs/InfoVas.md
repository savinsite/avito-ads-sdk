# InfoVas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_time** | **datetime** | Дата завершения услуги | [optional] 
**schedule** | **List[datetime]** | Информация о следующих применениях услуги | [optional] 
**vas_id** | **str** | Идентификатор услуги | [optional] 

## Example

```python
from avito_ads.models.info_vas import InfoVas

# TODO update the JSON string below
json = "{}"
# create an instance of InfoVas from a JSON string
info_vas_instance = InfoVas.from_json(json)
# print the JSON string representation of the object
print(InfoVas.to_json())

# convert the object into a dict
info_vas_dict = info_vas_instance.to_dict()
# create an instance of InfoVas from a dict
info_vas_from_dict = InfoVas.from_dict(info_vas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


