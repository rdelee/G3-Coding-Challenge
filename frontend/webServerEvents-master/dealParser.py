
import json 

#Nexsted classes to refelct the normalized data
#deals_data is a python object that carries all the info about a single deal

#initialization order : deals-> counter_party -> instrument -> deal_data

class Deal_data:

	def __init__(self,instrument, deal, counter_party):
		self.deal = deal
		self.coutner_party = counter_party
		self.instrument = instrument


class Deal:
	def __init__(deals_dict):
		self.price = deals_json['deal']['price']
		self.type = deals_json['deal']['type']
		self.quantity = deals_json['deal']['quantity']
		self.deal_id = deals_json['deal']['deal_id']

class Counter_party:
	def __init__(deals_dict):
		self.name  = deals_json['counter_party']['name']
		self.status = deals_json['counter_party']['quantity']
		self.date_registered = deals_json['counter_party']['time']

class Instrument:
	def __init__(deals_dict):
		self.instrument_id = deals_json['instrument']['instrumentName']
		self.name = deals_json['instrument']['name']

#turns normalized json into a python dict
def getDealsFromJson(deals_json):    
    deals_as_py_dict = json.loads(deals_json)
    return deals_as_py_dict

# returns python object with all the deal data      
def create_deals_py_obj(deals_as_py_dict):
    
    instrument = Instrument(deals_as_py_dict)
    deal = Deal(deals_as_py_dict)
    counter_party = Counter_party(deals_as_py_dict)
    deal_data_py_obj = Deal_data(instrument, deal, counter_party)
    return deal_data_py_obj


def convert_deals_to_pyObj(json_data): 
    deals_as_pyDict = getDealsFromJsonToPy(json_data)
    deal_py_obj = create_deals_py_obj(deals_as_pyDict)
    return deal_py_obj