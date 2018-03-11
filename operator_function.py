


#another feature of the if command is the elif statement
#it stands for else if and it means if the original if
#statement is false but the elif part is true, then do
#the elif part and if neither the if or elif expressions are
#true, then do what is in the else block

a=0
while a<10:
    a=a+1
    if a>5:
        print(a, ">",5)
    elif a<=3:
        print(a,"<=",3)
    else:
        print("Neither test was true")

#Notice how the elif a<=3 is only tested when the if statement fails to be true
#There can be more than one elif expression, allowing multiple tests to be done
#in a singleif statement
