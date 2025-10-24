# VacancyV2CreateContacts

Контактная информация

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_calls** | **bool** | Разрешены ли звонки по вакансии. | [optional] [default to True]
**allow_messages** | **bool** | Возможность откликнуться на вакансию через сайт. Если передается apply_processing, то значение allow_messages будет игнорироваться и равно true | [optional] 
**name** | **str** | Имя менеджера, контактного лица компании по данному объявлению (строка длиной до 30 символов) | [optional] 
**phone** | **str** | Контактный телефон, если не передать - подставляется номер из профиля который используется по умолчанию. Если передать номер телефона которого нет в профиле, то он будет добавлен в профиль, но по нему необходимо будет пройти верификацию. Если номер телефона принадлежит другому пользователю, то вакансия не будет опубликована. Если вакансия публикуется от имени сотрудника и номер телефона ему не принадлежит - объявление так же не будет опубликовано. | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create_contacts import VacancyV2CreateContacts

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2CreateContacts from a JSON string
vacancy_v2_create_contacts_instance = VacancyV2CreateContacts.from_json(json)
# print the JSON string representation of the object
print(VacancyV2CreateContacts.to_json())

# convert the object into a dict
vacancy_v2_create_contacts_dict = vacancy_v2_create_contacts_instance.to_dict()
# create an instance of VacancyV2CreateContacts from a dict
vacancy_v2_create_contacts_from_dict = VacancyV2CreateContacts.from_dict(vacancy_v2_create_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


