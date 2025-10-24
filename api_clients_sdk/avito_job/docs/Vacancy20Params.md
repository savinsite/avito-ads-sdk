# Vacancy20Params

Блок с параметрами вакансии. Все поля опциональны и выводятся при наличии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Место работы | [optional] 
**age_preferences** | **List[str]** | Подходит кандидатам | [optional] 
**bonuses** | **List[str]** | Бонусы, которые компания предоставляет кандидатам | [optional] 
**business_area** | **str** | Сфера деятельности компании. &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;business_area&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-business-area.xml) объявлен устаревшим и более не будет использоваться.  &lt;br&gt;  | [optional] 
**change** | **List[str]** | Смены | [optional] 
**construction_work_type** | **List[str]** | С какими видами строительных или ремонтных работ предстоит столкнуться кандидату | [optional] 
**coordinates** | [**Vacancy20ParamsCoordinates**](Vacancy20ParamsCoordinates.md) |  | [optional] 
**cuisine** | **List[str]** | Блюда какой кухни предстоит готовить кандидату | [optional] 
**delivery_method** | **List[str]** | Способ доставки | [optional] 
**driving_experience** | **str** | Стаж вождения | [optional] 
**driving_license_category** | **List[str]** | Категория прав | [optional] 
**eatery_type** | **List[str]** | Формат заведения общепита в котором предстоит работать кандидату | [optional] 
**experience** | **str** | Требуемый опыт работы | [optional] 
**facility_type** | **List[str]** | Тип склада или производственной линии на которой предстоит работать кандидату | [optional] 
**food_production_shop_type** | **List[str]** | В каком цеху по приготовлению пищи предстоит работать кандидату | [optional] 
**is_company_car** | **str** | Предоставляет ли компания машину | [optional] 
**medical_book** | **str** | Требуется ли медкнижка и кем она оформляется при приеме на работу | [optional] 
**paid_period** | **str** | Оплачиваемый период | [optional] 
**payout_frequency** | **str** | Частота выплат | [optional] 
**piecework_flag** | **str** | Сдельная оплата. На самом деле это bool поле. Но из-за ограничений платформы выводим как есть. Т.е. если поле присутствует, значит piecework_flag &#x3D; true иначе &#x3D; false | [optional] 
**profession** | **str** | Название профессии &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;profession&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-profession.xml?v&#x3D;5) объявлен устаревшим и более не будет использоваться. &lt;br&gt; | [optional] 
**programs** | **List[str]** | Участие вакансии в программах Авито | [optional] 
**registration_method** | **List[str]** | Способ оформления | [optional] 
**retail_equipment_type** | **List[str]** | С каким оборудованием или ПО предстоит работать кандидату | [optional] 
**retail_shop_type** | **List[str]** | Что продает магазин в котором предстоит работать кандидату | [optional] 
**salary** | [**Vacancy20ParamsSalary**](Vacancy20ParamsSalary.md) |  | [optional] 
**salary_base_bonus** | **str** | Премия | [optional] 
**salary_base_range** | [**Vacancy20ParamsSalaryBaseRange**](Vacancy20ParamsSalaryBaseRange.md) |  | [optional] 
**schedule** | **str** | Режим работы | [optional] 
**taxes** | **str** | Зарплата указана | [optional] 
**tools_availability** | **str** | Требуется ли кандидату собственные инструменты для работы | [optional] 
**where_to_work** | **str** | Где предстоит работать | [optional] 
**worker_class** | **List[str]** | Предпочтительный разряд кандидата | [optional] 

## Example

```python
from avito_job.models.vacancy20_params import Vacancy20Params

# TODO update the JSON string below
json = "{}"
# create an instance of Vacancy20Params from a JSON string
vacancy20_params_instance = Vacancy20Params.from_json(json)
# print the JSON string representation of the object
print(Vacancy20Params.to_json())

# convert the object into a dict
vacancy20_params_dict = vacancy20_params_instance.to_dict()
# create an instance of Vacancy20Params from a dict
vacancy20_params_from_dict = Vacancy20Params.from_dict(vacancy20_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


