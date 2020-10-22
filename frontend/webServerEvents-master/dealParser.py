import numpy 
import json


def getDealsFromJason(self):   #returns a python dict that contains deals data 
	return (json.loads(self))


# calculates the deal price for from the python object passed 
def calculateNextPrice(self, direction):
    newPriceStarter = self.__price + numpy.random.normal(0,1)*self.__variance + self.__drift
    newPrice = newPriceStarter if (newPriceStarter > 0) else 0.0
    if self.__price < self.__startingPrice*0.4:
        self.__drift =( -0.7 * self.__drift )
    self.__price = newPrice*1.01 if direction=='B' else newPrice*0.99
    return self.__price