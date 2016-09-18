#Author: Remi Pelletier
#File:   rp_array_search.py
#Desc.:  Module containing various array search functions.


#Finds the position of an element (x)
#in the given array (arr) using binary search.
#The array needs to already be sorted.
#Returns -1 if the element is not found.
#Complexity: O(log(n))
def binary_search(arr, x, lo = 0, hi = -1):
    if x is None or arr is None or len(arr) == 0:
        return -1
    length = len(arr)
    lo %= length
    hi %= length # = to len(arr) - 1 when hi = -1 (default).
    while hi >= lo:
        mid = (hi + lo) // 2
        if arr[mid] == x:
            return mid
        if x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
    

#Finds the position of an element (x)
#in the given array (arr) using interpolation search.
def interpolation_search(arr, x):
    pass #TODO


#Finds the position of an element (x)
#in the given array (arr) using linear search.
#Returns -1 if the element is not found.
#Complexity: O(n)
def linear_search(arr, x):
    if x is None or arr is None or len(arr) == 0:
        return -1
    pos = 0
    for val in arr:
        if val == x:
            return pos
        pos += 1
    return -1


#Finds the position of the first element in the given
#array (arr) which doesn't evaluate to less than the
#given value (x) using binary search.
#The array needs to be already sorted.
#If no value is found within the given bounds hi + 1
#is returned ( = len(arr) by default).
#Complexity: O(log(n))
def lower_bound(arr, x, lo = 0, hi = -1):
    if x is None or arr is None or len(arr) == 0:
        return -1
    length = len(arr)
    lo %= length
    hi %= length # = to len(arr) - 1 when hi = -1 (default).
    while hi >= lo:
        mid = (hi + lo) // 2
        if arr[mid] >= x:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


#Finds the position of the first element in the given
#array (arr) which evaluates to greater than the
#given value (x) using binary search.
#The array needs to be already sorted.
#If no value is found within the given bounds hi + 1
#is returned ( = len(arr) by default).
#Complexity: O(log(n))
def upper_bound(arr, x, lo = 0, hi = -1):
    if x is None or arr is None or len(arr) == 0:
        return -1
    length = len(arr)
    lo %= length
    hi %= length # = to len(arr) - 1 when hi = -1 (default).
    while hi >= lo:
        mid = (hi + lo) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo



#Tests
arr = [1, 4, 7, 8, 15, 21, 23, 34]
x = 22
print(lower_bound(arr, x))