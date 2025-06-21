# SubscriptionUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_emails** | **float** |  | [optional] 
**remaining_quota** | **float** |  | [optional] 
**remaining_emails** | **float** |  | [optional] 
**allowed_emails** | **float** |  | [optional] 
**allowed_alias** | **float** |  | [optional] 
**remaining_alias** | **float** |  | [optional] 
**allowed_quota** | **float** |  | [optional] 

## Example

```python
from workplace_client.models.subscription_usage_response import SubscriptionUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUsageResponse from a JSON string
subscription_usage_response_instance = SubscriptionUsageResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUsageResponse.to_json())

# convert the object into a dict
subscription_usage_response_dict = subscription_usage_response_instance.to_dict()
# create an instance of SubscriptionUsageResponse from a dict
subscription_usage_response_from_dict = SubscriptionUsageResponse.from_dict(subscription_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


