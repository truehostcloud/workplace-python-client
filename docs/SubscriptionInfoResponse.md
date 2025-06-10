# SubscriptionInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**OrderDisplay**](OrderDisplay.md) |  | 
**emails** | [**List[EmailDisplay]**](EmailDisplay.md) |  | 

## Example

```python
from workplace_client.models.subscription_info_response import SubscriptionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionInfoResponse from a JSON string
subscription_info_response_instance = SubscriptionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionInfoResponse.to_json())

# convert the object into a dict
subscription_info_response_dict = subscription_info_response_instance.to_dict()
# create an instance of SubscriptionInfoResponse from a dict
subscription_info_response_from_dict = SubscriptionInfoResponse.from_dict(subscription_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


