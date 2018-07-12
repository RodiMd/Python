#personal information module


import personalinformationclass

def main():

    count = int(input('How many persons would you like to add? '))

    for i in range(0, count):
        try:
            cat = int(input('the following person is a: 1.Creator 2. Family member, 3. Friend? '))
        except:
            print('Enter a value 1, 2, or 3')
            cat = int(input('the following person is a: 1.Creator 2. Family member, 3. Friend? '))

        name = input('Enter first and last name ')
        address = input('Enter email address ')
        age = input('Enter the age of the person you are adding ')
        phone_No = input('Enter the phone number ')
        person = personalinformationclass.PersonalInfo(name, address, age, phone_No)
        
        if cat == 1:
            creatorsList = Creator(person.get_name, person.get_address, person.get_age, person.get_phone_No)
            for item in Creator(name, address, age, phone_No):
                print('The name of the creator is ', item.get_name())
                print('The creator\'s email is ', item.get_address())
                print('The creator\'s age is ', item.get_age())
                print('The creator\'s phone No.', item.get_phone_No())
                print('-------------------')
        elif cat == 2:
            familyList = Family(person.get_name, person.get_address, person.get_age, person.get_phone_No)
            for item in Family(name, address, age, phone_No):
                print('The name of the family member is ', item.get_name())
                print('The family member\'s email is ', item.get_address())
                print('The family member\'s age is ', item.get_age())
                print('The family member\'s phone No.', item.get_phone_No())
                print('-------------------')
        elif cat ==3:
            friendList = Friend(person.get_name, person.get_address, person.get_age, person.get_phone_No)
            for item in Friend(name, address, age, phone_No):
                print('The name of the friend is ', item.get_name())
                print('The friend\'s email is ', item.get_address())
                print('The friend\'s age is ', item.get_age())
                print('The friend\'s phone No.', item.get_phone_No())    
                print('-------------------')
def Creator(name, address, age, phone_No):
    creatorsList = []
    creators_List = personalinformationclass.PersonalInfo(name, address, age, phone_No)
    creatorsList.append(creators_List)
    return creatorsList

def Family(name, address, age, phone_No):
    familyList = []
    family_List = personalinformationclass.PersonalInfo(name, address, age, phone_No)
    familyList.append(family_List)
    return familyList

def Friend(name, address, age, phone_No):
    friendList = []
    frien_List = personalinformationclass.PersonalInfo(name, address, age, phone_No)
    friendList.append(friend_List)
    return friendList        

main()
   
