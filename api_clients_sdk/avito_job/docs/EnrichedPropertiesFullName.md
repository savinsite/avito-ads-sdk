# EnrichedPropertiesFullName

ФИО. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **str** | Строка со свободным вводом кандидата. Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_full_name import EnrichedPropertiesFullName

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesFullName from a JSON string
enriched_properties_full_name_instance = EnrichedPropertiesFullName.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesFullName.to_json())

# convert the object into a dict
enriched_properties_full_name_dict = enriched_properties_full_name_instance.to_dict()
# create an instance of EnrichedPropertiesFullName from a dict
enriched_properties_full_name_from_dict = EnrichedPropertiesFullName.from_dict(enriched_properties_full_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


