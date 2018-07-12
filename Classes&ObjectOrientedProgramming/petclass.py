#Pet Class
#write a class named Pet, with the following attributes
#__name()
#__animalType
#__age
#__init__ method
#set_name
#set_animal_type
#set_age
#get_name
#get_animal_type
#get_age

class Pet:
    def __init__(self, name, animal_type, age):

        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
#set is the mutator method (called: setters)#
    def set_name(self, name):
        self.__name = name 
        
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
        
#get is the accessor method (called: getters)#
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

