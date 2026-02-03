"""
https://leetcode.com/problems/monotonic-array/description/
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""
# The interviewer told that the Array is pre sorted
# Empty array is also to be treaten as Monotonic array



def is_monotonic(array):
    array_length=len(array)
    if array_length==0: return True
    first_value=array[0]
    last_value=array[array_length-1]
    if first_value > last_value:
        #Monotonically decreasing
        for i in range(array_length-1):
            if array[i]<array[i+1]: return False
            
    elif first_value == last_value:
        #Monotonic as all values are equal
        for i in range(array_length-1):
            if array[i]!=array[i+1]: return False
        
    else:
        #first_value<last_value
        #Monotonically increasing
        for i in range(array_length-1):
            if array[i]>array[i+1]: return False
    return True
