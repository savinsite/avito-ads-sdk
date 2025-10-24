# StickerResp

Информация о значках для переданного списка объявлений

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Описание значка | 
**id** | **int** | Идентификатор значка | 
**title** | **str** | Название значка | 

## Example

```python
from avito_ads.models.sticker_resp import StickerResp

# TODO update the JSON string below
json = "{}"
# create an instance of StickerResp from a JSON string
sticker_resp_instance = StickerResp.from_json(json)
# print the JSON string representation of the object
print(StickerResp.to_json())

# convert the object into a dict
sticker_resp_dict = sticker_resp_instance.to_dict()
# create an instance of StickerResp from a dict
sticker_resp_from_dict = StickerResp.from_dict(sticker_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


