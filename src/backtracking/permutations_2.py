#https://leetcode.com/problems/permutations-ii/description/
# space complexityO(N) and time complexity O(n!*n)

def permute_unique(nums):
    result = []
    n = len(nums)
    def helper(index):
        #base case
        if index == n:
            result.append(nums[:])
        #recursive case
        hash={}
        for j in range(index, n):
            if nums[j] not in hash:
                hash[nums[j]]=True
                nums[index],nums[j]=nums[j],nums[index]
                helper(index+1)
                nums[index],nums[j]=nums[j],nums[index]    
    helper(0)
    return result