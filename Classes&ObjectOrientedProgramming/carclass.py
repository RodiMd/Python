#Car Class
#data attributes to be included
#1. __year_model
#2. __make
#3. __speed
#__init__ method that accepts the __year_model and __make, and should assign 0 to __speed
#the class should also have the following methods
#1. accelerate - add 5 to the speed data attribute each time it is called
#2. brake - subtract 5 from speed data each time it is called
#3. get_speed - return current speed

class Car:

    def __init__(self, year_model, make, speed, accelerate, breakk):
        
        self.__year_moder = year_model
        self.__make = make
        self.__speed = speed
        self.__accelerate = accelerate
        self.__breakk = breakk

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    def set_accelerate(self, accelerate):
        self.__accelerate = 5

    def set_break(self, breakk):
        self.__breakk = -5

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def get_accelerate(self):
        return self.__accelerate

    def get_breakk(self):
        return self.__breakk

    
