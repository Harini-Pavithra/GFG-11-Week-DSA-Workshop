Number is sparse or not 

Given a number N. The task is to check whether it is sparse or not. A number is said to be a sparse number if no two or more consecutive bits are set in the binary representation.

Example 1:

Input: N = 2
Output: true
Explanation: Binary Representation of 2 is 10, 
which is not having consecutive set bits. 
So, it is sparse number.
Example 2:

Input: N = 3
Output: false
Explanation: Binary Representation of 3 is 11, 
which is having consecutive set bits in it. 
So, it is not a sparse number.

Your Task: The task is to complete the function checkSparse() that takes n as a parameter and returns true if the number is sparse else returns false.


Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106

Solution

#User function Template for python3

##Complete this function
def isSparse2(n):
    #this is more efficient because we do not use any loop
    if n & (n>>1) == 0:
        return True
    else:
        return False

def isSparse(n):
    c=0
    while(n>0):
        if (n%2 == 0):
            c=0
        elif (n%2==1):
            c=c+1
        if c>=2:
            return False
        n=n//2
    return True



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

