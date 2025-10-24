# EnrichedPropertiesAge

Возраст. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **int** | Целое число, полное количество лет кандидата. Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_age import EnrichedPropertiesAge

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesAge from a JSON string
enriched_properties_age_instance = EnrichedPropertiesAge.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesAge.to_json())

# convert the object into a dict
enriched_properties_age_dict = enriched_properties_age_instance.to_dict()
# create an instance of EnrichedPropertiesAge from a dict
enriched_properties_age_from_dict = EnrichedPropertiesAge.from_dict(enriched_properties_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


