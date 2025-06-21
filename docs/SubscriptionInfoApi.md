# workplace_client.SubscriptionInfoApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_info_create**](SubscriptionInfoApi.md#subscription_info_create) | **POST** /subscription-info/ | Get subscription usage info


# **subscription_info_create**
> SubscriptionUsageResponse subscription_info_create(sub_scription_info)

Get subscription usage info

Get subscription usage info

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.sub_scription_info import SubScriptionInfo
from workplace_client.models.subscription_usage_response import SubscriptionUsageResponse
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://workplace-console.truehost.cloud/api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "https://workplace-console.truehost.cloud/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = workplace_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionInfoApi(api_client)
    sub_scription_info = workplace_client.SubScriptionInfo() # SubScriptionInfo | 

    try:
        # Get subscription usage info
        api_response = api_instance.subscription_info_create(sub_scription_info)
        print("The response of SubscriptionInfoApi->subscription_info_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionInfoApi->subscription_info_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_scription_info** | [**SubScriptionInfo**](SubScriptionInfo.md)|  | 

### Return type

[**SubscriptionUsageResponse**](SubscriptionUsageResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription usage information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

