# ChangeEmailQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**quota** | **int** |  | 

## Example

```python
from workplace_console_client.models.change_email_quota import ChangeEmailQuota

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEmailQuota from a JSON string
change_email_quota_instance = ChangeEmailQuota.from_json(json)
# print the JSON string representation of the object
print(ChangeEmailQuota.to_json())

# convert the object into a dict
change_email_quota_dict = change_email_quota_instance.to_dict()
# create an instance of ChangeEmailQuota from a dict
change_email_quota_from_dict = ChangeEmailQuota.from_dict(change_email_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


