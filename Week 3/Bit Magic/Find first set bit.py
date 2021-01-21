Find first set bit

Given an integer an N. The task is to return the position of first set bit found from the right side in the binary representation of the number.
Note: If there is no set bit in the integer N, then return 0 from the function.  

Example 1:

Input: N = 18
Output: 2
Explanation: Binary representation of 
18 is 010010,the first set bit from the 
right side is at position 2.
Example 2:

Input: N = 12 
Output: 3 
Explanation: Binary representation 
of  12 is 1100, the first set bit 
from the right side is at position 3.
Your Task:
The task is to complete the function getFirstSetBit() that takes an integer n as a parameter and returns the position of first set bit.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
0 <= N <= 106

Solution

#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends

#User function Template for python3

##Complete this function
def getFirstSetBit(n):
    #Your code here
    i=0
    if n == 0:
        return 0
    while(n>0):
       if n%2 == 1:
           return i+1
       i=i+1
       n=n//2

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        print(getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends