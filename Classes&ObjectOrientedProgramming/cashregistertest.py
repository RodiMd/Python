#Cash Register
#the class should have the following methods:
#purchaseItem accepting and retain item
#getTotal - returns the total price for all items
#showItem - displays data about retaiItem
#clear - which clears the cash register
#allow ot select several items for checkout, once ready to checkout
#display all items in cart.

import retailitemclass

def main():

    addItem = addAnotherItem()    

def addAnotherItem():

    another = 'y'
    itemsInBag = {}
    
    while another.lower() != 'n':
        addToCart = addItems(itemsInBag)
        another = input('Would you like to add an item to cart?y = yes, n = no ')
        x += oneTimePrice(itemPrice)
    print(addToCart)
    print(x)
def addItems(itemsInBag):

    itemName = input('Enter the name of the item added to bag ')
    itemQuantity = float(input('Enter the quantity added to bag '))
    itemPrice = float(input('Enter the price of the item per unit '))

    itemInfo = retailitemclass.RetailItem(itemName, itemQuantity, itemPrice)
    totalItemCost = itemPricee(itemInfo.get_unitsInInventory(), itemInfo.get_price())

    oneTP = oneTimePrice(itemInfo.get_price)
    
    itemsInBag[itemName] = (itemQuantity, totalItemCost)

    return itemsInBag

def itemPricee(itemQuantity, itemPrice):

    totalItemCost = itemQuantity * itemPrice
    
    return totalItemCost

def oneTimePrice(itemPrice):
    oneTP = itemPrice
    return oneTP
    
main()
