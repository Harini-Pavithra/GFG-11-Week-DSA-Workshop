Rightmost different bit

Given two numbers M and N. The task is to find the position of the rightmost different bit in the binary representation of numbers.

Example 1: 

Input: M = 11, N = 9
Output: 2
Explanation: Binary representation of the given 
numbers are: 1011 and 1001, 
2nd bit from right is different.
Example 2:

Input: M = 52, N = 4
Output: 5
Explanation: Binary representation of the given 
numbers are: 110100â€¬ and 0100, 
5th-bit from right is different.
User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two arguments m and n and returns the position of first different bits in m and n. If both m and n are the same then return -1 in this case.

Expected Time Complexity: O(max(log m, log n)).
Expected Auxiliary Space: O(1).

Constraints:
1 <= M <= 103
1 <= N <= 103

Solution

#{ 
#Driver Code Starts
#Initial Template for Python 3

import math




    
 # } Driver Code Ends

#User function Template for python3

##Complete this function
def posOfRightMostDiffBit(m,n):
    #Your code here
    if m > n:
        m, n = n, m
    i=1
    while (n > 0):

        if (m % 2) == (n % 2):
            pass
        else:
            return i
        m = m // 2
        n = n // 2
        i=i+1


#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends