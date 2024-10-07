from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import json


app = Flask(__name__)
CORS(app) 

#--------------------------------------- Get API key & Secrate key from mht.ionicerp.xyz--------------------
def fetch_API_Secrate_Key(api_url):
    url = f"""https://mht.ionicerp.xyz/api/resource/IONIC APPS Registration?filters=[["apps_url", "=", "{api_url}"]]&fields=["company_name", "apps_url", "api_key", "secret_key"]&limit_page_length=99"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "token 9c3d69dfcdf0340:2458265514dd7c1"
    }
    response = requests.get(url, headers=headers)
    
    # Check if the response was successful
    if response.status_code == 200:
        # print('main - ', response.json())
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

@app.route('/getapisecrate', methods=['GET'])
def get_API_Secrate_Key(): 
    # Accessing param from the request body
    data = request.json
    api_url = data.get('api_url')  # Replace 'api_url' with the actual key you expect in the body
    
    if api_url is None:
        return jsonify({"error": "Missing parameters"}), 400
    data = fetch_API_Secrate_Key(api_url)
    # Check if the 'data' key exists in the response
    if 'data' in data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found", "response": data})


#------------------------------------------------------- Get All ALl type of doctype data ---------------------------------------------------------------------
def fetch_all_data(erp_url, doctype_name):
    panal_data = fetch_API_Secrate_Key(f"{erp_url}")
    print(panal_data)
    if panal_data['data']:
        panal_url = panal_data['data'][0]['apps_url']
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panal is not registed"}
    
    url = f"{erp_url}/api/resource/{doctype_name}?fields=[\"*\"]&limit_page_length=99"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : f"token {panal_api_key}:{panal_secrate_key}"
    }
    
    response = requests.get(url, headers=headers)
    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Return an error message with status code
        return {"error": "Failed to fetch data", "status_code": response.status_code}

@app.route('/getall', methods=['GET'])
def get_all_documents():
    erp_url = request.args.get('erp_url')
    doctype_name = request.args.get('doctype_name')  # Replace 'param' with the actual key you expect in the body
    
    if not doctype_name or not erp_url:
        return jsonify({"error": "Missing doctype_name or erp_url parameter"}), 400
    
    data1 = fetch_all_data(erp_url, doctype_name)
    # Check if the 'data' key exists in the response
    if 'data' in data1:
        return jsonify(data1)
    else:
        # Handle the case where 'data' key is missing
        return jsonify({"error": "No data found", "response": data1})



# ---------------------------------------------------------------------- Get All Item Based ON Group ---------------------------------------------------
def fetch_data(erp_url, group_name):
    panal_data = fetch_API_Secrate_Key(f"{erp_url}")
    print(panal_data)
    if panal_data['data']:
        panal_url = panal_data['data'][0]['apps_url']
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panel is not registered"}
    
 
    
    url = f"""{erp_url}/api/resource/Item?filters=[["item_group", "=", "{group_name}"]]&fields=["*"]&limit_page_length=99"""
    # url = "https://ecommerce.ionicerp.xyz/api/resource/Item?filters=[['item_group', '=', 'Fish & Meat']]&fields=['*']&limit_page_length=99"
    print(url)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"token {panal_api_key}:{panal_secrate_key}"
    }
    print(headers)
 
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers=headers)
    print(response)
    # Check if the response was successful
    if response.status_code == 200:
   
        print(response.json())
        return response.json()
    else:
        # Return an error message with status code
        return {"error": "Failed to fetch data", "status_code": response.status_code}

@app.route('/groupitems', methods=['GET'])
def get_document():
    erp_url = request.args.get('erp_url')
    group_name = request.args.get('group_name')
    # URL-encode the group_name to handle special characters
    
        # Safely encode the group_name in the URL
    print(erp_url, group_name)

    # Check for missing parameters
    if not group_name or not erp_url:
        return jsonify({"error": "Missing group_name or erp_url parameter"}), 400
    
    if '*' in group_name:
        group_name = group_name.replace('*', '&')
    print(erp_url, group_name)
    encoded_group_name = quote(group_name)
    
    data = fetch_data(erp_url, encoded_group_name)
    
    # Check if the 'data' key exists in the response
    if 'data' in data and data['data']:
        return jsonify(data)
    else:
        # Handle the case where 'data' key is missing or empty
        return jsonify({"error": "No data found", "response": data})


    
    
# ----------------------------------------------------------------- POST data any Panal & any Doctype-----------------------------------------
@app.route('/post_data', methods=['POST'])
def receive_data():
    data = request.json  
    # Post the received data to another URL
    post_data_to_another_url(data)
    return data

def post_data_to_another_url(data):
    panal_data = fetch_API_Secrate_Key(f"{data['server']}")
    print(panal_data)
    if panal_data['data']:
        panal_url = panal_data['data'][0]['apps_url']
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panal is not registed"}
    
    # Define the URL to post the data to
    url = f"{panal_url}/api/resource/{data['doctype']}"

    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            # "Authorization" : "token 7b052228a6fd29d:7f323743adf2694"
            "Authorization" : f"token {panal_api_key}:{panal_secrate_key}"
        }
    #     # Post the data to the other URL
    #     # response = requests.post(another_url, json=data)
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status() 
        print('Data posted to another URL successfully')
        print(response)
    except requests.exceptions.RequestException as e:
        response = f"""'Error posting data to another URL:', {e}"""
        # response.raise_for_status() 
        print('Error posting data to another URL:', e)




# -------------------------------------------------------------- PUT ---------------------------------------
def update_data(erp_url, doctype_name, document_name):
    panal_data = fetch_API_Secrate_Key(erp_url)
    
    if panal_data['data']:
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panel is not registered"}

    url = f"{erp_url}/api/resource/{doctype_name}/{document_name}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"token {panal_api_key}:{panal_secrate_key}"
    }
    
    data = request.json  # Use the data from the request body
    print(data)
    response = requests.put(url, json=data, headers=headers)
    
    try:
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.HTTPError as e:
        return {"error": str(e)}, response.status_code

    # print('Data posted to another URL successfully')
    # print(response.json())  # Print the response content
    return response.json()

@app.route('/put_data', methods=['PUT'])
def put_data():
    data = request.json
    erp_url = data.get('erp_url')
    doctype_name = data.get('doctype_name')
    document_name = data.get('document_name')
    
    if erp_url is None or doctype_name is None or document_name is None:
        return jsonify({"error": "Missing parameters"}), 400

    response_data = update_data(erp_url, doctype_name, document_name)
    return jsonify(response_data)



# ------------------------------------------------- Delete Data ----------------------------------------------------------------
def delete_data(erp_url, doctype_name, document_name):
    panal_data = fetch_API_Secrate_Key(erp_url)
    
    if panal_data['data']:
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panel is not registered"}

    url = f"{erp_url}/api/resource/{doctype_name}/{document_name}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"token {panal_api_key}:{panal_secrate_key}"
    }

    response = requests.delete(url, headers=headers)
    print(response)
    try:
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.HTTPError as e:
        if response.status_code == 404:
            return {"error": "Resource not found."}, 404
        elif response.status_code == 417:
            return {"error": f"""Cannot delete or cancel because Contact '{document_name}' is linked with Another Doctype"""}, 417
        else:
            return {"error": str(e)}, response.status_code

    # print('Data posted to another URL successfully')
    # print(response.json())  # Print the response content
    return response.json()

@app.route('/delete_data', methods=['DELETE'])
def del_data():
    data = request.json
    erp_url = data.get('erp_url')
    doctype_name = data.get('doctype_name')
    document_name = data.get('document_name')
    
    if erp_url is None or doctype_name is None or document_name is None:
        return jsonify({"error": "Missing parameters"}), 400

    response_data = delete_data(erp_url, doctype_name, document_name)
    return jsonify(response_data)




#- --------------------------------------- User signin -----------------------------------------------------
def fetch_signup_data(erp_url, erp_data):
    panal_data = fetch_API_Secrate_Key(erp_url)
    # print('panal_data - ', panal_data)
    if panal_data['data']:
        panal_url = panal_data['data'][0]['apps_url']
        panal_api_key = panal_data['data'][0]['api_key']
        panal_secrate_key = panal_data['data'][0]['secret_key']
    else:
        return {"error": "Your panal is not registed"}
    url = f"{panal_url}/api/method/frappe.core.doctype.user.user.sign_up"

    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization" : f"token {panal_api_key}:{panal_secrate_key}"
        }

        # print(erp_data)
        response = requests.post(url, headers=headers, data=json.dumps(erp_data))
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        response = f"""'Error posting data to another URL:', {e}"""
        # print('Error posting data to another URL:', e)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json  
    # print('data ', data)
    erp_url = data.get('erp_url')
    erp_data = data.get('erp_data')
    fetch_signup_data(erp_url, erp_data)
    return data


@app.route('/login', methods=['POST'])
def signin():
    data = request.json  
    # print('data ', data)
    erp_url = data.get('erp_url')
    erp_data = data.get('erp_data')
    url = f"{erp_url}/api/method/login"
    try:
        response = requests.post(url, json=erp_data)  # use json= for JSON data
        print(response)

        if response.status_code == 200:
            print("Login successful!")
            session_cookies = response.cookies
            return {
                "status": "success",
                "data": response.json(),  # Return the JSON response from the server
                "cookies": session_cookies.get_dict()  # Optionally return the cookies
            }
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            return {
                "status": "error",
                "message": response.text,
                "status_code": response.status_code
            }, response.status_code

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {
            "status": "error",
            "message": "An error occurred while trying to login.",
            "error": str(e)
        }, 500


@app.route('/logout', methods=['POST'])
def signout():
    data = request.json  
    erp_url = data.get('erp_url')
    url = f"{erp_url}/api/method/logout"
    
    try:
        session_cookies = data.get('cookies')  # Get cookies from the request data if needed
        
        response = requests.post(url, cookies=session_cookies)  # Pass cookies if required
        print(response)

        if response.status_code == 200:
            print("Logout successful!")
            return {
                "status": "success",
                "message": "User logged out successfully."
            }
        else:
            print(f"Logout failed: {response.status_code} - {response.text}")
            return {
                "status": "error",
                "message": response.text,
                "status_code": response.status_code
            }, response.status_code

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {
            "status": "error",
            "message": "An error occurred while trying to logout.",
            "error": str(e)
        }, 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
