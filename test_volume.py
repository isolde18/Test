#volume formulas
#calculations program
#Volume is measured in "cubic" units. The volume of a figure is the number of cubes required to fill it completely, like blocks in a box.
#Volume of a cube = side times side times side. Since each side of a square is the same, it can simply be the length of one side cubed.
#If a square has one side of 4 inches, the volume would be 4 inches times 4 inches times 4 inches, or 64 cubic inches.
#(Cubic inches can also be written in*3.)
#Be sure to use the same units for all measurements. You cannot multiply feet times inches times yards, it doesn't make a perfectly cubed measurement.
#The volume of a rectangular prism is the length on the side times the width times the height. If the width is 4 inches, the length is 1 foot and
#the height is 3 feet, what is the volume?

#NOT CORRECT .... 4 times 1 times 3 = 12

#CORRECT.... 4 inches is the same as 1/3 feet. Volume is 1/3 feet times 1 foot times 3 feet = 1 cubic foot (or 1 cu. ft., or 1 ft*3).

  	
 
  	
 

def cube(L):
    return L* L* L
def rectangular_prism(a,b,c):
    return a * b * c
def irregular_prism(pr_w,h): 
    return pr_w * h
def cylinder(radius,height):
    return 3.14159 * height *radius ** 2
def pyramid(p_height,p_length):
    return 1.0/3.0 * p_height * p_length
def cone(radius,cone_height):
    return 1.0/3.0 * 3.14159 * cone_height * radius**2
def sphere(radius):
    return 4.0/3.0 * 3.14159 * radius**3
def ellipsoid (radius1,radius2,radius3):
    return 4.0/3.0 * 3.14159 * radius1 * radius2 * radius3
def options():
    print()
    print ("Options:")
    print ("cu=calculate the volume of a cube")
    print ("r=calculate the volume of a rectangular prism")
    print ("i=calculate the volume of irregular prism")
    print ("c=calculate the volume of a cylinder")
    print ("p=calculate the volume of a pyramid")
    print ("co=calculate the volume of a cone")
    print ("sp=calculate the volume of a sphere")
    print ("e=calculate the volume of an ellipsoid")
    print ("q=quit")
    print()
print ("This program will calculate the volume of a cube, a rectangular prism, an irregular prism, a cylinder, a pyramid, a cone, a sphere or an ellipsoid.")
choice="x"
options()
while choice != "q":
    choice=input("Please enter your choice: ")
    if choice=="cu":
        L=float(input("Length of cube side: "))
        print("The volume of the cube is", cube(L))
        options()
    elif choice=="r":
        a=float(input("enter weight: "))
        b=float(input("enter length: "))
        c=float(input("enter height: "))
        print ("The volume of a rectangular prism is: ", rectangular_prism(a,b,c) )
        options()
    elif choice =="i":
        pr_w=float(input("enter weight : "))
        h=float(input("enter height: "))
        print("The volume of an irregular prism is: ", irregular_prism(pr_w,h))
        options()
    elif choice =="c":
        radius=float(input("enter radius: "))
        height= float(input("enter height: "))
        print("The volume of a cylinder is: ",cylinder(radius, height))
        options()
    elif choice=="p":
        p_height=float(input("enter height: "))
        p_length=float (input("enter length: "))
        print("The volume of a pyramid is: ", pyramid(p_height,p_length))
        options()
    elif choice =="co":
        cone_height=float(input("enter cone height: " ))
        radius=float(input("enter radius: "))
        print ("The volume of a cone is: ",cone(radius,cone_height))
        options()
    elif choice=="sp":
        radius=float(input("enter the radius: "))
        print ("The volume of a sphere is: ", sphere(radius))
        options()
    elif choice=="e":
        radius1=float(input("enter radius1: "))
        radius2=float(input("enter radius2: "))
        radius3=float(input("enter radius3: "))
        print("The volume of an ellipsoid is: ",ellipsoid(radius1,radius2,radius3))
        options()
    elif choice=="q":
        print(" ",end="")
    else:
        print ("Unrecognized option.")
        options()
        
        
