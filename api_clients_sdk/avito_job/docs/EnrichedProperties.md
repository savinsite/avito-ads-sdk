# EnrichedProperties

Данные о кандидате

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | [**EnrichedPropertiesAge**](EnrichedPropertiesAge.md) |  | [optional] 
**citizenship** | [**EnrichedPropertiesCitizenship**](EnrichedPropertiesCitizenship.md) |  | [optional] 
**experience** | [**EnrichedPropertiesExperience**](EnrichedPropertiesExperience.md) |  | [optional] 
**full_name** | [**EnrichedPropertiesFullName**](EnrichedPropertiesFullName.md) |  | [optional] 
**gender** | [**EnrichedPropertiesGender**](EnrichedPropertiesGender.md) |  | [optional] 
**phone** | [**EnrichedPropertiesPhone**](EnrichedPropertiesPhone.md) |  | [optional] 
**status** | **str** | Текущий статус опроса. Возможные значения:&lt;br/&gt;  - &#x60;\&quot;in_progress\&quot;&#x60; - кандидат еще проходит опрос&lt;br/&gt;  - &#x60;\&quot;not_completed\&quot;&#x60; - кандидату не удалось пройти опрос до конца (например, истекло время на опрос)&lt;br/&gt;  - &#x60;\&quot;completed_no_criteria\&quot;&#x60; - опрос завершен без оценки ответов по критериям вакансии&lt;br/&gt;  - &#x60;\&quot;completed_matched\&quot;&#x60; - опрос завершен, кандидат подошел под критерии вакансии&lt;br/&gt;  - &#x60;\&quot;completed_mismatched\&quot;&#x60; - опрос завершен, кандидат не подошел под критерии вакансии | [optional] 

## Example

```python
from avito_job.models.enriched_properties import EnrichedProperties

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedProperties from a JSON string
enriched_properties_instance = EnrichedProperties.from_json(json)
# print the JSON string representation of the object
print(EnrichedProperties.to_json())

# convert the object into a dict
enriched_properties_dict = enriched_properties_instance.to_dict()
# create an instance of EnrichedProperties from a dict
enriched_properties_from_dict = EnrichedProperties.from_dict(enriched_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


