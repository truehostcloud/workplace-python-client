# SubscriptionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**mailbox** | **int** | Number of mailboxes. | [optional] 
**quota** | **int** | Allowed quota number per mailbox in GB. | [optional] 
**alias** | **int** | Allowed number of aliases per mailbox. | [optional] 
**forward** | **int** | Allowed number of forwarding rules per mailbox. | [optional] 
**platform** | **str** |  | [optional] 
**price** | **decimal.Decimal** |  | [optional] 

## Example

```python
from workplace_console_client.models.subscription_details import SubscriptionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetails from a JSON string
subscription_details_instance = SubscriptionDetails.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetails.to_json())

# convert the object into a dict
subscription_details_dict = subscription_details_instance.to_dict()
# create an instance of SubscriptionDetails from a dict
subscription_details_from_dict = SubscriptionDetails.from_dict(subscription_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


