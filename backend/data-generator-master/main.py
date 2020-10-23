from flask import Flask, Response, render_template, jsonify
from flask_cors import CORS
import webServiceStream
from RandomDealData import *
import mysql.connector
from mysql.connector import errorcode
import requests

try:
    cnx = mysql.connector.connect(host='localhost', database='mysql-server',user='root',password='')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

#with open('./data.json','r+') as myfile:
#        data = myfile.read()

@app.route('/jsontest')
def streamjson():
    return webServiceStream.send_file()
    #return jsonify(data)

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()


@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()


def bootapp():
    # global rdd 
    # rdd = RandomDealData()
    # webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
