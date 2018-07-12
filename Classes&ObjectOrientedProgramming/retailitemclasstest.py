#Retail Item Class Test

import retailitemclass

def main():

    products = inventory()
    displayItem(products)
    
def inventory():
    inventories = []
    quantityOfInput = input('How many items you want to input? ')

    for i in range (0, int(quantityOfInput)):
        itemDescription = input('Enter the item\'s description ')
        unitsInInventory = input('Enter the item\'s quantity ')
        price = input('Enter the item\'s price per unit ')

        items = retailitemclass.RetailItem(itemDescription, unitsInInventory, price)
        inventories.append(items)
        
    return inventories

def displayItem(products):
    j = 0
    for item in products:
        j += 1
        print('item#', j, ' Description ', item.get_itemDescription(), ' Units in Inventory ', item.get_unitsInInventory(), ' Price ', item.get_price())
        print('-------------')
        
main()

