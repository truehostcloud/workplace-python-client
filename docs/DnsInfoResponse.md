# DnsInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain name that was checked | 
**score** | **float** | DNS configuration score | 
**all_dns_score** | **float** | Overall DNS score | 
**found** | **int** | Number of required DNS records found | 
**total** | **int** | Total number of required DNS records | 
**missing_dns** | [**List[DnsRecord]**](DnsRecord.md) | List of missing required DNS records | 
**other_missing_dns** | [**List[DnsRecord]**](DnsRecord.md) | List of other missing DNS records | 
**found_dns** | [**FoundDnsRecords**](FoundDnsRecords.md) |  | 

## Example

```python
from workplace_client.models.dns_info_response import DnsInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsInfoResponse from a JSON string
dns_info_response_instance = DnsInfoResponse.from_json(json)
# print the JSON string representation of the object
print(DnsInfoResponse.to_json())

# convert the object into a dict
dns_info_response_dict = dns_info_response_instance.to_dict()
# create an instance of DnsInfoResponse from a dict
dns_info_response_from_dict = DnsInfoResponse.from_dict(dns_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


