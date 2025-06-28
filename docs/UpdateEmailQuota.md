# UpdateEmailQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**email_quota_gb** | **int** |  | 
**client_id** | **int** |  | 

## Example

```python
from workplace_client.models.update_email_quota import UpdateEmailQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailQuota from a JSON string
update_email_quota_instance = UpdateEmailQuota.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailQuota.to_json())

# convert the object into a dict
update_email_quota_dict = update_email_quota_instance.to_dict()
# create an instance of UpdateEmailQuota from a dict
update_email_quota_from_dict = UpdateEmailQuota.from_dict(update_email_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


