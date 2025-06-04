# workplace_console_client.ChangeQuotaApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_quota_create**](ChangeQuotaApi.md#change_quota_create) | **POST** /change-quota/ | Change email quota.


# **change_quota_create**
> ChangeQuotaCreate200Response change_quota_create(data)

Change email quota.

Change email quota.

### Example

* Basic Authentication (Basic):

```python
import workplace_console_client
from workplace_console_client.models.change_email_quota import ChangeEmailQuota
from workplace_console_client.models.change_quota_create200_response import ChangeQuotaCreate200Response
from workplace_console_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_console_client.Configuration(
    host = "http://127.0.0.1:8000/api"
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
    api_instance = workplace_console_client.ChangeQuotaApi(api_client)
    data = workplace_console_client.ChangeEmailQuota() # ChangeEmailQuota | 

    try:
        # Change email quota.
        api_response = api_instance.change_quota_create(data)
        print("The response of ChangeQuotaApi->change_quota_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeQuotaApi->change_quota_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ChangeEmailQuota**](ChangeEmailQuota.md)|  | 

### Return type

[**ChangeQuotaCreate200Response**](ChangeQuotaCreate200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

