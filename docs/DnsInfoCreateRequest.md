# DnsInfoCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**client_id** | **str** | Client id | 
**email** | **str** | Email | 

## Example

```python
from workplace_console_client.models.dns_info_create_request import DnsInfoCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsInfoCreateRequest from a JSON string
dns_info_create_request_instance = DnsInfoCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DnsInfoCreateRequest.to_json())

# convert the object into a dict
dns_info_create_request_dict = dns_info_create_request_instance.to_dict()
# create an instance of DnsInfoCreateRequest from a dict
dns_info_create_request_from_dict = DnsInfoCreateRequest.from_dict(dns_info_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


