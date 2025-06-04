# workplace_console_client.DeleteAliasApi

All URIs are relative to *http://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alias_create**](DeleteAliasApi.md#delete_alias_create) | **POST** /delete-alias/ | Delete alias.


# **delete_alias_create**
> ChangeQuotaCreate200Response delete_alias_create(data)

Delete alias.

Delete alias.

### Example

* Basic Authentication (Basic):

```python
import workplace_console_client
from workplace_console_client.models.change_quota_create200_response import ChangeQuotaCreate200Response
from workplace_console_client.models.delete_alias import DeleteAlias
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
    api_instance = workplace_console_client.DeleteAliasApi(api_client)
    data = workplace_console_client.DeleteAlias() # DeleteAlias | 

    try:
        # Delete alias.
        api_response = api_instance.delete_alias_create(data)
        print("The response of DeleteAliasApi->delete_alias_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeleteAliasApi->delete_alias_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeleteAlias**](DeleteAlias.md)|  | 

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

