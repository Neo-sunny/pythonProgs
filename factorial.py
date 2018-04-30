def calculate_factorial_multi(number):

    if number == 1 or number == 0:
        return 1

    result = 1 # variable to hold the result
	
    for x in xrange(1, number + 1, 1):
        result *= x
        print result
    return result
    
    
calculate_factorial_multi(100)    