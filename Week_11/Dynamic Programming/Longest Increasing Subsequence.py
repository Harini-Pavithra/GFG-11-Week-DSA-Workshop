Longest Increasing Subsequence

Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:

Input:
N = 16
A[]={0,8,4,12,2,10,6,14,1,9,5
     13,3,11,7,15}
Output: 6
Explanation:Longest increasing subsequence
0 2 6 9 13 15, which has length 6
Example 2:

Input:
N = 6
A[] = {5,8,3,7,9,1}
Output: 3
Explanation:Longest increasing subsequence
5 7 9, with length 3
Your Task:
Complete the function longestSubsequence() which takes the input array and its size as input parameters and returns the length of the longest increasing subsequence.

Expected Time Complexity : O( N*log(N) )
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
0 ≤ A[i] ≤ 106

Solution

class Solution:
    
    #binary search function finds the position of the first integer
    #in arr[] which is greater than or equal to 'value'.
    def binarySearch(self,lst, l, h, value):
        
        
        #if new value is greater than all array values,
        #then it is placed at the end.
        if value > lst[h]:
            return h+1
        
        #binary search algorithm.
        while h>l:
            middle = (h+l)//2
            
            if lst[middle] == value:
                return middle
            
            if lst[middle] > value:
                h = middle
            
            else:
                l = middle + 1
        
        return h
    
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        
        #tail[i] holds the last value in a subsequence of length i+1.
        tail = [0 for _ in range(n)]
        tail[0] = a[0]
       
        #the position of last filled index in tail[].
        lastIndex = 0 
        
        for i in range(1,n):
            
            #getting the furthest possible index for a[i].
            index = self.binarySearch( tail, 0, lastIndex, a[i] )
            
            tail[index] = a[i]
            #updating lastIndex.
            lastIndex = max( lastIndex, index )
        
        #returning the result.
        return lastIndex+1

       


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends