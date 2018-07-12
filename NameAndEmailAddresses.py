#Name and Email Addresses
#keep names and email addresses in a dictionary as key-value pairs.
#display a menu that lets the user lookup a person's email
#add a new name and email address
#change an existing email address
#delete an email address
#each time the program starts, it should unpickle it and retrieve all data

import pickle

def main():
#unpickling a file (note: unpickling may cause an eoerror, should use try/except to prevent)

    try:
        input_File = open('NameEmail.dat', 'rb')
        dicNameEmail = pickle.load(input_File)
    except:
        print('file does not exist')
        dicNameEmail = {}
    
    print('1:Lookup contact information, 2:Add a new contact, 3:Change an existing name, 4:Delete an email')
    userDesire = input('Enter the desired option from the menu displayed above ')
    try:
        if userDesire == "1":
            nameLookup = input('Enter the contact name searching for ')
            print(dicNameEmail[nameLookup])
            
        elif userDesire == "2":
            newContactName = input('Enter the contact name to be added ')
            newContactEmail = input('Enter the contact email to be added ')
            dicNameEmail[newContactName] = newContactEmail
            
        elif userDesire == "3":
            contactNameChange = input('Enter the name of contact information desired to change ')
            contactNewEmail = input('Enter the new e-mail desired to change for the contact ')
            dicNameEmail[contactNameChange] = contactNewEmail
        
        elif userDesire == "4":
            deleteContact = input('Enter the contact desired to be deleted ')
            del dicNameEmail[deleteContact]
    except:
        print('Error, contact not found or other')
#now we need to pickle the file - pickling = serializing.
#pickling is done by opening a file for binary writing, module's dump method
        
#        (pickle.dump(object, file)
    input_File.close()
    output_File = open('NameEmail.dat', 'wb')
    pickle.dump(dicNameEmail, output_File)
    output_File.close()
    
main()        
