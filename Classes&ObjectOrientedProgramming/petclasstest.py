#create object of the pet
#accept input from user
#data should be stored as object's attrbutes
#use object's accessor methdos to retrieve the pet's name, type and age

import petclass #this is the name of the module/file

def main():
    pets = pet_List()
    display_List(pets)#display List calls the pets list to display it

def pet_List():
    #create a list to hold the pet information
    petList = []

    count = int(input('Enter how many dogs\' whould you like to enter? '))
    for i in range(0, count):
        name = input('Enter the name of your pet ')
        animal_type = input('Enter the type of animal ')
        age = input('Enter the age of your pet ')
    
#creates a pet object in memory and assigns pet variables to it
        pet = petclass.Pet(name, animal_type, age) #petclass (name of module) & Pet (name of Class)
        petList.append(pet)
    return petList

def display_List(pet_List):
    
    for item in pet_List:
        print ('The name of the pet ', item.get_name())
        print ('The type of the pet ', item.get_animal_type())
        print ('The pet is ', item.get_age(), ' years old')
        print('-------------------------------')

main()
