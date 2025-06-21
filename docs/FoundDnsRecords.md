# FoundDnsRecords

Found DNS records organized by type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns** | **List[str]** | Name server records | [optional] 
**a** | **List[str]** | IPv4 address records | [optional] 
**aaaa** | **List[str]** | IPv6 address records | [optional] 
**cname** | **List[str]** | Canonical name records | [optional] 
**mx** | **List[str]** | Mail exchange records | [optional] 
**txt** | **List[str]** | Text records | [optional] 
**soa** | **List[str]** | Start of authority records | [optional] 
**srv** | **List[str]** | Service records | [optional] 
**ptr** | **List[str]** | Pointer records | [optional] 

## Example

```python
from workplace_client.models.found_dns_records import FoundDnsRecords

# TODO update the JSON string below
json = "{}"
# create an instance of FoundDnsRecords from a JSON string
found_dns_records_instance = FoundDnsRecords.from_json(json)
# print the JSON string representation of the object
print(FoundDnsRecords.to_json())

# convert the object into a dict
found_dns_records_dict = found_dns_records_instance.to_dict()
# create an instance of FoundDnsRecords from a dict
found_dns_records_from_dict = FoundDnsRecords.from_dict(found_dns_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


