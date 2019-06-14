#-*- coding: utf8 -*-
from flask import Flask
from flask import *
from flaskext.mysql import MySQL
from flask_basicauth import request
from flask_basicauth import BasicAuth
import json
import requests
import time
import pymysql
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'test_database'
app.config['MYSQL_DATABASE_HOST'] = '203.154.83.124'
app.config['MYSQL_DATABASE_PORT'] = 3306

app.config['BASIC_AUTH_USERNAME'] = 'sdi'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

secure_my_api = BasicAuth(app)

mysql = MySQL()
mysql.init_app(app)


@app.route('/users', methods = ['POST'])
@secure_my_api.required

def db():
    conn = mysql.connect()
    cursors = conn.cursor()
    results = request.json
    usernames= results["username"]
    password = results["password"]
    times = time.time()
    try:
        sql = """Insert into users (username,password,create_time)values(%s,%s,%s)"""
        value=(usernames,password,times)
        cursors.execute(sql, value)

    except Exception as e:
        print e
        return "failed"
    conn.commit()
    conn.close()

    ans(usernames)
    return "ok"
def ans(username):

    url = "https://notify-api.line.me/api/notify"

    payload = "message=%s" % username
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer GAhSF7cqYkrhWh7FuEJxnjrffyd6AGWIAZuNVMzlN6N",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "89cbcb24-a666-4bcd-95b8-3074f963d787,8ba9b0de-c7aa-407b-8801-f83d8f1e8300",
        'Host': "notify-api.line.me",
        'accept-encoding': "gzip, deflate",
        'content-length': "21",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    # return "ok"
app.run(debug=True,host='127.0.0.1',port=5000)
