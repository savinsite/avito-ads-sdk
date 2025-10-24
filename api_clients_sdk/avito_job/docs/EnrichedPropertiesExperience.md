# EnrichedPropertiesExperience

Опыт по профессии. Пусто, если соискатель не оставил эти данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_status** | [**EnrichedPropertyMatchingStatus**](EnrichedPropertyMatchingStatus.md) |  | [optional] 
**value** | **str** | Возможные значения:&lt;br/&gt;  - &#x60;\&quot;0\&quot;&#x60; - нет опыта&lt;br/&gt;  - &#x60;\&quot;lt_1\&quot;&#x60; - меньше года&lt;br/&gt;  - &#x60;\&quot;1\&quot;&#x60;..&#x60;\&quot;50\&quot;&#x60; - значения от 1 до 50, опыт в количестве лет&lt;br/&gt;  - &#x60;\&quot;no_experience\&quot;&#x60; - нет опыта&lt;br/&gt;  - &#x60;\&quot;has_experience\&quot;&#x60; - есть опыта&lt;br/&gt; Пусто, если соискатель не оставил эти данные. | [optional] 

## Example

```python
from avito_job.models.enriched_properties_experience import EnrichedPropertiesExperience

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPropertiesExperience from a JSON string
enriched_properties_experience_instance = EnrichedPropertiesExperience.from_json(json)
# print the JSON string representation of the object
print(EnrichedPropertiesExperience.to_json())

# convert the object into a dict
enriched_properties_experience_dict = enriched_properties_experience_instance.to_dict()
# create an instance of EnrichedPropertiesExperience from a dict
enriched_properties_experience_from_dict = EnrichedPropertiesExperience.from_dict(enriched_properties_experience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


