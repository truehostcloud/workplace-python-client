# workplace_client.ChangeQuotaApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_email_quota**](ChangeQuotaApi.md#change_email_quota) | **POST** /change-quota/ | Change email quota


# **change_email_quota**
> StandardResponse change_email_quota(change_email_quota)

Change email quota

Change email quota

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.change_email_quota import ChangeEmailQuota
from workplace_client.models.standard_response import StandardResponse
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
    api_instance = workplace_client.ChangeQuotaApi(api_client)
    change_email_quota = workplace_client.ChangeEmailQuota() # ChangeEmailQuota | 

    try:
        # Change email quota
        api_response = api_instance.change_email_quota(change_email_quota)
        print("The response of ChangeQuotaApi->change_email_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeQuotaApi->change_email_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_email_quota** | [**ChangeEmailQuota**](ChangeEmailQuota.md)|  | 

### Return type

[**StandardResponse**](StandardResponse.md)

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

