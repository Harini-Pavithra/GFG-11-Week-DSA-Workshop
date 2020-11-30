GP Term 

Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Example 1:

Input:
A = 2 
B = 3
N = 1
Output: 2
Explanation: The first term is already
given in the input as 2
Example 2:

Input:
A = 1
B = 2
N = 2
Output: 2
Explanation: Common ratio = 2,
Hence second term is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function termOfGP() that takes A, B and N as parameter and returns Nth term of GP. The return value should be double that would be automatically converted to floor by the driver code.

Expected Time Complexity : O(logN)
Expected Auxilliary Space : O(1)

Constraints:
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Solution:
#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends

#User function Template for python3

#Compelte his function
def termOfGP(A,B,N):
    #Your code here
    CP = B/A
    if N==1:
        return A
    if N==2:
        return B
    else:
        result = A * (CP**(N-1))
        return result
        



#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        
        print(math.floor(termOfGP(A,B,N)))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends