# workplace_console_client.DomainInfoApi

All URIs are relative to *http://127.0.0.1:8001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_info_create**](DomainInfoApi.md#domain_info_create) | **POST** /domain-info/ | Get domain subscription details.


# **domain_info_create**
> SubscriptionInfoResponse domain_info_create(data)

Get domain subscription details.

Get domain subscription details and emails list.

### Example

* Basic Authentication (Basic):

```python
import workplace_console_client
from workplace_console_client.models.sub_scription_info import SubScriptionInfo
from workplace_console_client.models.subscription_info_response import SubscriptionInfoResponse
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
    api_instance = workplace_console_client.DomainInfoApi(api_client)
    data = workplace_console_client.SubScriptionInfo() # SubScriptionInfo | 

    try:
        # Get domain subscription details.
        api_response = api_instance.domain_info_create(data)
        print("The response of DomainInfoApi->domain_info_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->domain_info_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubScriptionInfo**](SubScriptionInfo.md)|  | 

### Return type

[**SubscriptionInfoResponse**](SubscriptionInfoResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

