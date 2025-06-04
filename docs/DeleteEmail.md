# DeleteEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**domain** | **str** |  | 
**subscription** | **int** |  | 

## Example

```python
from workplace_console_client.models.delete_email import DeleteEmail

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEmail from a JSON string
delete_email_instance = DeleteEmail.from_json(json)
# print the JSON string representation of the object
print(DeleteEmail.to_json())

# convert the object into a dict
delete_email_dict = delete_email_instance.to_dict()
# create an instance of DeleteEmail from a dict
delete_email_from_dict = DeleteEmail.from_dict(delete_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


