# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
# this has a time complexity of n**2 and space coplexity of n and it would be solved using array
def find_winner(n,k):
    #creating n =4 , arr=[1,2,3,4]
    arr = [i+1 for i in range(n)]
    def helper(arr, start_index):
        #base case
        if len(arr)==1 : return arr[0]
        # recursive condtion
        index_to_remove = (start_index + k -1) % len(arr)
        del arr[index_to_remove]
        return helper(arr,index_to_remove)
    return helper(arr, 0)