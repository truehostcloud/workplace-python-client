# OpenExchangeCreateAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** |  | 
**domain_name** | **str** |  | 
**subscription** | **int** |  | 
**new_subscription** | **bool** |  | 

## Example

```python
from workplace_client.models.open_exchange_create_account import OpenExchangeCreateAccount

# TODO update the JSON string below
json = "{}"
# create an instance of OpenExchangeCreateAccount from a JSON string
open_exchange_create_account_instance = OpenExchangeCreateAccount.from_json(json)
# print the JSON string representation of the object
print(OpenExchangeCreateAccount.to_json())

# convert the object into a dict
open_exchange_create_account_dict = open_exchange_create_account_instance.to_dict()
# create an instance of OpenExchangeCreateAccount from a dict
open_exchange_create_account_from_dict = OpenExchangeCreateAccount.from_dict(open_exchange_create_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


