Print first n Fibonacci Numbers

Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:

Input:
N = 5
Output: 1 1 2 3 5
Example 2:

Input:
N = 7
Output: 1 1 2 3 5 8 13
Your Task:
Your task is to complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: This space is used to store and return the answer for printing purpose.

Constraints:
1<= N <=84

Solution

#User function Template for python3

class Solution:
    
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        
        #creating a list to store the numbers. 
        res = []
        
        #storing base values for a and b.
        a=b=1
        
        #pushing 1 once in the list if n>=1 and again if n>=2.
        if n>=1:
            res.append (1)
        if n>=2:
            res.append (1)
            
            
        for i in range(2,n):
            #pushing sum of a and b in the list.
            res.append (a+b)
            c=a+b
            #updating a as b and b as c (sum of a and b).
            a=b
            b=c
            
        #returning the list.
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends