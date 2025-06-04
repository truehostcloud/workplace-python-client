# AliasDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**primary_email** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from workplace_console_client.models.alias_display import AliasDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of AliasDisplay from a JSON string
alias_display_instance = AliasDisplay.from_json(json)
# print the JSON string representation of the object
print(AliasDisplay.to_json())

# convert the object into a dict
alias_display_dict = alias_display_instance.to_dict()
# create an instance of AliasDisplay from a dict
alias_display_from_dict = AliasDisplay.from_dict(alias_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


