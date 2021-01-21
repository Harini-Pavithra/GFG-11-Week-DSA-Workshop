Count total set bits

You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

Example 1:

Input: N = 4
Output: 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bits
For 2: 0 1 0 = 1 set bits
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bits
Therefore, the total set bits is 5.
Example 2:

Input: N = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), 
the total number of set bits is 35.

Your Task: The task is to complete the function countSetBits() that takes n as a parameter and returns the count of all bits.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106


solution
def countSetBits(n):
    n += 1
    count = 0
    
    x = 2
    while x//2 < n:
        
        quotient = n//x
        count += quotient * x // 2
        
        remainder = n % x
        if remainder > x//2:
            count += remainder - x//2
        
        x = x*2
    
    return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        print(countSetBits(int(input())))
# } Driver Code Ends