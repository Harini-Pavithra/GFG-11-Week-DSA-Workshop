Digits In Factorial

Given an integer N. Find the number of digits that appear in its factorial. 
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
 

Example 1:

Input: N = 5
Output: 3
Explanation: Factorial of 5 is 120.
Number of digits in 120 is 3 (1, 2, and 0)
 

Example 2:

Input: N = 120
Output: 199
Explanation: The number of digits in
120! is 199

Your Task:
You don't need to read input or print anything. Your task is to complete the function digitsInFactorial() that takes N as input parameter and returns number of digits in factorial of N.


Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)


Constraints:
1 ≤ N ≤ 104

Solution:

#User function Template for python3

def digitsInFactorial(N):
    count =0
    if N <=1:
        return 1
    while N>0:
        count +=math.log10(N)
        N -=1
    return math.ceil(count)
    # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

