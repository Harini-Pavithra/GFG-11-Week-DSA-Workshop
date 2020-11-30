Exactly 3 Divisors

Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

 

Example 1:

Input:
N = 6
Output: 1
Explanation: The only number with 
3 divisor is 4.
 

Example 2:

Input:
N = 10
Output: 2
Explanation: 4 and 9 have 3 divisors.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function exactly3Divisors() that takes N as input parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

 

Expected Time Complexity : O(N1/2 * N1/4)
Expected Auxilliary Space :  O(1)

Constraints :
1 <= N <= 109

Solution:

#{ 
#Driver Code Starts
#Initial Template for Python 3


import math


 # } Driver Code Ends

#User function Template for python3

def exactly3Divisors(N):
    # code here
    def isPrime(i):
        i=2
        while i<=math.sqrt(N):
            if N%i==0:
                return False
            i +=1
        return True
    count =0
    i=2
    while i<N and (i*i)<=N:
        if isPrime(i):
            count +=1
    return count


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        print(exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends