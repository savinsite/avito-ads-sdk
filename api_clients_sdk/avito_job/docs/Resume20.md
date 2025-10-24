# Resume20


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Описание резюме | [optional] 
**id** | **int** | Идентификатор резюме | [optional] 
**is_active** | **bool** | Активность резюме | [optional] 
**is_purchased** | **bool** | Контакты резюме куплены | [optional] 
**params** | [**Resume20Params**](Resume20Params.md) |  | [optional] 
**photos** | [**List[Photo]**](Photo.md) | Присутствует в ответе только если в запросе есть флаг photos&#x3D;true | [optional] 
**salary** | **int** | Зарплата. Поле может отсутствовать в ответе (выводится при наличии зарплаты) | [optional] 
**start_time** | **str** | Дата публикации резюме | [optional] 
**title** | **str** | Наименование резюме | [optional] 
**update_time** | **str** | Дата последнего обновления резюме | [optional] 
**url** | **str** | URL резюме на сайте | [optional] 

## Example

```python
from avito_job.models.resume20 import Resume20

# TODO update the JSON string below
json = "{}"
# create an instance of Resume20 from a JSON string
resume20_instance = Resume20.from_json(json)
# print the JSON string representation of the object
print(Resume20.to_json())

# convert the object into a dict
resume20_dict = resume20_instance.to_dict()
# create an instance of Resume20 from a dict
resume20_from_dict = Resume20.from_dict(resume20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


