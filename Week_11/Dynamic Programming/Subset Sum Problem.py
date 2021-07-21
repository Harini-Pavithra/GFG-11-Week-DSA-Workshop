Subset Sum Problem 

Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Example 1:

Input:
N = 4
arr[] = {1,5,11,5}
Output: YES
Explanation: There exists two subsets
such that {1, 5, 5} and {11}.
Example 2:

Input:
N = 3
arr[] = {1,3,5}
Output: NO
Your Task:
Your task is to complete the findPartition() function which takes an array a[] and N as input parameter and return true if the given set can be partitioned into two subsets such that the sum of elements in both subsets is equal, else return false.
Note: The output will be YES or NO depending upon the value returned by your code. The printing is done by the driver's code.

Expected Time Complexity: O(N*S).
Expected Auxiliary Space: O(S) where S is the sum of the given Array.

Constraints:
1 <= N <= 100
0 <= arr[i] <= 1000

Solution

#User function Template for python3

class Solution:
    def isSubsetSum(self,arr, n, sum): 
         
        #the value of subset[i%2][j] will be true if there exists 
        #a subset of sum j in arr[0, 1, ...., i-1].
        subset = [ [False for j in range(sum + 1)] for i in range(3) ] 
       
        for i in range(n + 1): 
            for j in range(sum + 1): 
                
                #a subset with sum 0 is always possible. 
                if (j == 0): 
                    subset[i % 2][j] = True
       
                #if there exists zero element, no sum is possible.  
                elif (i == 0): 
                    subset[i % 2][j] = False
                    
                #else we update the value of subset[i%2][j].
                elif (arr[i - 1] <= j): 
                    subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)  
                                                                                   % 2][j] 
                else: 
                    subset[i % 2][j] = subset[(i + 1) % 2][j] 
        
        #returning the result.              
        return subset[n % 2][sum]
      
    #Function to check whether a set of numbers can be partitioned into 
    #two subsets such that the sum of elements in both subsets is same.
    def findPartition(self,arr,n):
        
        #storing sum of all elements.
        sm=sum(arr)
        
        if sm%2==0:
            return self.isSubsetSum(arr, n, sm//2)
        #if the total sum is odd, returning false.
        else:
            return
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        if ob.findPartition(arr,n):
            print('YES')
        else:
            print('NO')
        
# } Driver Code Ends