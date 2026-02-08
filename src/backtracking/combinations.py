# https://leetcode.com/problems/combinations/description/
# Time complextity = O( k x nCk) Space Complexity = O(K)

def combine(n,k):
    result = []
    def helper(start,current):
        #basecase
        if len(current) == k:
            result.append(current[:])
            return
        #optimizing according to need to save unnecessary iterations
        need = k - len(current)
        #recursive case
        #for j in range(start, n+1):
        for j in range(start, n-(need-1)+1):
            current.append(j)
            helper(j+1,current)
            current.pop()
    helper(1,[])
    return result