# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
# this has a time complexity of n and space coplexity of n

def find_winner(n,k):
    def josephus(n):
        if n==1 : return 0
        else:
            return (josephus(n-1) + k) % n 
    
    return josephus(n)+1
