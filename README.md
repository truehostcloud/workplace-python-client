# Workplace Console Client

This is the Truehost's pip package for using the workplace console API from other python applications.

- API version: v1
- Package version: 1.0.1
- Generator version: 7.13.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/truehost/workplace-console-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/truehost/workplace-console-client.git`)

Then import the package:
```python
import workplace_console_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import workplace_console_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import workplace_console_client
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

    try:
        api_instance.change_quota_create()
    except ApiException as e:
        print("Exception when calling ChangeQuotaApi->change_quota_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChangeQuotaApi* | [**change_quota_create**](docs/ChangeQuotaApi.md#change_quota_create) | **POST** /change-quota/ | 
*CreateAliasApi* | [**create_alias_create**](docs/CreateAliasApi.md#create_alias_create) | **POST** /create-alias/ | 
*DeleteAliasApi* | [**delete_alias_create**](docs/DeleteAliasApi.md#delete_alias_create) | **POST** /delete-alias/ | 
*DeleteEmailApi* | [**delete_email_create**](docs/DeleteEmailApi.md#delete_email_create) | **POST** /delete-email/ | 
*DnsInfoApi* | [**dns_info_create**](docs/DnsInfoApi.md#dns_info_create) | **POST** /dns-info/ | 
*DomainApi* | [**domain_create**](docs/DomainApi.md#domain_create) | **POST** /domain/ | 
*DomainAliasApi* | [**domain_alias_create**](docs/DomainAliasApi.md#domain_alias_create) | **POST** /domain-alias/ | 
*DomainInfoApi* | [**domain_info_create**](docs/DomainInfoApi.md#domain_info_create) | **POST** /domain-info/ | 
*GetTokenApi* | [**get_token_create**](docs/GetTokenApi.md#get_token_create) | **POST** /get-token/ | 
*ImportApi* | [**import_create**](docs/ImportApi.md#import_create) | **POST** /import/ | 
*RefreshTokenApi* | [**refresh_token_create**](docs/RefreshTokenApi.md#refresh_token_create) | **POST** /refresh-token/ | 
*ResetPasswordApi* | [**reset_password_create**](docs/ResetPasswordApi.md#reset_password_create) | **POST** /reset-password/ | 
*SubscriptionInfoApi* | [**subscription_info_create**](docs/SubscriptionInfoApi.md#subscription_info_create) | **POST** /subscription-info/ | 
*SubscriptionsApi* | [**subscriptions_create**](docs/SubscriptionsApi.md#subscriptions_create) | **POST** /subscriptions/ | 
*SubscriptionsApi* | [**subscriptions_create_0**](docs/SubscriptionsApi.md#subscriptions_create_0) | **POST** /subscriptions/{context_id}/ | 
*SubscriptionsApi* | [**subscriptions_list**](docs/SubscriptionsApi.md#subscriptions_list) | **GET** /subscriptions/ | 
*SubscriptionsApi* | [**subscriptions_read**](docs/SubscriptionsApi.md#subscriptions_read) | **GET** /subscriptions/{context_id}/ | 
*UpgradeApi* | [**upgrade_create**](docs/UpgradeApi.md#upgrade_create) | **POST** /upgrade/ | 


## Documentation For Models

 - [DnsInfoCreate200Response](docs/DnsInfoCreate200Response.md)
 - [DnsInfoCreateRequest](docs/DnsInfoCreateRequest.md)
 - [TokenObtainPair](docs/TokenObtainPair.md)
 - [TokenRefresh](docs/TokenRefresh.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Basic"></a>
### Basic

- **Type**: HTTP basic authentication


## Author

support@truehost.cloud


