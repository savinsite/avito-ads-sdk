# Resume20Params

Блок с параметрами резюме. Все поля опциональны и выводятся при наличии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_to_business_trip** | **str** | Готовность к командировкам | [optional] 
**address** | **str** | Место, рядом с которым вы хотите работать | [optional] 
**age** | **int** | Возраст соискателя | [optional] 
**business_area** | **str** | Сфера деятельности | [optional] 
**driver_licence** | **str** | Водительское удостоверение | [optional] 
**driver_licence_category** | **List[str]** | Категория водительских прав | [optional] 
**education** | **str** | Образование соискателя | [optional] 
**education_list** | [**List[Resume20ParamsEducationListInner]**](Resume20ParamsEducationListInner.md) |  | [optional] 
**experience_list** | [**List[Resume20ParamsExperienceListInner]**](Resume20ParamsExperienceListInner.md) |  | [optional] 
**language_list** | [**List[Resume20ParamsLanguageListInner]**](Resume20ParamsLanguageListInner.md) |  | [optional] 
**moving** | **str** | Возможность переезда | [optional] 
**nationality** | **str** | Гражданство соискателя | [optional] 
**pol** | **str** | Пол соискателя | [optional] 
**razreshenie_na_rabotu_v_rossii** | **str** | Наличие разрешения на работу в России | [optional] 
**schedule** | **str** | Режим работы Возможные значения:   - flyInFlyOut - Вахта   - partTime - Неполный день   - fullDay - Полный день   - flexible - Плавающий   - shift - Сменный   - remote - Удалённая работа   - fiveDay - Пятидневная рабочая неделя   - sixDay - Шестидневная рабочая неделя  | [optional] 

## Example

```python
from avito_job.models.resume20_params import Resume20Params

# TODO update the JSON string below
json = "{}"
# create an instance of Resume20Params from a JSON string
resume20_params_instance = Resume20Params.from_json(json)
# print the JSON string representation of the object
print(Resume20Params.to_json())

# convert the object into a dict
resume20_params_dict = resume20_params_instance.to_dict()
# create an instance of Resume20Params from a dict
resume20_params_from_dict = Resume20Params.from_dict(resume20_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


