

#variable assignmetns inside a function do not override global variables
#they exist only inside the function
#more examples

a_var = 10
b_var = 15
e_var = 25

def a_func (a_var):
    print ("in a_func a_var =", a_var)
    b_var = 100 + a_var
    d_var = 2 * a_var
    print ("in a_func b_var =", b_var)
    print ("in a_func d_var =", d_var)
    print ("in a_func e_var =", e_var)
    return b_var + 10
c_var = a_func (b_var)

print ("a_var =", a_var)
print ("b_var =", b_var)
print("c_var =",c_var)
print ("d_var =", d_var)

#a_var,b_var,and d_var are all local variables
#when they are inside the function a_func
#after the statement return b_var + 10 is run,
#they all cease to exist
#the variable a_var is automatically a local var. since
#it is a parameter name
#the var.b_var and d_var are local variables,
#since they appear on the left of an equals sign
#in the function in the statement b_var =100 + a_var
#and d_var =2 * a_var

#inside the function a_var has no value assigned to it
#........
#all the local var.are deleted when the functon exits,(error d_var)
#f you want to get something from a function, you will have to use
#return something
#the value of e_var remains unchanged,inside a_func, since it's not a parameter,
#and it never appears on the left of an equals sign inside of the function a_func
