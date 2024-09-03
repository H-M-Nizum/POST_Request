from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import json


def fetch_data(param):
    url = f"""https://erp.gawsiashop.com.bd/api/resource/Item?filters=[["item_group", "=", "{param}"]]&fields=["*"]&limit_page_length=99"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "token 092867a6814bfc7:bcc0df87d4b1a77"
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


#----------------------------------------------------------------------------------------------------------------------------
def fetch_all_data():
    url = f"""https://erp.gawsiashop.com.bd/api/resource/Item Group?fields=["*"]&limit_page_length=99"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "token 092867a6814bfc7:bcc0df87d4b1a77"
    }
    # Assuming you want to use param1 and param2 in the request
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/getall', methods=['GET'])
def get_all_documents():
    
    data = fetch_all_data()
    print(len(data["data"][0]))
    return jsonify(data)


    
    
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
    url = f"https://{data['server']}.ionicerp.xyz/api/resource/{data['doctype']}"

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

