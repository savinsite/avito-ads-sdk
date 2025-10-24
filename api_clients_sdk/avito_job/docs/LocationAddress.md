# LocationAddress

Адрес объекта

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | Район области | [optional] 
**house** | **str** | Номер дома | [optional] 
**locality** | **str** | Населённый пункт | 
**province** | **str** | Область | [optional] 
**region** | **str** | Округ | [optional] 
**street** | **str** | Улица | [optional] 

## Example

```python
from avito_job.models.location_address import LocationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LocationAddress from a JSON string
location_address_instance = LocationAddress.from_json(json)
# print the JSON string representation of the object
print(LocationAddress.to_json())

# convert the object into a dict
location_address_dict = location_address_instance.to_dict()
# create an instance of LocationAddress from a dict
location_address_from_dict = LocationAddress.from_dict(location_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


