
#while loop
#control structure
#changes the order that statement are executed
#or decides if a certain statement will be run


keep_going = 'y'
while keep_going =='y':
    sales = float(input('enter sales amount: '))
    comm_rate = float(input('enter commission rate '))
    commission = sales* comm_rate
    print ('your commission is ',commission)
    print()
    keep_going = input (' do you want to calculate commission for another user? enter y if yes: ')
    print()
