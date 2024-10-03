
 # Handle request & response 
 
 ## Base URL

[https://post-request.onrender.com](https://post-request.onrender.com/)

## End Point
--------------------------------------------------------------------------------------------------
1. Get APi key & Secrate Key :-  /getapisecrate
   
```
{
  "param": "Panal URL"
}
```

--------------------------------------------------------------------------------------------------
2. Get item, based on item Group - /groupitems
```
{
  "erp_url" : "Panal URL",
  "group_name": "Item Group"
}
```
---------------------------------------------------------------------------------------------------
3. Get all type of doctype data - /getall
```
{
  "erp_url" : "Panal URL",
  "doctype_name": "Doctype name"
}
```
---------------------------------------------------------------------------------------------------
4. Post request Sales order - /receive_data
```
 {
  "server": "Panal URL",
  "doctype": "Doctype Name",
  "data": {
    "customer": "Customer Name",
    "transaction_date": "2024-09-05",
    "custom_delivery_type": "",  
    "items": [
        {
            "item_code": "Item Code",
            "item_name": "Item Name",
            "delivery_date": "2024-09-05",
            "qty": Quantity,
            "rate": 1 Pes Rate,
            "amount": Total Amount,
            "uom": "Item UOM"
        }
    ]
}

}
```






1. Get All Item Group : /getall
2. Get Item Under A Group : /get?param=Item Group Name
3. Post Document Data : /receive_data
    Body = {"server" : ServerName, "doctype" : DoctypeName, "Authorization" : "token 7b052228a6fd29d:7f323743adf2694", "data" : { "item_code" : "Jahangir vi12", "key" : "value", ......}}
   Authorization = token api_key:api_secret
