# workplace_client.UpgradeApi

All URIs are relative to *http://https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upgrade_create**](UpgradeApi.md#upgrade_create) | **POST** /upgrade/ | Upgrade subscription.


# **upgrade_create**
> ChangeQuotaCreate200Response upgrade_create(data)

Upgrade subscription.

Upgrade subscription.

### Example

* Api Key Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.change_quota_create200_response import ChangeQuotaCreate200Response
from workplace_client.models.sub_scription_info import SubScriptionInfo
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://workplace-console.truehost.cloud/api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://workplace-console.truehost.cloud/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.UpgradeApi(api_client)
    data = workplace_client.SubScriptionInfo() # SubScriptionInfo | 

    try:
        # Upgrade subscription.
        api_response = api_instance.upgrade_create(data)
        print("The response of UpgradeApi->upgrade_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpgradeApi->upgrade_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubScriptionInfo**](SubScriptionInfo.md)|  | 

### Return type

[**ChangeQuotaCreate200Response**](ChangeQuotaCreate200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

