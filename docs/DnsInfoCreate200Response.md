# DnsInfoCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | 
**message** | **str** |  | 
**domain** | **str** |  | 
**all_dns_score** | **float** |  | 
**found** | **float** |  | 
**total** | **float** |  | 
**missing_dns** | **List[str]** |  | 
**other_missing_dns** | **List[str]** |  | 
**found_dns** | [**DnsInfoCreate200ResponseFoundDns**](DnsInfoCreate200ResponseFoundDns.md) |  | 
**error** | **List[str]** |  | 

## Example

```python
from workplace_client.models.dns_info_create200_response import DnsInfoCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DnsInfoCreate200Response from a JSON string
dns_info_create200_response_instance = DnsInfoCreate200Response.from_json(json)
# print the JSON string representation of the object
print(DnsInfoCreate200Response.to_json())

# convert the object into a dict
dns_info_create200_response_dict = dns_info_create200_response_instance.to_dict()
# create an instance of DnsInfoCreate200Response from a dict
dns_info_create200_response_from_dict = DnsInfoCreate200Response.from_dict(dns_info_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


