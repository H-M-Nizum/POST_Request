
 # Handle request & response 
 
 ## Base URL

[https://post-request.onrender.com](https://post-request.onrender.com/)

## End Point
--------------------------------------------------------------------------------------------------
1. Get APi key & Secrate Key :- $${\color{green}GET}$$ -   /getapisecrate
   
```
{
  "param": "Panal URL"
}
```

--------------------------------------------------------------------------------------------------
2. Get item, based on item Group - $${\color{green}GET}$$ -  /groupitems
```
{
  "erp_url" : "Panal URL",
  "group_name": "Item Group"
}
```
---------------------------------------------------------------------------------------------------
3. Get all type of doctype data - $${\color{green}GET}$$ - /getall
```
http://127.0.0.1:5000/getall?erp_url=erp_url&doctype_name=doctype_name
```
---------------------------------------------------------------------------------------------------
4. Post request Sales order -  $${\color{yellow}POST}$$ -  /post_data
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
4. Update Any DocType Document -  $${\color{blue}PUT}$$ - /put_data

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
4. Delete Any DocType Document -  $${\color{red}DELETE}$$ - /delete_data

```
{
  "erp_url" : "Panal URL",
  "doctype_name": "Doctype Name",
  "document_name" : "Document Name or ID"
}
```
-----------------------------------------------------------------------------------------------------
5. SignUp  -  $${\color{yellow}POST}$$ - /signup
```
{
  "erp_url" : "base url",
  "erp_data" : {
    "email": "Ionic@gmail.com",
    "first_name": "name",
    "full_name": "full name",
    "password": "password",
    "redirect_to": "/app"
}
}


```
-----------------------------------------------------------------------------------------------------
6. Login  -  $${\color{yellow}POST}$$ - /login

```
{
  "erp_url" : "https://ecommerce.ionicerp.xyz",
  "erp_data" : {
        "usr": "username",
        "pwd": "password"
    }
}

```
------------------------------------------------------------------------------------------------------
7. Logout -  $${\color{yellow}POST}$$ - /logout

```
{
  "erp_url" : "base url"
}
```


