# EnrichedPropertiesPhone

Номер телефона. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **str** | Номер телефона в формате +79211234455. Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_phone import EnrichedPropertiesPhone

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesPhone from a JSON string
enriched_properties_phone_instance = EnrichedPropertiesPhone.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesPhone.to_json())

# convert the object into a dict
enriched_properties_phone_dict = enriched_properties_phone_instance.to_dict()
# create an instance of EnrichedPropertiesPhone from a dict
enriched_properties_phone_from_dict = EnrichedPropertiesPhone.from_dict(enriched_properties_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


