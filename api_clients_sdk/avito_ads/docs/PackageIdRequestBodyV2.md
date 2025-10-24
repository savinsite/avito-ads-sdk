# PackageIdRequestBodyV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** | Идентификатор пакета услуг, возможные варианты значения: - &#x60;x2_1&#x60; - применение пакета До 2 раз больше просмотров на 1 день - &#x60;x2_7&#x60; - применение пакета До 2 раз больше просмотров на 7 дней - &#x60;x5_1&#x60; - применение пакета До 5 раз больше просмотров на 1 день - &#x60;x5_7&#x60; - применение пакета До 5 раз больше просмотров на 7 дней - &#x60;x10_1&#x60; - применение пакета До 10 раз больше просмотров на 1 день - &#x60;x10_7&#x60; - применение пакета До 10 раз больше просмотров на 7 дней  В некоторых регионах и категориях также доступны дополнительные варианты: - &#x60;x15_1&#x60; - применение пакета До 15 раз больше просмотров на 1 день - &#x60;x15_7&#x60; - применение пакета До 15 раз больше просмотров на 7 дней - &#x60;x20_1&#x60; - применение пакета До 20 раз больше просмотров на 1 день - &#x60;x20_7&#x60; - применение пакета До 20 раз больше просмотров на 7 дней  Если попытаться применить эти пакеты в недоступных для них регионе и категории, оплата не пройдёт.  | 

## Example

```python
from avito_ads.models.package_id_request_body_v2 import PackageIdRequestBodyV2

# TODO update the JSON string below
json = "{}"
# create an instance of PackageIdRequestBodyV2 from a JSON string
package_id_request_body_v2_instance = PackageIdRequestBodyV2.from_json(json)
# print the JSON string representation of the object
print(PackageIdRequestBodyV2.to_json())

# convert the object into a dict
package_id_request_body_v2_dict = package_id_request_body_v2_instance.to_dict()
# create an instance of PackageIdRequestBodyV2 from a dict
package_id_request_body_v2_from_dict = PackageIdRequestBodyV2.from_dict(package_id_request_body_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


