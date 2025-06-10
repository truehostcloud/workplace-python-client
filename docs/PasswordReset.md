# PasswordReset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from workplace_client.models.password_reset import PasswordReset

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordReset from a JSON string
password_reset_instance = PasswordReset.from_json(json)
# print the JSON string representation of the object
print(PasswordReset.to_json())

# convert the object into a dict
password_reset_dict = password_reset_instance.to_dict()
# create an instance of PasswordReset from a dict
password_reset_from_dict = PasswordReset.from_dict(password_reset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


