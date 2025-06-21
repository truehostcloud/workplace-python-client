# DnsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**client_id** | **str** | Client id | 
**email** | **str** | Email | 

## Example

```python
from workplace_client.models.dns_info_request import DnsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsInfoRequest from a JSON string
dns_info_request_instance = DnsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(DnsInfoRequest.to_json())

# convert the object into a dict
dns_info_request_dict = dns_info_request_instance.to_dict()
# create an instance of DnsInfoRequest from a dict
dns_info_request_from_dict = DnsInfoRequest.from_dict(dns_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


