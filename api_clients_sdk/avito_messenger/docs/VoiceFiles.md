# VoiceFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voices_urls** | **Dict[str, str]** |  | [optional] 

## Example

```python
from avito_messenger.models.voice_files import VoiceFiles

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceFiles from a JSON string
voice_files_instance = VoiceFiles.from_json(json)
# print the JSON string representation of the object
print(VoiceFiles.to_json())

# convert the object into a dict
voice_files_dict = voice_files_instance.to_dict()
# create an instance of VoiceFiles from a dict
voice_files_from_dict = VoiceFiles.from_dict(voice_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


