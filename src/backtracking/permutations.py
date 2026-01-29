# https://leetcode.com/problems/permutations/description/
def permute(nums):
    n = len(nums)
    result = []
    def helper(index):
        #base case
        if index == n:
            result.append(nums[:])
        # recursive case
        for j in range(index,n):
            nums[index],nums[j]= nums[j],nums[index]
            helper(index+1) #backtracking
            nums[index],nums[j]= nums[j],nums[index]
    helper(0)
    return result