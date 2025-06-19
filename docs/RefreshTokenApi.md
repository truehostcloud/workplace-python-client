# workplace_client.RefreshTokenApi

All URIs are relative to *http://https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_token_create**](RefreshTokenApi.md#refresh_token_create) | **POST** /refresh-token/ | 


# **refresh_token_create**
> TokenRefresh refresh_token_create(data)

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

### Example

* Api Key Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.token_refresh import TokenRefresh
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
    api_instance = workplace_client.RefreshTokenApi(api_client)
    data = workplace_client.TokenRefresh() # TokenRefresh | 

    try:
        api_response = api_instance.refresh_token_create(data)
        print("The response of RefreshTokenApi->refresh_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefreshTokenApi->refresh_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenRefresh**](TokenRefresh.md)|  | 

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

