# SubscriptionInfoCreate200Response


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
from workplace_client.models.subscription_info_create200_response import SubscriptionInfoCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionInfoCreate200Response from a JSON string
subscription_info_create200_response_instance = SubscriptionInfoCreate200Response.from_json(json)
# print the JSON string representation of the object
print(SubscriptionInfoCreate200Response.to_json())

# convert the object into a dict
subscription_info_create200_response_dict = subscription_info_create200_response_instance.to_dict()
# create an instance of SubscriptionInfoCreate200Response from a dict
subscription_info_create200_response_from_dict = SubscriptionInfoCreate200Response.from_dict(subscription_info_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


