# ResetEmailPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from workplace_client.models.reset_email_password import ResetEmailPassword

# TODO update the JSON string below
json = "{}"
# create an instance of ResetEmailPassword from a JSON string
reset_email_password_instance = ResetEmailPassword.from_json(json)
# print the JSON string representation of the object
print(ResetEmailPassword.to_json())

# convert the object into a dict
reset_email_password_dict = reset_email_password_instance.to_dict()
# create an instance of ResetEmailPassword from a dict
reset_email_password_from_dict = ResetEmailPassword.from_dict(reset_email_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


