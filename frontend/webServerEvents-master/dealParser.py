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

	def __init__(self,instrument, deal, counter_party, deals_json):
		self.deal = deal
		self.coutner_party = counter_party
		self.instrument = instrument


class deal:
	def __init__(instrument):
		self.__price = deals_json['deal']['price']
		self.type = deals_json['deal']['type']
		self.quantity = deals_json['deal']['quantity']
		self.deal_id = deals_json['deal']['deal_id']

class counter_party:

	self.name  = deals_json['counter_party']['name']
	self.status = deals_json['counter_party']['quantity']
	self.date_registered = deals_json['counter_party']['time']

class instrument:
	def __init__(instrument):
		self.instrument_id = deals_json['instrument']['instrumentName']
		self.name = deals_json['instrument']['name']

# calculates the deal price for from the python object passed 
# Pass one deal at a time to this fuction
	def calculateNextPrice(self, direction):
    	newPriceStarter = self.__price + numpy.random.normal(0,1)*self.__variance + self.__drift
    	newPrice = newPriceStarter if (newPriceStarter > 0) else 0.0
   		if self.__price < self.__startingPrice*0.4:
        	self.__drift =( -0.7 * self.__drift )
    	self.__price = newPrice*1.01 if direction=='B' else newPrice*0.99
    	return self.__price