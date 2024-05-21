from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app) 
@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  
   
    print('Received data:', data)
    
    # Post the received data to another URL
    post_data_to_another_url(data)


    return data

def post_data_to_another_url(data):
    print(data)
    
    # Define the URL to post the data to
    url = f"https://{data['server']}.ionicerp.xyz/api/resource/{data['doctype']}"

    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization" : "token 7b052228a6fd29d:7f323743adf2694"
        }
    #     # Post the data to the other URL
    #     # response = requests.post(another_url, json=data)
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status() 
        print('Data posted to another URL successfully')
        print(response)
    except requests.exceptions.RequestException as e:
        print('Error posting data to another URL:', e)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  
