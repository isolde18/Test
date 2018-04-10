


classA=int(input("Enter tickets sold for class A "))
classB=int(input("Enter tickets sold for class B "))
classC=int(input("Enter tickets sold for class C "))

def expenses(a,b,c):
    totalA= a*20
    totalB=b*15
    totalC=c*10
    total=totalA+totalB+totalC
    print('Profit generated from class A=',totalA)
    print ('Profit generated from class B', totalB)
    print('Profit generated from class C', totalC)
    print('\noverall generated=',total)



expenses(classA,classB,classC)
