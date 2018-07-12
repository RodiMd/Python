#shipping charges
# 2 lb =$1.1
# > 2 & 6 < lb = $2.2
# > 6 & 10 < lb = $3.7
# > 10 lb = $3.8

weightFPckg = input('Enter the weight of package ')
weightFPckg = float(weightFPckg)

def main():
    if weightFPckg <= 2:
        totalCost = weightFPckg * 1.1
        print('Shipping cost is %.2f' %totalCost)
    elif weightFPckg > 2 and weightFPckg <= 6:
        totalCost = weightFPckg * 2.2
        print('Shipping cost is %.2f' %totalCost)
    elif weightFPckg > 6 and weightFPckg <= 10:
        totalCost = weightFPckg * 3.7
        print('Shipping cost is %.2f' %totalCost)
    else:
        if weightFPckg > 10:
            totalCost = weightFPckg * 3.8
            print('Shipping cost is %.2f' %totalCost)
main()
        
