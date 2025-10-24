# Phone

Контактный телефон, если не передать - подставляется номер из профиля который используется по умолчанию. Если передать номер телефона которого нет в профиле, то он будет добавлен в профиль, но по нему необходимо будет пройти верификацию. Если номер телефона принадлежит другому пользователю, то вакансия не будет опубликована. Если вакансия публикуется от имени сотрудника и номер телефона ему не принадлежит - объявление так же не будет опубликовано.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Код города (строка, соответствующая шаблону \&quot;^\\\\d{0,6}$\&quot;) | 
**country** | **str** | Код страны (строка, соответствующая шаблону \&quot;^\\\\+?\\\\d{0,5}$\&quot;) | 
**number** | **str** | Телефон (строка, соответствующая шаблону \&quot;^[\\\\d -]{4,32}$\&quot;) | 

## Example

```python
from avito_job.models.phone import Phone

# TODO update the JSON string below
json = "{}"
# create an instance of Phone from a JSON string
phone_instance = Phone.from_json(json)
# print the JSON string representation of the object
print(Phone.to_json())

# convert the object into a dict
phone_dict = phone_instance.to_dict()
# create an instance of Phone from a dict
phone_from_dict = Phone.from_dict(phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


