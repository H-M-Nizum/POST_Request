from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import json


# const SITE_URL = "https://ecommerce.ionicerp.xyz";
# const API_SECRET = "02fbdaed78fefbb";
# const API_KEY = "84859bedced40f4";
# ---------------------------------------------------------------------- Get All Item Based ON Group ---------------------------------------------------
def fetch_data(param):
    url = f"""https://ecommerce.ionicerp.xyz/api/resource/Item?filters=[["item_group", "=", "{param}"]]&fields=["*"]&limit_page_length=99"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "token 84859bedced40f4:02fbdaed78fefbb"
    }
    payload = {
        "param1": param
    }
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


app = Flask(__name__)
CORS(app) 
@app.route('/get', methods=['GET'])
def get_document():
    param = request.args.get('param')  
    # Accessing param2 from query string
    if param is None:
        return jsonify({"error": "Missing parameters"}), 400
    data = fetch_data(param)
    if 'data' not in data or not data['data']:
        return jsonify({"error": "No data found"}), 404
    print(len(data["data"][0]), 'bal')
    return jsonify(data)


#------------------------------------------------------- Get All ALl type of doctype data ---------------------------------------------------------------------
def fetch_all_data(doctype_name):
    url = f"https://ecommerce.ionicerp.xyz/api/resource/{doctype_name}?fields=[\"*\"]&limit_page_length=99"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "token 84859bedced40f4:02fbdaed78fefbb"
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
    # Get the doctype name from query parameters
    doctype_name = request.args.get('doctype_name')
    
    if not doctype_name:
        return jsonify({"error": "Missing doctype_name parameter"}), 400
    
    data1 = fetch_all_data(doctype_name)
    
    # Check if the 'data' key exists in the response
    if 'data' in data1:
        return jsonify(data1)
    else:
        # Handle the case where 'data' key is missing
        return jsonify({"error": "No data found", "response": data1})
    


    
    
# ----------------------------------------------------------------- POST data any Panal & any Doctype-----------------------------------------
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  
    # Post the received data to another URL
    post_data_to_another_url(data)
    return data

def post_data_to_another_url(data):
    # print(data)
    
    # Define the URL to post the data to
    url = f"https://{data['server']}/api/resource/{data['doctype']}"

    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            # "Authorization" : "token 7b052228a6fd29d:7f323743adf2694"
            "Authorization" : data['Authorization']
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
