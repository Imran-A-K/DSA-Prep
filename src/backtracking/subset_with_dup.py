# https://leetcode.com/problems/subsets-ii/description/
# time complexity T = O(n*2^n) and space complexity S = O(n)
def subset_with_dup(nums):
    nums.sort()
    result = []
    def helper(i,curr):
        #base case 
        if i == len(nums):
            result.append(curr[:])
            return
        #include case
        curr.append(nums[i])
        helper(i+1,curr)
        curr.pop()
        #exclue case
        while i < len(nums)-1 and nums[i]==nums[i+1]:
            i+=1
        helper(i+1,curr)
    helper(0,[])
    return result