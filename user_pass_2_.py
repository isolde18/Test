


#another way of username_pass
#after type lock to lock
#dont know what happens
#last two lines not working

name = input ("Set name: ")
password = input ("Set password: ")
while 1==1:
    nameguess=""
    passwordguess=""
    key=""
    while (nameguess !=name) or (passwordguess != password):
        nameguess=input ("Name? ")
        passwordguess=input ("Password? ")
    print ("Welcome,",name, ".Type lock to lock.")
    while key != "lock":
        key = input ("")
        
        

