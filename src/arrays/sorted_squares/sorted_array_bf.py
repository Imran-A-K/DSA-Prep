"""
You are given an array of Integers in which each subsequent value is not less than the previous value.
 Write a function that takes this array as an input and returns a new array with the squares of each number
   sorted in ascending order.

Clarifying Questions

Are all numbers positive?
-No, can be Not necessarily -ve or O also

-Are the Integers distinct? - Not necessarily

Can an empty array of Integers be given As input?

-Yes; return an empty array in this case

"""

# Brute force
def sorted_squares(array):
    n = len(array)
    result = [0]*n
    for i in range(n):
        result[i] = array[i]**2
    result.sort()
    return result

