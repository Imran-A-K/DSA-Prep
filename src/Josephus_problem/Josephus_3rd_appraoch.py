# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
# this has a time complexity of n and space coplexity of 1 best solution 

def find_winner(n,k):
    survivor = 0 
    for i in range(2, n+1):
        survivor = (survivor+k)%i
    return survivor +1
