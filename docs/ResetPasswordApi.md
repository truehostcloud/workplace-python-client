# workplace_client.ResetPasswordApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_email_password**](ResetPasswordApi.md#reset_email_password) | **POST** /reset-password/ | Reset subscription email password


# **reset_email_password**
> StandardResponse reset_email_password(reset_email_password)

Reset subscription email password

Reset subscription email password

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.reset_email_password import ResetEmailPassword
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
    api_instance = workplace_client.ResetPasswordApi(api_client)
    reset_email_password = workplace_client.ResetEmailPassword() # ResetEmailPassword | 

    try:
        # Reset subscription email password
        api_response = api_instance.reset_email_password(reset_email_password)
        print("The response of ResetPasswordApi->reset_email_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResetPasswordApi->reset_email_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_email_password** | [**ResetEmailPassword**](ResetEmailPassword.md)|  | 

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

