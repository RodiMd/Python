# Calories Burned
#3.9 calories /min burned
# write a program that count calories after 10, 15, 20, 25 & 30 minutes

#calsBrnd = 3.9 # calories burned per minute

for time in range(5, 35, 5):
    global calsBrnd
    calsBrnd = 3.9 * time
    print ('At time ', time, 'The calories burned every 5minutes are %.2f ' %calsBrnd)

