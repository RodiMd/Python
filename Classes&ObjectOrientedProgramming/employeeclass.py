#Employee Class
#The write a class named employee, that holds data:
#name, ID num, department, job title.
#store data in 3 objects, display data for each emplyee.
#objects:
#Name, ID Number, Department, Job title

class Employee:

    def __init__(self, Name, ID_number, Department, Job_title):
        self.__Name = Name
        self.__ID_number = ID_number
        self.__Department = Department
        self.__Job_title = Job_title

    def set_Name(self, Name):
        self.__Name = Name

    def set_ID_Number(self, ID_Number):
        self.__ID_number = ID_number

    def set_Department(self, Department):
        self.__Department = Department

    def set_Job_title (self, Job_title):
        self.__Job_title
        
    def get_Name(self):
        return self.__Name
    
    def get_ID_number(self):
        return self.__ID_number

    def get_Department(self):
        return self.__Department

    def get_Job_title(self):
        return self.__Job_title
        
