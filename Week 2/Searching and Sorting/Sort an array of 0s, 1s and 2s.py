Sort an array of 0s, 1s and 2s 

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output: 0 0 1 2 2
Explanation: 0s 1s and 2s are segregated 
into ascending order.
 

Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output: 0 0 1
Explanation: 0s 1s and 2s are segregated 
into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes array and n as input parameters and sorts the array in-place. 


Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)

 

Constraints:
1 <= N <= 10^5
0 <= A[i] <= 2

Solution:

#User function Template for python3

def sort012(arr,n):
    # code here
    return arr.sort()




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends