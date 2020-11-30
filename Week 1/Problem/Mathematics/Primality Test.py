Primality Test 

A prime number is a number which is only divisible by 1 and itself.
Given number N check if it is prime or not.

 

Example 1:

Input:
N = 5
Output: Yes
Explanation: 5 is a prime number.
 

Example 2:

Input:
N = 4
Output: No
Explanation: 4 is not a prime number.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function isPrime() that takes N as input parameter and returns True if N is prime else returns False. 

 

Expected Time Complexity : O(N1/2)
Expected Auxilliary Space :  O(1)

 

Constraints:
1 <= N <= 109

Solution:

#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends

#User function Template for python3
import math

def isPrime(N):
    # code here
    if N<=1:
        return False
    if N<=3:
        return True
    if N%2==0 or N%3==0:
        return False
    
    i=5
    while i*i <= N :
        if N%i==0 or N % (i+2)==0 :
            return False
        i=i+6
    return True
            


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        if(isPrime(N)):
            print("Yes")
        else:
            print("No")
        T-=1
    
    
if __name__=="__main__":
    main()
#} Driver Code Ends