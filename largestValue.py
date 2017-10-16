


def getLargestVal():
    largest_so_far=-1   
    for num in [9,41,12,3,74,115]:
        if num>largest_so_far:
            largest_so_far=num
    print("Largest Value:-> ",largest_so_far)  


def getSmallestVal():
    smallest_so_far=None
    for num in [9,41,12,3,74,115]:
        if smallest_so_far is None:
            smallest_so_far=num
        elif num< smallest_so_far:
            smallest_so_far=num
    print("Smallest Value:-> ",smallest_so_far)
                       
getLargestVal()
getSmallestVal()