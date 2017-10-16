def hello():
    """ prints hello, world """
    print("Hello, world!")
def areacircle(radius):
    """ Computes the area of a circle of the given radius """
    area = 3.14*radius**2
    print("The area of a circle of radius",radius,"is", area)
def areatriangle(b,h):
    area = 0.5*b*h
    print("The area of a triangle is", area)    
def fahrenheit_to_celsius(temp):
    """ Converts Fahrenheit temperature to Celsius. 
        Formula is 5/9 of temp minus 32 """
    # Note that this line is not executed
    # end='' keeps print from starting a new line.
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to",newTemp,end='')
    print(" degrees Celsius")
def celsius_to_fahrenheit(temp):
    newTemp = (9/5*(temp))+32
    print("The Celsius temperature",temp,"is equivalent to",newTemp,end='')
    print(" degrees Fahrenheit")   
def name():
    """ Input first and last name, combine to one string and print """
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    city = input("Enter the city you live in: ")
    state = input("Enter the state you live in: ")
    fullname = fname + " " + lname
    print("Your name is:", fullname, "City: ", city, " state", state)
def absolutevalue(num):
    if num>0:
        print(num)
    elif num<0:
        print(-1*num)    
def fahrenheit_to_celsius3():
    """ Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    Uses if to check whether input is a number and then uses .isdigit() method 
    of strings to check whether input is made of digits. 
    """
        
    temp_str = input("Enter a Fahrentheit temperature: ")
    if temp_str:
        if temp_str.isdigit():  
            temp = int(temp_str)
            newTemp = 5*(temp-32)/9
            print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
            print(newTemp,"degrees Celsius")
        else:
            print("You must enter a number. Bye")
def inches_to_feet1(inches):
    """ converts inches to feet and inches """
    feet = inches//12  # division by integer with fraction thrown away
    extra_inches = inches%12
    print(inches,"inches is",feet,"feet and",extra_inches,"inches") 
def cheer2():
    """ Same as cheer, but uses a for loop and range()
    range uses a start number, a stop number and a step size. """
    for ct in range(2,9,2):
        print(ct,end=' ')
    print()
    print("Who do we appreciate?")
    print("COURSERA!")  
def countdown1():
    for ct in range(10,0,-1):
        print(ct,end=' ')
    print("BlastOff!")
    print("Who do we appreciate?")
    print("COURSERA!")  
def favorite():
    my_toy = input("What is my favorite toy? ")
    print("Your favorite toy is", my_toy)
    