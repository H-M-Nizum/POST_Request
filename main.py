from flask import Flask, jsonify, request
from flask_cors import CORS
import os

# Sample data
import requests

def fetch_data(param1):
    url = f"""https://erp.gawsiashop.com.bd/api/resource/Item?filters=[["item_group", "=", "{param1}"]]&fields=["*"]&limit_page_length=99"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "token 092867a6814bfc7:bcc0df87d4b1a77"
    }
    payload = {
        "param1": param1
    }
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


app = Flask(__name__)
CORS(app) 
@app.route('/get', methods=['GET'])
def get_document():
    param1 = request.args.get('param1')  
    # Accessing param2 from query string
    if param1 is None:
        return jsonify({"error": "Missing parameters"}), 400
    data = fetch_data(param1)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

