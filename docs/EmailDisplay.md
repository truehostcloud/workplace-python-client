# EmailDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**email_quota_gb** | **int** | Email quota in GB | [optional] 
**max_quota** | **int** | Max email quota in GB | [optional] 
**used_quota** | **int** | Used quota in GB | [optional] 
**email_id** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from workplace_client.models.email_display import EmailDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDisplay from a JSON string
email_display_instance = EmailDisplay.from_json(json)
# print the JSON string representation of the object
print(EmailDisplay.to_json())

# convert the object into a dict
email_display_dict = email_display_instance.to_dict()
# create an instance of EmailDisplay from a dict
email_display_from_dict = EmailDisplay.from_dict(email_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


