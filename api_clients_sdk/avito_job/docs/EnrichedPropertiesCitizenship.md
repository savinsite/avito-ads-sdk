# EnrichedPropertiesCitizenship

Гражданство. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **str** | Код страны в стандартной кодировке ISO 3166-1 alpha-3. Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_citizenship import EnrichedPropertiesCitizenship

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesCitizenship from a JSON string
enriched_properties_citizenship_instance = EnrichedPropertiesCitizenship.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesCitizenship.to_json())

# convert the object into a dict
enriched_properties_citizenship_dict = enriched_properties_citizenship_instance.to_dict()
# create an instance of EnrichedPropertiesCitizenship from a dict
enriched_properties_citizenship_from_dict = EnrichedPropertiesCitizenship.from_dict(enriched_properties_citizenship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


