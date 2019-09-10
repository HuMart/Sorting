# STRETCH: implement Linear Search	
# TO-DO: add missing code
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1   # not found
  


      


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(list, target, ):
    if len(list) == 0:
        return -1 # array empty    
    low = 0
    high = len(list)-1
    while low <= high:
        x = (low + high) // 2
        if list[x] == target:
           return x
        elif list[x] > target:
           high = x + 1
        else:
           low = x - 1
    return -1 # not found     

  # TO-DO: add missing code

  


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(list, target, low, high):
    if len(list) == 0:
        return -1 # array empty
    x = ( low + high) // 2
    if list[x] == target:
       return x
    elif list[x] < target:
       low = x - 1
       return binary_search_recursive(list, target, low, high)
    else:
       high = x + 1
       return binary_search_recursive(list, target, low, high)