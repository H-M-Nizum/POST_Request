
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
4. Post request Sales order - /post_data
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
---------------------------------------------------------------------------------------------------
4. Update Any DocType Document - /put_data

```
{
  "erp_url" : "Panal URL",
  "doctype_name": "Doctype Name",
  "document_name" : "Document Name or ID",
  "data": {
        Document Data 
   }
}
```

---------------------------------------------------------------------------------------------------
4. Delete Any DocType Document - /delete_data

```
{
  "erp_url" : "Panal URL",
  "doctype_name": "Doctype Name",
  "document_name" : "Document Name or ID"
}
```


