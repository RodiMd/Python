#Personal Information
#design a class to hold: name, address, age, phone#
#write appropriate accessor and mutator methods
#write a program that creates three instances of a class
#instance1: hold info, instance2: hold friends and family info

class PersonalInfo:

    def __init__(self, name, address, age, phone_No):

        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_No = phone_No

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_No(self, phone_No):
        self.__phone_No = phone_No

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_No(self):
        return self.__phone_No
        
        
        
