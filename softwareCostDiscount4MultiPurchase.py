# Software purchase discount

fullPrice = 99.0
fulPrice = float(fullPrice)

def main():
    quantityPurchased = input('Enter the quantity purchsed ')
    quantityPurchased = float(quantityPurchased)
    
    if quantityPurchased < 10:
        price = fullPrice * quantityPurchased
        print('For a purchase of less than 10, the total cost is %.2f ' %price)
    elif quantityPurchased >= 10 and quantityPurchased <= 19:
        discountPrice = float(quantityPurchased)*(fullPrice - 0.2 * fullPrice)
        print('For a multi purchase of greater than 10 and less than 19 the discount price is %.2f' %discountPrice)
        
    elif quantityPurchased > 19 and quantityPurchased <= 49:
        discountPrice = float(quantityPurchased)*(fullPrice - 0.3 * fullPrice)
        print('For a multi purchase of greater than 20 and less than 50 the discount price is %.2f ' %discountPrice)
        
    elif quantityPurchased > 49 and quantityPurchased <= 99:
        discountPrice = float(quantityPurchased)*(fullPrice - 0.4 * fullPrice)
        print('For a multi purchase of greater than 50 and less than 100 the discount price is %.2f ' %discountPrice)
        
    else:
        if quantityPurchased >= 100:
            discountPrice = float(quantityPurchased)*(fullPrice - 0.5 * fullPrice)
            print('For a multi purchase of greater than 100 then the discount price is %.2f ' %discountPrice)
main()
