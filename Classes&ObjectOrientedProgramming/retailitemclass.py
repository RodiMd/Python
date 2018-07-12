#Retail Item Class
#holds data about item in retail store
#attributes to be stored: item description, units in inverntory, price

#then write a program that creates three objects and store

class RetailItem:

    def __init__(self, itemDescription, unitsInInventory, price):

        self.__itemDescription = itemDescription
        self.__unitsInInventory = unitsInInventory
        self.__price = price
        
    def set_itemDescription(self, itemDescription):
        self.__itemDescription = itemDescription

    def set_unitsInInventory(self, unitsInInventory):
        self.__unitsInInventory = unitsInInventory

    def set_price(self, price):
        self.__price = price

    def get_itemDescription(self):
        return self.__itemDescription

    def get_unitsInInventory(self):
        return self.__unitsInInventory

    def get_price(self):
        return self.__price
