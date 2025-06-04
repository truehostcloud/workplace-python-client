# EmailAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**domain** | **str** |  | 
**alias** | **str** |  | 

## Example

```python
from workplace_console_client.models.email_alias import EmailAlias

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAlias from a JSON string
email_alias_instance = EmailAlias.from_json(json)
# print the JSON string representation of the object
print(EmailAlias.to_json())

# convert the object into a dict
email_alias_dict = email_alias_instance.to_dict()
# create an instance of EmailAlias from a dict
email_alias_from_dict = EmailAlias.from_dict(email_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


