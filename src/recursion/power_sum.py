"""
Coding Exercise: Power Sum

Instructions

Question:

Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2

another example - [1,2,[7,[3,4],2]] = 1 + 2 +( 7+(3+4)^3+2)^2
"""
#time complexity is O(N) - ( here N is total number of elemetns including array like for this case [1,2,[7,[3,4],2]] the N is 8) + space complexity O(D) D = the maximum depth of the call stack


def power_sum(array, power=1):
    total = 0
    for i in array:
        if type(i) == list : 
            total += power_sum(i,power+1)
        else :  
            total += i
    return total**power
