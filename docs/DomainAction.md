# DomainAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**domain** | **str** |  | 

## Example

```python
from workplace_client.models.domain_action import DomainAction

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAction from a JSON string
domain_action_instance = DomainAction.from_json(json)
# print the JSON string representation of the object
print(DomainAction.to_json())

# convert the object into a dict
domain_action_dict = domain_action_instance.to_dict()
# create an instance of DomainAction from a dict
domain_action_from_dict = DomainAction.from_dict(domain_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


