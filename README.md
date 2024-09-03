
 # Handle request & response 
 
 ## Data format 
 
 body: JSON.stringify({
    "server" : "serverName",
    "doctype" : "doctypeName",
    "data" : {
      "field_name" : "value",
      .......................
      ....................... 
    }
  })

  ## Base URL

[https://post-request.onrender.com](https://post-request.onrender.com/)

## End Point
1. Get All Item Group : /getall
2. Get Item Under A Group : /get?param=Item Group Name
3. Post Document Data : /receive_data
    Body = {"server" : ServerName, "doctype" : DoctypeName, "Authorization" : "token 7b052228a6fd29d:7f323743adf2694", "data" : { "item_code" : "Jahangir vi12", "key" : "value", ......}}
   Authorization = token api_key:api_secret
