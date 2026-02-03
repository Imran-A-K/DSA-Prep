# https://leetcode.com/problems/subsets/description/
# time complexity T = O(n*2^n) and space complexity S = O(n*2^n)
# this problem is also known as power sets
def power_set(nums):
    output = []
    def helper( nums, i , subset):
        if i == len(nums) :
             output.append(subset.copy()) 
             return
        helper(nums, i + 1, subset)
        subset.append(nums[i])
        helper(nums, i + 1, subset)
        subset.pop()
    helper(nums, 0, [])
    return output