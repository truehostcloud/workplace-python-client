# workplace_client.DeleteAliasApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email_alias**](DeleteAliasApi.md#delete_email_alias) | **POST** /delete-alias/ | Delete alias


# **delete_email_alias**
> StandardResponse delete_email_alias(delete_alias)

Delete alias

Delete alias

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.delete_alias import DeleteAlias
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
    api_instance = workplace_client.DeleteAliasApi(api_client)
    delete_alias = workplace_client.DeleteAlias() # DeleteAlias | 

    try:
        # Delete alias
        api_response = api_instance.delete_email_alias(delete_alias)
        print("The response of DeleteAliasApi->delete_email_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeleteAliasApi->delete_email_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_alias** | [**DeleteAlias**](DeleteAlias.md)|  | 

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

