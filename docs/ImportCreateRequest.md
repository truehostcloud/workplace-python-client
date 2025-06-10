# ImportCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | CSV or excel file containing email accounts | 
**domain** | **str** | Domain to associate with emails | 

## Example

```python
from workplace_client.models.import_create_request import ImportCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCreateRequest from a JSON string
import_create_request_instance = ImportCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ImportCreateRequest.to_json())

# convert the object into a dict
import_create_request_dict = import_create_request_instance.to_dict()
# create an instance of ImportCreateRequest from a dict
import_create_request_from_dict = ImportCreateRequest.from_dict(import_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


