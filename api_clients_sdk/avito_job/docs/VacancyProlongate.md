# VacancyProlongate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_type** | **str** | Вариант платного размещения  Возможные значения:   - \&quot;package\&quot; - размещение объявления осуществляется только при наличии подходящего пакета размещения   - \&quot;packageOrSingle\&quot; - при наличии подходящего пакета оплата размещения объявления произойдет с него; если нет подходящего пакета, но достаточно денег на кошельке Авито, то произойдет разовое размещение   - \&quot;single\&quot; - только разовое размещение, произойдет при наличии достаточной суммы на кошельке Авито; если есть подходящий пакет размещения, он будет проигнорирован  | 
**employee_id** | **int** | employee_id - Идентификатор сотрудника на Авито. Если этот параметр указан, то с баланса сотрудника в Avito Pro будет списано размещение. Использовать параметр можно только с billing_type равным package. Сотрудник должен быть в активен.  | [optional] 

## Example

```python
from avito_job.models.vacancy_prolongate import VacancyProlongate

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyProlongate from a JSON string
vacancy_prolongate_instance = VacancyProlongate.from_json(json)
# print the JSON string representation of the object
print(VacancyProlongate.to_json())

# convert the object into a dict
vacancy_prolongate_dict = vacancy_prolongate_instance.to_dict()
# create an instance of VacancyProlongate from a dict
vacancy_prolongate_from_dict = VacancyProlongate.from_dict(vacancy_prolongate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


