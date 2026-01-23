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
    total_indexes=len(array)
    left_pointer,right_pointer=0, total_indexes-1
    result=[0]*total_indexes
    for i in reversed(range(total_indexes)):
        lsq = array[left_pointer]**2 
        rsq = array[right_pointer]**2
        if lsq > rsq:
            result[i]=lsq
            left_pointer+=1
        else:
            result[i]=rsq
            right_pointer-=1
    return result



