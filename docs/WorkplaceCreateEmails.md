# WorkplaceCreateEmails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** |  | 
**domain_name** | **str** |  | 
**plan_id** | **int** |  | 
**new_subscription** | **bool** |  | 
**display_name** | **str** |  | 
**user_password** | **str** |  | 
**email_quota_gb** | **int** |  | 
**client_id** | **int** |  | 

## Example

```python
from workplace_client.models.workplace_create_emails import WorkplaceCreateEmails

# TODO update the JSON string below
json = "{}"
# create an instance of WorkplaceCreateEmails from a JSON string
workplace_create_emails_instance = WorkplaceCreateEmails.from_json(json)
# print the JSON string representation of the object
print(WorkplaceCreateEmails.to_json())

# convert the object into a dict
workplace_create_emails_dict = workplace_create_emails_instance.to_dict()
# create an instance of WorkplaceCreateEmails from a dict
workplace_create_emails_from_dict = WorkplaceCreateEmails.from_dict(workplace_create_emails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


