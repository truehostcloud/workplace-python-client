# workplace_console_client.AvailableSubscriptionsApi

All URIs are relative to *http://127.0.0.1:8001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_subscriptions_list**](AvailableSubscriptionsApi.md#available_subscriptions_list) | **GET** /available-subscriptions/ | Get available subscriptions.


# **available_subscriptions_list**
> List[SubscriptionDetails] available_subscriptions_list()

Get available subscriptions.

Get available subscriptions.

### Example

* Basic Authentication (Basic):

```python
import workplace_console_client
from workplace_console_client.models.subscription_details import SubscriptionDetails
from workplace_console_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001/api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_console_client.Configuration(
    host = "http://127.0.0.1:8001/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_console_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_console_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_console_client.AvailableSubscriptionsApi(api_client)

    try:
        # Get available subscriptions.
        api_response = api_instance.available_subscriptions_list()
        print("The response of AvailableSubscriptionsApi->available_subscriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSubscriptionsApi->available_subscriptions_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SubscriptionDetails]**](SubscriptionDetails.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

