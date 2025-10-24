# EnrichedPropertiesGender

Пол. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **str** | Возможные значения:&lt;br/&gt;  - &#x60;\&quot;male\&quot;&#x60; - мужской&lt;br/&gt;  - &#x60;\&quot;female\&quot;&#x60; - женский&lt;br/&gt; Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_gender import EnrichedPropertiesGender

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesGender from a JSON string
enriched_properties_gender_instance = EnrichedPropertiesGender.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesGender.to_json())

# convert the object into a dict
enriched_properties_gender_dict = enriched_properties_gender_instance.to_dict()
# create an instance of EnrichedPropertiesGender from a dict
enriched_properties_gender_from_dict = EnrichedPropertiesGender.from_dict(enriched_properties_gender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


