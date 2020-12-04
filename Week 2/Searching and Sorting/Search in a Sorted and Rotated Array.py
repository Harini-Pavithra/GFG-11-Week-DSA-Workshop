Search in a Sorted and Rotated Array 

Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

Example 1:

Input:
N = 9
A[] = {5 6,7,8,9,10,1,2,3}
K = 10
Output: 5
Explanation: 10 is found at index 5.
Example 1:

Input:
N = 3
A[] = {3,1,2}
K = 1
Output: 1
User Task:
Complete Search() function and return the index of the element K if found in the array. If the element is not present, then return -1.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
0 ≤ Ai ≤ 108
1 ≤ K ≤ 108

Solution:

#User function Template for python3

def Search(arr,n,k):
    #code here
    if k in arr:
        return arr.index(k)
    else:
        return -1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends