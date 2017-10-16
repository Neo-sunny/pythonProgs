def problem1_7():
    b1=input('Enter the length of one of the bases: ')
    b2=input('Enter the length of the other base: ')
    h=input('Enter the height: ')
    area=(float(b1)+float(b2))*float(h)
    farea=area/2
    print("The area of a trapezoid with bases",float(b1),'and',float(b2),'and height',float(h),'is',farea)