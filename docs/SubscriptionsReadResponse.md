# SubscriptionsReadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_context** | **object** |  | [optional] 
**user_emails** | **List[object]** |  | [optional] 
**email_aliases** | **object** |  | [optional] 

## Example

```python
from workplace_client.models.subscriptions_read_response import SubscriptionsReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsReadResponse from a JSON string
subscriptions_read_response_instance = SubscriptionsReadResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsReadResponse.to_json())

# convert the object into a dict
subscriptions_read_response_dict = subscriptions_read_response_instance.to_dict()
# create an instance of SubscriptionsReadResponse from a dict
subscriptions_read_response_from_dict = SubscriptionsReadResponse.from_dict(subscriptions_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


