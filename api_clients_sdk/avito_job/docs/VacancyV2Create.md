# VacancyV2Create


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_organization_type** | **int** | Тип организации в которой предстоит работать кандидату. Используется для профессии Администратор &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;administrator_organization_type&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-admininstrator-organization-type.xml) объявлен устаревшим и более не будет использоваться.  &lt;br&gt;  | [optional] 
**age** | [**AgeCriteria**](AgeCriteria.md) |  | [optional] 
**age_preferences** | **List[str]** | Блок \&quot;в том числе для кандидатов\&quot; (массив строк)  Возможные значения элементов массива:   - \&quot;olderThan45\&quot; - старше 45 лет;   - \&quot;olderThan14\&quot; - от 14 лет;   - \&quot;olderThan16\&quot; - от 16 лет;   - \&quot;withHealthProblems\&quot; - с нарушениями здоровья;   - \&quot;students\&quot; - для студентов;   - \&quot;pensioners\&quot; - для пенсионеров.  | [optional] 
**apply_processing** | [**ApplyProcessing**](ApplyProcessing.md) |  | [optional] 
**billing_type** | **str** | Вариант платного размещения  Возможные значения:   - \&quot;package\&quot; - размещение объявления осуществляется только при наличии подходящего пакета размещения   - \&quot;packageOrSingle\&quot; - при наличии подходящего пакета оплата размещения объявления произойдет с него; если нет подходящего пакета, но достаточно денег на кошельке Авито, то произойдет разовое размещение  | 
**bonuses** | **List[str]** | Бонусы, которые компания предоставляет кандидатам | [optional] 
**business_area** | **int** | Идентификатор сферы деятельности  &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;business_area&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-business-area.xml) объявлен устаревшим и более не будет использоваться.  &lt;br&gt;  | 
**citizenship** | **List[str]** | Гражданство кандидата.  Если выберите значение, в данных кандидата будет отметка, что кандидат соответствует этому критерию или нет.  Кандидаты не увидят этого в вакансии.  | [optional] 
**construction_work_type** | **List[str]** | С какими видами строительных или ремонтных работ предстоит столкнуться кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;paintingWorks\&quot; - Малярные работы;   - \&quot;wallCovering\&quot; - Облицовка стен;   - \&quot;tileWork\&quot; - Работы с плиткой;   - \&quot;mountingAndInstallation\&quot; - Монтаж и установка;   - \&quot;finishingWork\&quot; - Отделочные работы;   - \&quot;roofing\&quot; - Кровельные работы;   - \&quot;installationAndConfigurationOfEquipment\&quot; - Монтаж и настройка оборудования;   - \&quot;weldingWork\&quot; - Сварочные работы;   - \&quot;constructionOfFacades\&quot; - Строительство фасадов;   - \&quot;formingMaterials\&quot; - Формовка материалов;   - \&quot;concreteAndStoneWorks\&quot; - Бетонные и каменные работы;   - \&quot;repairWork\&quot; - Ремонтные работы;   - \&quot;other\&quot; - Другие.  | [optional] 
**contacts** | [**VacancyV2CreateContacts**](VacancyV2CreateContacts.md) |  | [optional] 
**cuisine** | **List[str]** | Блюда какой кухни предстоит готовить кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;russian\&quot; - Русская;   - \&quot;european\&quot; - Европейская;   - \&quot;caucasian\&quot; - Кавказская;   - \&quot;italian\&quot; - Итальянская;   - \&quot;japanese\&quot; - Японская;   - \&quot;turkish\&quot; - Турецкая;   - \&quot;other\&quot; - Другая.  | [optional] 
**delivery_method** | **List[str]** | Способ доставки | [optional] 
**description** | **str** | Описание вакансии (строка длиной от 1 до 5000 символов)  Можно использовать HTML-теги в тексте.  Поддерживаемые тэги - &#x60;p&#x60;, &#x60;ul&#x60;, &#x60;ol&#x60;, &#x60;li&#x60;, &#x60;br&#x60;, &#x60;strong&#x60;, &#x60;em&#x60;  | 
**driving_experience** | **str** | Стаж вождения | [optional] 
**driving_license_category** | **List[str]** | Категория прав | [optional] 
**eatery_type** | **List[str]** | Формат заведения общепита в котором предстоит работать кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;cafe\&quot; - Кафе;   - \&quot;bar\&quot; - Бар;   - \&quot;fastFood\&quot; - Фастфуд;   - \&quot;restaurant\&quot; - Ресторан;   - \&quot;canteen\&quot; - Столовая;   - \&quot;bakery\&quot; - Пекарня;   - \&quot;other\&quot; - Другой.  | [optional] 
**education_level** | [**VacancyEducationLevel**](VacancyEducationLevel.md) |  | [optional] 
**employment** | **str** | Занятость &lt;br&gt; Возможные значения:   - temporary - Временная   - full - Полная   - internship - Стажировка   - partial - Частичная  Если ничего не выбрать то будет автоматически проставляться в зависимости от графика работы:  При flexible и partTime, тип занятости - partial. ßДля всех остальных full.  | 
**experience** | **str** | Опыт работы | 
**facility_type** | **List[str]** | Тип склада или производственной линии на которой предстоит работать кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;production\&quot; - Производство;   - \&quot;logisticsCenter\&quot; - Логистический центр;   - \&quot;warehouse\&quot; - Склад;   - \&quot;other\&quot; - Другое.  | [optional] 
**food_production_shop_type** | **List[str]** | В каком цеху по приготовлению пищи предстоит работать кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;cold\&quot; - Холодный;   - \&quot;hot\&quot; - Горячий;   - \&quot;confectionery\&quot; - Кондитерский;   - \&quot;preparation\&quot; - Заготовочный;   - \&quot;other\&quot; - Другой.  | [optional] 
**grade** | [**Grade**](Grade.md) |  | [optional] 
**hierarchy** | [**VacancyV2CreateHierarchy**](VacancyV2CreateHierarchy.md) |  | [optional] 
**image_url** | **str** | URL-адрес логотипа вакансии. Ссылка на файл должна быть прямой | (при переходе не открываются элементы другого сайта (логотипы, кнопки или другие детали интерфейса) и не запрашивается логин и пароль) и доступной для IP 185.89.12.0/22, 146.158.48.0/21, 185.79.237.224/28 и 87.245.204.32/28; | [optional] 
**is_company_car** | **bool** | Предоставляет ли компания автомобиль | [optional] 
**is_side_job** | **bool** | Подработка | [optional] 
**location** | [**VacancyV2CreateLocation**](VacancyV2CreateLocation.md) |  | 
**medical_book** | [**MedicalBookVacancy**](MedicalBookVacancy.md) |  | [optional] 
**medical_specialization** | **List[str]** | Медицинская специализация (можно указать несколько значений через запятую) &lt;br&gt; см. названия специализаций в [ справочнике ](https://www.avito.st/s/openapi/catalog-medical-spec.xml)  | [optional] 
**medical_specialization_ids** | **List[int]** | Медицинская специализация (можно указать несколько значений) &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;medical_specialization&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID).  | [optional] 
**payout_frequency** | **str** | Частота выплат &lt;br&gt; Возможные значения:   - \&quot;dailyPay\&quot; - Каждый день;   - \&quot;biweeklyPay\&quot; - Дважды в месяц;   - \&quot;weeklyPay\&quot; - Раз в неделю;   - \&quot;thriceMonthlyPay\&quot; - три раза в месяц;   - \&quot;monthlyPay\&quot; - Раз в месяц.  Для paid_period равным month и week недоступно для выбора dailyPay.  deprecated значение hourlyPay будет заменено на dailyPay  | [optional] 
**profession** | **int** | Название профессии &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;profession&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-profession.xml?v&#x3D;5) объявлен устаревшим и более не будет использоваться. &lt;br&gt; | [optional] 
**programs** | **List[str]** | Блок участие вакансии в программах (массив строк)  Если у компании от лица которой создается вакансия нет всех необходимых разрешений на участие, программа у вакансии не будет включена.  Возможные значения элементов массива:   - \&quot;chastyeVyplaty\&quot; - Частые выплаты.  | [optional] 
**registration_method** | **List[str]** | Способ оформления (можно указать несколько значений через запятую) &lt;br&gt; Возможные значения: - contract - Трудовой договор - gph_ip - ГПХ с ИП - gph_self_employed - ГПХ с самозанятым - gph_individual - ГПХ с физическим лицом  | [optional] 
**retail_equipment_type** | **List[str]** | С каким оборудованием или ПО предстоит работать кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;cashRegisterAndPosTerminals\&quot; - Касса и POS-терминалы;   - \&quot;accountingSoftware\&quot; - Программы учёта товаров.  | [optional] 
**retail_shop_type** | **List[str]** | Что продает магазин в котором предстоит работать кандидату &lt;br&gt; Возможные значения элементов массива:   - \&quot;hypermarketOrSupermarket\&quot; - Гипермаркет или супермаркет;   - \&quot;grocery\&quot; - Продуктовый;   - \&quot;electronicsAndHouseholdAppliances\&quot; - Электроника и бытовая техника;   - \&quot;clothesAndShoes\&quot; - Одежда и обувь;   - \&quot;perfumesAndCosmetics\&quot; - Парфюмерия и косметика;   - \&quot;constructionAndHouseholdGoods\&quot; - Строительство и хозтовары;   - \&quot;childrenGoods\&quot; - Детские товары;   - \&quot;sportingGoods\&quot; - Спортивные товары;   - \&quot;petShop\&quot; - Зоомагазин;   - \&quot;pharmacy\&quot; - Аптека;   - \&quot;other\&quot; - Другое.  | [optional] 
**salary** | [**VacancyV2CreateSalary**](VacancyV2CreateSalary.md) |  | [optional] 
**salary_detail** | [**SalaryDetail**](SalaryDetail.md) |  | [optional] 
**schedule** | **str** | Режим работы &lt;br&gt; Возможные значения:   - flyInFlyOut - Вахта   - fixed - Фиксированный   - flexible - Гибкий   - shift - Сменный  flyInFlyOut - Вахта, при выборе данного режима работы, адрес вакансии может быть только \&quot;Город\&quot;, если адрес передается полноценный, то улица будет отрезана и адрес будет до \&quot;Города\&quot;.  deprecated значения fiveDay, sixDay, partTime, fullDay и remote будут заменены на fixed  | 
**shifts** | **List[int]** | Смены &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;shifts&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Доступен только для следующих режимов работы (schedule): \&quot;Сменный (shift)\&quot;,  \&quot;Фиксированный (fixed)\&quot; &lt;br&gt; Для режима работы (schedule) \&quot;Фиксированный (fixed)\&quot; доступны только значения показывающие отношение количества рабочих дней к выходным, например \&quot;5/2\&quot;  | [optional] 
**title** | **str** | Название вакансии (строка длиной от 1 до 50 символов) | 
**tools_availability** | [**ToolsAvailability**](ToolsAvailability.md) |  | [optional] 
**vacancy_code** | **str** | Внутренний идентификатор вакансии или номер заявки на подбор, максимум 150 символов | [optional] 
**vehicle_type** | **int** | На какой технике предстоит работать кандитату, от выбора техники зависит какие категории прав можно будет указать в вакансии &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;vehicle_type&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Статичный [справочник](https://www.avito.st/s/openapi/catalog-vehicle-type.xml) объявлен устаревшим и более не будет использоваться.  &lt;br&gt; Используется только для профессий   - Водитель пассажирского транспорта  - Водитель грузового транспорта  - Водитель спецтехники  - Машинист спецтехники &lt;br&gt;  | [optional] 
**work_days_per_week** | **List[int]** | Количество рабочих дней в неделю &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;work_days_per_week&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Доступен только для режима работы (schedule) равным \&quot;Гибкий (flexible)\&quot;  | [optional] 
**work_format** | **List[str]** | Блок \&quot;Формат работы\&quot; (массив строк)  Возможные значения элементов массива:   - \&quot;office\&quot; - В офисе или на объекте;   - \&quot;remote\&quot; - Удалённо;   - \&quot;gibrid\&quot; - Гибрид.  | [optional] 
**work_hours_per_day** | **List[int]** | Количество рабочих часов в день &lt;br&gt; Получить актуальный список доступных значений можно из справочника &#x60;work_hours_per_day&#x60; через метод [getDictByID](/api-catalog/job/documentation#operation/getDictByID). &lt;br&gt; Для режима работы (schedule) равным \&quot;Вахта (flyInFlyOut)\&quot; недоступны значения \&quot;13–15 часов\&quot;, \&quot;Больше 15 часов\&quot;  &lt;br&gt; Для типа занятости (employment) равным \&quot;Полная (full)\&quot; недоступны значения \&quot;До 4 часов\&quot;, \&quot;4–5 часов\&quot; &lt;br&gt; Для типов занятости (employment) равным \&quot;Временная (temporary)\&quot;, \&quot;Стажировка (internship)\&quot;, \&quot;Частичная (partial)\&quot; недоступно значение \&quot;Больше 15 часов\&quot;  | [optional] 
**worker_class** | **List[str]** | Предпочтительный разряд кандидата &lt;br&gt; Возможные значения элементов массива:   - \&quot;1\&quot; - Первый;   - \&quot;2\&quot; - Второй;   - \&quot;3\&quot; - Третий;   - \&quot;4\&quot; - Четвертый;   - \&quot;5andHigher\&quot; - Пятый и выше;   - \&quot;notNeeded\&quot; - Не требуется.  | [optional] 

## Example

```python
from avito_job.models.vacancy_v2_create import VacancyV2Create

# TODO update the JSON string below
json = "{}"
# create an instance of VacancyV2Create from a JSON string
vacancy_v2_create_instance = VacancyV2Create.from_json(json)
# print the JSON string representation of the object
print(VacancyV2Create.to_json())

# convert the object into a dict
vacancy_v2_create_dict = vacancy_v2_create_instance.to_dict()
# create an instance of VacancyV2Create from a dict
vacancy_v2_create_from_dict = VacancyV2Create.from_dict(vacancy_v2_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


