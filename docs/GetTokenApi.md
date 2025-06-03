# workplace_console_client.GetTokenApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_create**](GetTokenApi.md#get_token_create) | **POST** /get-token/ | 


# **get_token_create**
> TokenObtainPair get_token_create(data)

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

### Example

* Basic Authentication (Basic):

```python
import workplace_console_client
from workplace_console_client.models.token_obtain_pair import TokenObtainPair
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
    api_instance = workplace_console_client.GetTokenApi(api_client)
    data = workplace_console_client.TokenObtainPair() # TokenObtainPair | 

    try:
        api_response = api_instance.get_token_create(data)
        print("The response of GetTokenApi->get_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetTokenApi->get_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenObtainPair**](TokenObtainPair.md)|  | 

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

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

