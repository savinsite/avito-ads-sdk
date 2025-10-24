# PrevalidationAnswer

Ответ на вопрос превалидации. Содержит лейбл, название и значение переменной.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Название переменной | [optional] 
**value** | **str** | Значение переменной | [optional] 
**variable** | **str** | Идентификатор переменной. Распространенные значения:&lt;br/&gt; &#x60;job_fio&#x60; - ФИО&lt;br/&gt; &#x60;job_phone&#x60; - телефон&lt;br/&gt; &#x60;job_birthdate&#x60; - дата рождения&lt;br/&gt; &#x60;job_city&#x60; - город&lt;br/&gt; &#x60;job_gender&#x60; - пол&lt;br/&gt; &#x60;job_citizenship&#x60; - гражданство&lt;br/&gt; &#x60;job_schedule&#x60; - желаемый режим работы&lt;br/&gt; &#x60;job_educational_level&#x60; - образование&lt;br/&gt; &#x60;job_district&#x60; - желаемый район работы&lt;br/&gt; &#x60;job_experience&#x60; - есть ли подходящий опыт&lt;br/&gt; &#x60;job_work_duration&#x60; - стаж работы на аналогичной должности&lt;br/&gt; &#x60;job_last_employment&#x60; - последнее место работы&lt;br/&gt; &#x60;job_last_position&#x60; - должность на последнем месте работы&lt;br/&gt; &#x60;job_salary_expectations&#x60; - желаемая зарплата&lt;br/&gt; &#x60;job_responsibility&#x60; - образование, специальность&lt;br/&gt; &#x60;job_current_education&#x60; - учится ли сейчас&lt;br/&gt; &#x60;job_current_employment&#x60; - работает ли сейчас&lt;br/&gt; &#x60;docs_available&#x60; - наличие СНИЛС, ИНН, паспорта или временного удостоверения&lt;br/&gt; &#x60;job_military_docs&#x60; - наличие документов воинского учета&lt;br/&gt; &#x60;is_drivers_licence&#x60; - наличие водительских прав&lt;br/&gt; &#x60;job_drivers_licence&#x60; - категория водительских прав&lt;br/&gt; &#x60;drivers_licence_country&#x60; - страна выдачи водительских прав&lt;br/&gt; &#x60;is_individual_entrepreneur&#x60; - оформлен ли как ИП&lt;br/&gt; &#x60;job_employment_records&#x60; - наличие трудовой книжки&lt;br/&gt; &#x60;is_medical_record&#x60; - наличие медицинской книжки&lt;br/&gt; &#x60;job_covid19&#x60; - сертификат о вакцинации&lt;br/&gt; &#x60;job_official_employment&#x60; - готовность работать по трудовому договору&lt;br/&gt; &#x60;job_tha&#x60; - РВП&lt;br/&gt; &#x60;job_work_permit&#x60; - разрешение на работу&lt;br/&gt; &#x60;job_tractor_driver_license&#x60; - наличие прав для управления спецтехникой&lt;br/&gt; &#x60;way_to_travel&#x60; - способ перемещения по городу&lt;br/&gt; &#x60;job_hostel&#x60; - нужно ли проживание&lt;br/&gt; &#x60;job_fly_in_basis_readiness&#x60; - готовность к вахте по графику из вакансии&lt;br/&gt; &#x60;job_spent_time_road&#x60; - желаемое время на дорогу&lt;br/&gt; &#x60;job_call_time&#x60; - время для звонка&lt;br/&gt; &#x60;job_driving_experience&#x60; - стаж вождения&lt;br/&gt; &#x60;job_phone_android&#x60; - наличие телефона на Android&lt;br/&gt; &#x60;job_use_own_car&#x60; - наличие авто&lt;br/&gt; &#x60;job_for_me&#x60; - ищет ли работу для себя&lt;br/&gt; &#x60;job_email&#x60; - электронная почта&lt;br/&gt; &#x60;job_preferred_address&#x60; - желаемый адрес работы&lt;br/&gt; &#x60;is_self_employed&#x60; - статус самозанятого&lt;br/&gt; &#x60;job_training_ready&#x60; - готовность пройти обучение&lt;br/&gt; &#x60;has_pc_and_workplace&#x60; - наличие рабочего места и компьютера | [optional] 

## Example

```python
from avito_job.models.prevalidation_answer import PrevalidationAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of PrevalidationAnswer from a JSON string
prevalidation_answer_instance = PrevalidationAnswer.from_json(json)
# print the JSON string representation of the object
print(PrevalidationAnswer.to_json())

# convert the object into a dict
prevalidation_answer_dict = prevalidation_answer_instance.to_dict()
# create an instance of PrevalidationAnswer from a dict
prevalidation_answer_from_dict = PrevalidationAnswer.from_dict(prevalidation_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


