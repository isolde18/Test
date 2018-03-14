#the program creates a positive integer multiplication system,
#and then demonstrates the use of recursion,that's a form of iteration
#repetition in which there is a function that repeaedly call itself until an exit condition is
#satisfied.It uses repeaed additions to give the same result as multiplication.
#eg.3+3 gives the same result as 3*2

def mult(a,b):
    if b==0:
        return 0
    rest=mult(a,b-1)
    value= a+rest
    return value

result=mult(3,2)
print ("3 *2 =",result)
