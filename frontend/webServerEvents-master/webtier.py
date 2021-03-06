from flask import Flask, render_template, Response, jsonify
from flask_sse import sse
from flask_cors import CORS
import requests
import time
import json
import os
#import 'dealParser.py' as dp

DATA_FLAG = "JSON" # look in @app.route for info on this
#DATA_FLAG = "PYTHON"


#input : Normalized json containing one deal
#output : python object with same structure 
#access as following object_name.Deal.price, object_name.Instrument.instrument_id , object_name.Counter_party.name
def json_to_py(deal_json):
    return
    #return deal_PyObj = dp.convert_deals_to_pyObj(deal_jason)



app = Flask(__name__)
app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

@app.route('/file')
def readFILE():
    r = requests.get('http://localhost:8080/jsontest')
    def eventStream():
            
            for line in r.iter_lines( chunk_size=1):
                if line:
                    # send normalized data to dealParser
                    #json_to_py(line)
                    current_deal_json =json.loads(line.decode()) #convert incoming stream to json object

                    #if(DATA_FLAG == "PYHTON"):
                      #  json_to_py(current_deal_json)


                    yield line
    return Response(eventStream(), mimetype="text/json")

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():

            for line in r.iter_lines( chunk_size=1):
                if line:
                    # emit data as SSE
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are running..."

@app.route('/endpos')
def calc_pos():
    dealer = 'Jupiter'
    #Attempt to access specific parts of stream to get deal Price
    # Could not get that info
    #could use 8090/file if doing in front-end
    r = requests.get('http://localhost:8080/jsontest')
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    # emit data as SSE
                    l = json.loads(line)
                    yield '{}\n\n'.format(l)
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/get_test_data')
def get_deals_json():
    list_deals = []

    r = requests.get('http://localhost:8080/jsontest')
    def eventStream():
        for line in r.iter_lines( chunk_size=1):
                if line:
                    current_deal_json =json.loads(line.decode()) #convert incoming stream to json object
                    list_deals.append(current_deal_json)
                    yield line
    '''
    deal_1 = {
        'instrument': {
            'Instrument_Name': 'Eclipse',
            'instrument_id': '654'
        },
        'deal' : {
            'Deal_Id': '456',
            'Price' : '45',
            'Type': 'S',
            'Quantity': '3',
            'Time': '26-sep-2020 (12:35:17.152282)'
        },
        'counter_party' : {
        'counterparty_name': "Lewis",
        'counterparty_id': "07"
        }
    }
    # deal_1 = {
    #     "instrumentName": "Eclipse",
    #     "cpty": "Lewis",
    #     "price": "7743.939118689354",
    #     "type": "S",
    #     "quantity": "562",
    #     "time": "26-sep-2020 (14:40:17.152282)"
    # }
    # deal_2 = {
    #     "instrumentName": "Celestial",
    #     "cpty": "Nidia",
    #     "price": "73.86634",
    #     "type": "B",
    #     "quantity": "42",
    #     "time": "26-sep-2020 (12:35:17.152282)"
    # }

    list_deals.append(deal_1)
    list_deals.append(deal_2)
    '''



    return jsonify(list_deals)

def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()

