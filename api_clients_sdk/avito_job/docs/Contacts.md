# Contacts

Контактная информация

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email (строка длиной от 0 до 255 символов) | [optional] 
**name** | **str** | Имя менеджера, контактного лица компании по данному объявлению (строка длиной до 30 символов) | [optional] 
**phone** | [**Phone**](Phone.md) |  | [optional] 

## Example

```python
from avito_job.models.contacts import Contacts

# TODO update the JSON string below
json = "{}"
# create an instance of Contacts from a JSON string
contacts_instance = Contacts.from_json(json)
# print the JSON string representation of the object
print(Contacts.to_json())

# convert the object into a dict
contacts_dict = contacts_instance.to_dict()
# create an instance of Contacts from a dict
contacts_from_dict = Contacts.from_dict(contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


