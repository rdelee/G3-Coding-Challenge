from flask import Flask, render_template, Response
from flask_sse import sse
from flask_cors import CORS
import requests
import time
import json
import os
#import 'dealParser.py' as dp


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
            
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, str(time.time()))
            if not os.path.exists(final_directory):
                os.makedirs(final_directory) 
            
            for line in r.iter_lines( chunk_size=1):
                if line:
                    # send normalized data to dealParser
                    #json_to_py(line)

                    current_deal_json =json.loads(line.decode())
                    with open(os.path.join(final_directory, str(time.time())),'w') as jsonFile:
                        json.dump(current_deal_json, jsonFile)

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


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()

