# OrderDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**context_id** | **int** |  | [optional] 
**domain** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**average_size** | **int** |  | [optional] 
**filestore_id** | **int** |  | [optional] 
**filestore_name** | **str** |  | [optional] 
**max_quota** | **int** |  | [optional] 
**context_name** | **str** |  | [optional] 
**used_quota** | **int** |  | [optional] 
**gab_mode** | **str** |  | [optional] 
**is_order_active** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**unallocated_quota** | **int** |  | [optional] 
**unallocated_alias** | **int** |  | [optional] 
**is_alias_calculated** | **bool** |  | [optional] 
**is_alias_synched** | **bool** |  | [optional] 
**last_dns_check** | **datetime** |  | [optional] 
**is_dns_valid** | **bool** |  | [optional] 
**client_id** | **int** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**subscription** | **int** |  | [optional] 

## Example

```python
from workplace_console_client.models.order_display import OrderDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDisplay from a JSON string
order_display_instance = OrderDisplay.from_json(json)
# print the JSON string representation of the object
print(OrderDisplay.to_json())

# convert the object into a dict
order_display_dict = order_display_instance.to_dict()
# create an instance of OrderDisplay from a dict
order_display_from_dict = OrderDisplay.from_dict(order_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


