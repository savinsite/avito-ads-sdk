# VacancyCreatePayoutFrequency

Частота выплат<br> Возможные значения:   - \"dailyPay\" - Каждый день;   - \"biweeklyPay\" - Дважды в месяц;   - \"weeklyPay\" - Раз в неделю;   - \"thriceMonthlyPay\" - три раза в месяц;   - \"monthlyPay\" - Раз в месяц.  Для paid_period равным month и week недоступно для выбора dailyPay.  deprecated значение hourlyPay будет заменено на dailyPay 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from avito_job.models.vacancy_create_payout_frequency import VacancyCreatePayoutFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyCreatePayoutFrequency from a JSON string
vacancy_create_payout_frequency_instance = VacancyCreatePayoutFrequency.from_json(json)
# print the JSON string representation of the object
print(VacancyCreatePayoutFrequency.to_json())

# convert the object into a dict
vacancy_create_payout_frequency_dict = vacancy_create_payout_frequency_instance.to_dict()
# create an instance of VacancyCreatePayoutFrequency from a dict
vacancy_create_payout_frequency_from_dict = VacancyCreatePayoutFrequency.from_dict(vacancy_create_payout_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


