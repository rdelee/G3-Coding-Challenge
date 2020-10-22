import time
from flask import Flask, Response
from flask_cors import CORS
import numpy, random
from datetime import datetime, timedelta
import json
from RandomDealData import *

app = Flask(__name__)
CORS(app)
global batching_frequency
batching_frequency = 5 #seconds

def index():
    return "Data Generator is running..."

def testservice():
    rdd = RandomDealData()
    deal = rdd.createRandomData( rdd.createInstrumentList() )
    return Response( deal, status=200, mimetype='application/json')

def stream():
    rdd = RandomDealData()
    instrList = rdd.createInstrumentList()
    deal_list = []
    start_time = time.time()

    def eventStream():
        while True:
            #nonlocal instrList
            deal = rdd.createRandomData(instrList) + "\n"
            #Add deal data to deal_list
            deal_list.append(deal)
            send_json(deal_list,start_time)
            outfile = open('data.json', 'w')
            json.dump(deal_list, outfile)
            yield deal

    return Response(eventStream(), status=200, mimetype="text/event-stream")

def sse_stream():
    theHeaders = {"X-Accel-Buffering": "False"}
    rdd = RandomDealData()
    instrList = rdd.createInstrumentList()
    def eventStream():
        while True:
            #nonlocal instrList
            yield 'data:{}\n\n'.format(rdd.createRandomData(instrList))
    resp = Response(eventStream(), status=200, mimetype="text/event-stream")
    resp.headers["X-Accel-Buffering"] = "False"
    return resp


def get_time():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def batch(start_time):
    t = time.time()
    if float(t) - start_time >= batching_frequency:
        start_time = float(t)
        return True
    else:
        return False


def send_json(deal_list,start_time):
    if batch(start_time):
        #Insert normalize function here
        #yield deal_list
        #Send deal_list json file to webtier
        #print('in send_json')
        deal_list = []
        return True
    else:
        return False

def send_file():
    with open('./data.json', 'r+') as myfile:
        data = myfile.read()
    return data
