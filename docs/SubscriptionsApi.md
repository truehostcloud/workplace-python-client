# workplace_client.SubscriptionsApi

All URIs are relative to *http://https://your-workplace-console.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_create**](SubscriptionsApi.md#subscriptions_create) | **POST** /subscriptions/ | Create a new email subscription, it will create a new subscription for the domain if emails list is not empty
[**subscriptions_list**](SubscriptionsApi.md#subscriptions_list) | **GET** /subscriptions/ | 
[**subscriptions_read**](SubscriptionsApi.md#subscriptions_read) | **GET** /subscriptions/{context_id}/ | Get subscription details
[**update_subscription_status**](SubscriptionsApi.md#update_subscription_status) | **POST** /subscriptions/{context_id}/ | Update subscription status, delete, suspend, unsuspend, etc...


# **subscriptions_create**
> ChangeQuotaCreate200Response subscriptions_create(data)

Create a new email subscription, it will create a new subscription for the domain if emails list is not empty

Create a new email subscription

### Example

* Basic Authentication (Basic):

```python
import workplace_client
from workplace_client.models.change_quota_create200_response import ChangeQuotaCreate200Response
from workplace_client.models.open_exchange_create_account import OpenExchangeCreateAccount
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://your-workplace-console.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://your-workplace-console.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionsApi(api_client)
    data = workplace_client.OpenExchangeCreateAccount() # OpenExchangeCreateAccount | 

    try:
        # Create a new email subscription, it will create a new subscription for the domain if emails list is not empty
        api_response = api_instance.subscriptions_create(data)
        print("The response of SubscriptionsApi->subscriptions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OpenExchangeCreateAccount**](OpenExchangeCreateAccount.md)|  | 

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

# **subscriptions_list**
> subscriptions_list()

### Example

* Basic Authentication (Basic):

```python
import workplace_client
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://your-workplace-console.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://your-workplace-console.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionsApi(api_client)

    try:
        api_instance.subscriptions_list()
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_read**
> SubscriptionsRead200Response subscriptions_read(context_id)

Get subscription details

Get subscription details

### Example

* Basic Authentication (Basic):

```python
import workplace_client
from workplace_client.models.subscriptions_read200_response import SubscriptionsRead200Response
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://your-workplace-console.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://your-workplace-console.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionsApi(api_client)
    context_id = 'context_id_example' # str | 

    try:
        # Get subscription details
        api_response = api_instance.subscriptions_read(context_id)
        print("The response of SubscriptionsApi->subscriptions_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**|  | 

### Return type

[**SubscriptionsRead200Response**](SubscriptionsRead200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_status**
> ChangeQuotaCreate200Response update_subscription_status(context_id, data)

Update subscription status, delete, suspend, unsuspend, etc...

Update subscription status. 

### Example

* Basic Authentication (Basic):

```python
import workplace_client
from workplace_client.models.change_quota_create200_response import ChangeQuotaCreate200Response
from workplace_client.models.service_action import ServiceAction
from workplace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://your-workplace-console.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = workplace_client.Configuration(
    host = "http://https://your-workplace-console.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = workplace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionsApi(api_client)
    context_id = 'context_id_example' # str | 
    data = workplace_client.ServiceAction() # ServiceAction | 

    try:
        # Update subscription status, delete, suspend, unsuspend, etc...
        api_response = api_instance.update_subscription_status(context_id, data)
        print("The response of SubscriptionsApi->update_subscription_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_subscription_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**|  | 
 **data** | [**ServiceAction**](ServiceAction.md)|  | 

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

