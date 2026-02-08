# https://leetcode.com/problems/combination-sum/description/
# N = number of candidates, T = Target, M = minimum value among candidates
# Maximum depth = T/M
# Time complexity = 0 (N ^(T/M + 1))  & Space Complexity = 0 (T/M) 
def combination_sum(candidates,target):
    result = []
    n=len(candidates)
    #candidates = sorted(candidates) # not necessary but for more speed
    def helper(start_index, current, sum_included):
        #base case
        if sum_included > target :
            return
        if sum_included == target:
            result.append(current[:])
            return
        
        #recursive case
        for j in range(start_index, n):
            current.append(candidates[j])
            helper(j,current,sum_included+candidates[j])
            current.pop()
    helper(0, [],0)
    return result