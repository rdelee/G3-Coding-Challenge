import numpy 
import json

#returns a python dict that contains deals data

def getDealsFromJason(deals_json):    
	return(json.loads(deals_json))


#To DO - Add a fuction for spliting up deals into individual python objects

#Nexsted classes to refelct the normalized data
#deals_data is a python object that carries all the info about a single deal

#initialization order : deals-> counter_party -> instrument -> deal_data

class deal_data:

	def __init__(self,instrument, deal, counter_party):
		self.deal = deal
		self.coutner_party = counter_party
		self.instrument = instrument


class deal:
	def __init__(deals_json):
		self.__price = deals_json['deal']['price']
		self.type = deals_json['deal']['type']
		self.quantity = deals_json['deal']['quantity']
		self.deal_id = deals_json['deal']['deal_id']

class counter_party:
	def __init(deals_json):
		self.name  = deals_json['counter_party']['name']
		self.status = deals_json['counter_party']['quantity']
		self.date_registered = deals_json['counter_party']['time']

class instrument:
	def __init__(deals_json):
		self.instrument_id = deals_json['instrument']['instrumentName']
		self.name = deals_json['instrument']['name']

