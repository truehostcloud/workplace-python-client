# SubscriptionsRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_context** | **object** |  | [optional] 
**user_emails** | **List[object]** |  | [optional] 
**email_aliases** | **object** |  | [optional] 

## Example

```python
from workplace_console_client.models.subscriptions_read200_response import SubscriptionsRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsRead200Response from a JSON string
subscriptions_read200_response_instance = SubscriptionsRead200Response.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsRead200Response.to_json())

# convert the object into a dict
subscriptions_read200_response_dict = subscriptions_read200_response_instance.to_dict()
# create an instance of SubscriptionsRead200Response from a dict
subscriptions_read200_response_from_dict = SubscriptionsRead200Response.from_dict(subscriptions_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


