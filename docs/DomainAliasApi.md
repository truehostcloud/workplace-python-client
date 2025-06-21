# workplace_client.DomainAliasApi

All URIs are relative to *https://workplace-console.truehost.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_alias_create**](DomainAliasApi.md#domain_alias_create) | **POST** /domain-alias/ | Get domain alias list


# **domain_alias_create**
> List[AliasDisplay] domain_alias_create(domain)

Get domain alias list

Get domain alias list

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import workplace_client
from workplace_client.models.alias_display import AliasDisplay
from workplace_client.models.domain import Domain
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
    api_instance = workplace_client.DomainAliasApi(api_client)
    domain = workplace_client.Domain() # Domain | 

    try:
        # Get domain alias list
        api_response = api_instance.domain_alias_create(domain)
        print("The response of DomainAliasApi->domain_alias_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAliasApi->domain_alias_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**Domain**](Domain.md)|  | 

### Return type

[**List[AliasDisplay]**](AliasDisplay.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of domain aliases |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

