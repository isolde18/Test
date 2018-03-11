

#write a program that:
#asks for login name and password
#displays:to lock your computer type 'lock'
#'what's your command'
#user answer 'lock'
#program then asks
#your username; your password;
#so enter, none-none-lock;none-none or
#anything you want a-b-lock and repeat a-b to unlock
#displays the message: welcome back to your systema 

name = input  ("what is your UserName: ")
password = input ("what is your password: ")
print ("to lock your computer type lock ")
command=None
input1=None
input2=None
while command != "lock":
    command = input ("what is your command :")

while input1 != name:
    input1=input("what is your username: ")
while input2 != password:
    input2=input("what is your password: ")
print ("welcome back to your systema ")
    
   

