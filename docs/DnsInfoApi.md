# workplace_client.DnsInfoApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_info_create**](DnsInfoApi.md#dns_info_create) | **POST** /dns-info/ | Get DNS information


# **dns_info_create**
> DnsInfoResponse dns_info_create(dns_info_request)

Get DNS information

Get DNS configuration information for a domain

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.dns_info_request import DnsInfoRequest
from workplace_client.models.dns_info_response import DnsInfoResponse
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
    api_instance = workplace_client.DnsInfoApi(api_client)
    dns_info_request = workplace_client.DnsInfoRequest() # DnsInfoRequest | 

    try:
        # Get DNS information
        api_response = api_instance.dns_info_create(dns_info_request)
        print("The response of DnsInfoApi->dns_info_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsInfoApi->dns_info_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_info_request** | [**DnsInfoRequest**](DnsInfoRequest.md)|  | 

### Return type

[**DnsInfoResponse**](DnsInfoResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DNS information response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

