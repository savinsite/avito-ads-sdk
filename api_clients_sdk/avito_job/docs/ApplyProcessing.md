# ApplyProcessing

Объект с настройкой обработки откликов на вакансию.  Даёт возможность настроить отклики только с резюме. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_questions** | **List[str]** | *DEPRECATED* Заполнение поля не влияет на вакансию.   Массив со списком дополнительных вопросов, которые задаст ассистент Авито.    - &#x60;experience&#x60; - вопрос про опыт работы.  В качестве критерия будет использоваться значение поля &#x60;experience&#x60;.  В результатах опроса ассистент отметит, достаточно у кандидата опыта или нет.     - &#x60;citizenship&#x60; - вопрос про гражданство. В качестве критерия будет использоваться значение поля &#x60;citizenship&#x60;, если оно заполнено.    - &#x60;age&#x60; - вопрос про возраст. В качестве критерия будет использоваться значение поля &#x60;age&#x60;, если оно заполнено.  | [optional] 
**apply_type** | **str** | Принимает два значения:    - &#x60;with_assistant&#x60; *DEPRECATED* - Указание данного значения не влияет на вакансию. Обработка отклика с помощью ассистента Авито. После отклика на вакансию  ассистент Авито предложит кандидату ответить на несколько вопросов — результаты придут в чат. ФИО и номер телефона ассистент спросит в любом случае. Остальные вопросы можно настроить  в поле &#x60;additional_questions&#x60;.    - &#x60;only_with_resume&#x60; - на вакансию смогут откликаться только кандидаты с резюме. Если у кандидата нет резюме,  Авито поможет создать его и откликнуться на вакансию  | [optional] 

## Example

```python
from avito_job.models.apply_processing import ApplyProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyProcessing from a JSON string
apply_processing_instance = ApplyProcessing.from_json(json)
# print the JSON string representation of the object
print(ApplyProcessing.to_json())

# convert the object into a dict
apply_processing_dict = apply_processing_instance.to_dict()
# create an instance of ApplyProcessing from a dict
apply_processing_from_dict = ApplyProcessing.from_dict(apply_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


