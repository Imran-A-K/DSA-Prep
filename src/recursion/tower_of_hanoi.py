# https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1
# space complexity O(n) and time complexity O(2**n)
def toh(N, starting_rod, destination_rod, helper_rod):
    count = 0

    def helper(n, start, dest, aux):
        nonlocal count
        #base case
        if n == 1:
            print(f"move disk 1 from rod {start} to rod {dest}")
            count += 1
            return
        #recursive case
        helper(n - 1, start, aux, dest)
        print(f"move disk {n} from rod {start} to rod {dest}")  # <-- FIXED
        count += 1
        helper(n - 1, aux, dest, start)

    helper(N, starting_rod, destination_rod, helper_rod)
    return count
