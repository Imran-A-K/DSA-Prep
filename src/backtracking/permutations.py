# https://leetcode.com/problems/permutations/description/
# space complexityO(N) and time complexity O(n!*n)
def permute(nums):
    n = len(nums)
    result = []
    """
    if not nums:
    return [[]]  -  I can give this part or the base case can be  if index == n:
            result.append(nums[:]) - originally it was index == n-1
    """
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