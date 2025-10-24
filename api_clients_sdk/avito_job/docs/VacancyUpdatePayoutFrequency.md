# VacancyUpdatePayoutFrequency

Частота выплат Возможные значения:   - \"dailyPay\" - Каждый день;   - \"biweeklyPay\" - Дважды в месяц;   - \"weeklyPay\" - Раз в неделю;   - \"thriceMonthlyPay\" - три раза в месяц   - \"monthlyPay\" - Раз в месяц.  deprecated значение hourlyPay будет заменено на dailyPay 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from avito_job.models.vacancy_update_payout_frequency import VacancyUpdatePayoutFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyUpdatePayoutFrequency from a JSON string
vacancy_update_payout_frequency_instance = VacancyUpdatePayoutFrequency.from_json(json)
# print the JSON string representation of the object
print(VacancyUpdatePayoutFrequency.to_json())

# convert the object into a dict
vacancy_update_payout_frequency_dict = vacancy_update_payout_frequency_instance.to_dict()
# create an instance of VacancyUpdatePayoutFrequency from a dict
vacancy_update_payout_frequency_from_dict = VacancyUpdatePayoutFrequency.from_dict(vacancy_update_payout_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


