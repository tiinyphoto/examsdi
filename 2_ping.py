import requests
import threading
import time
from flask import Flask ,request,jsonify
import subprocess
import json
import os

app_name = Flask(__name__)

@app_name.route('/api/v1/ping', methods = ['POST'])

def get_response():
    reciver_value = request.get_json()
    data = reciver_value['destination']
    value_data={}
    for i in data:
        start_time = time.time()
        response = os.popen('ping -c 2 ' + i)
        t=time.time()-start_time
        if i == 0:
            value_data[i] = t
        else:
            value_data[i]= t

    return jsonify(value_data),200

app_name.run(host="127.0.0.1")
