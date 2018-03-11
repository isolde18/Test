#enter password
#the program waits until a password
#has been entered
#use control-c to break out
#without the password

#NOTE that this must not be the password so that the
#while loop runs at least once

password = str ()

#not that != means not equal
while password != "unicorn":
    password = input ("password: ")
print ("welcome in")
