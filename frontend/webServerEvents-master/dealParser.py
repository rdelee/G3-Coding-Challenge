import numpy 
import json

#returns a python dict that contains deals data

def getDealsFromJason(deals_json):    
	return(json.loads(deals_json))


#To DO - Add a fuction for spliting up deals into individual python objects




# calculates the deal price for from the python object passed 
# Pass one deal at a time to this fuction
def (self, direction):
    newPriceStarter = self.__price + numpy.random.normal(0,1)*self.__variance + self.__drift
    newPrice = newPriceStarter if (newPriceStarter > 0) else 0.0
    if self.__price < self.__startingPrice*0.4:
        self.__drift =( -0.7 * self.__drift )
    self.__price = newPrice*1.01 if direction=='B' else newPrice*0.99
    return self.__price