

a = 1
s = 0
print ('enter numbers to add to the sum ')
print ('enter 0 to quit ')
while a != 0:
    print ('current sum:', s)
    a = float (input('number? '))
    s = s + a
print ('total sum =' ,s)
#notice how print ('total sum = ',s )is only run at the end.
#the while statement only affects the lines that are intended
#with whitespace.the != means does not equal so while a !=0:
#means as long as a is not zero run the tabbed stattements that follow

#note that a is a floating point number, and not all floating numbers can be accurately represented
#so using != on them can sometimes not work.
#try typing in 1.1 in interactive mode.
    
