# workplace_client.AvailablePackagesApi

All URIs are relative to *http://https://your-workplace-console.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_packages_list**](AvailablePackagesApi.md#available_packages_list) | **GET** /available-packages/ | Get available subscriptions.


# **available_packages_list**
> List[SubscriptionDetails] available_packages_list()

Get available subscriptions.

Get available subscriptions.

### Example

* Basic Authentication (Basic):

```python
import workplace_client
from workplace_client.models.subscription_details import SubscriptionDetails
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://your-workplace-console.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://your-workplace-console.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.AvailablePackagesApi(api_client)

    try:
        # Get available subscriptions.
        api_response = api_instance.available_packages_list()
        print("The response of AvailablePackagesApi->available_packages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailablePackagesApi->available_packages_list: %s\n" % e)
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

