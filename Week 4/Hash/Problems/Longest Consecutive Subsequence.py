Longest Consecutive Subsequence

Given an array A of integers. Find the length of the longest sub-sequence such that elements in the sub-sequence are consecutive integers, the consecutive numbers can be in any order.
 

Example 1:

Input:
7
1 9 3 10 4 20 2
Output:
4
Explanation:
Logest consecutive subsequence is 1, 2, 3, 4 of length 4.
Example 2:

Input:
11
36 41 56 35 44 33 34 92 43 32 42
Output:
5
 

Your task:
Complete findLongestConseqSubseq() function which takes both the given array and their size as function arguments and returns the length of the longest sub-sequence such that elements in the sub-sequence are consecutive integers.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 108

Solution

# your task is to complete this function
# your function should return the length of the longest subsequence
def findLongestConseqSubseq(arr, n):
    # code here
    s = set()
    ans=0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if (arr[i]-1) not in s:
            j=arr[i]
            while(j in s):
                j+=1
            ans=max(ans, j-arr[i])
    return ans
    



#{ 
#  Driver Code Starts
# Driver function 
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        print(findLongestConseqSubseq(arr, n[0]))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends