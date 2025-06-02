# openapi_client.RefreshTokenApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_token_create**](RefreshTokenApi.md#refresh_token_create) | **POST** /refresh-token/ | 


# **refresh_token_create**
> TokenRefresh refresh_token_create(data)

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

### Example

* Basic Authentication (Basic):

```python
import openapi_client
from openapi_client.models.token_refresh import TokenRefresh
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RefreshTokenApi(api_client)
    data = openapi_client.TokenRefresh() # TokenRefresh | 

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

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

