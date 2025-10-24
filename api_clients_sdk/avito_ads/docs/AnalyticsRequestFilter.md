# AnalyticsRequestFilter

Набор ограничений, по которым нужно отфильтровать данные

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_ids** | **List[int]** | Идентификаторы категорий&lt;/br&gt; [ Справочник идентификаторов категорий ](https://www.avito.st/s/openapi/catalog-categories.xml) | [optional] 
**employee_ids** | **List[int]** | Идентификаторы сотрудников&lt;/br&gt; [ Метод получения идентификаторов сотрудников ](https://developers.avito.ru/api-catalog/accounts-hierarchy/documentation#operation/getEmployeesV1) | [optional] 

## Example

```python
from avito_ads.models.analytics_request_filter import AnalyticsRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRequestFilter from a JSON string
analytics_request_filter_instance = AnalyticsRequestFilter.from_json(json)
# print the JSON string representation of the object
print(AnalyticsRequestFilter.to_json())

# convert the object into a dict
analytics_request_filter_dict = analytics_request_filter_instance.to_dict()
# create an instance of AnalyticsRequestFilter from a dict
analytics_request_filter_from_dict = AnalyticsRequestFilter.from_dict(analytics_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


