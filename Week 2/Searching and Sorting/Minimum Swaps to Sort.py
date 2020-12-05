Minimum Swaps to Sort 

Given an array of size N. Find the minimum number of swaps required to sort the array in non-decreasing order.


Example 1:

Input: 
N = 5
arr = {1 5 4 3 2}
Output: 2
Explaination: swap 2 with 5 and 3 with 4.
 

Example 2:

Input: 
N = 4
arr[] = {8 9 16 15}
Output: 1
Explaination: swap 16 and 15.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the array arr[] and its size N as input parameters and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 


Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

 

Constraints:
1 <= N <= 105
1 <= A[] <= 106

Solution:

# Your task is to complete this function

# return the minimum number of swaps required to sort the arra
def minSwaps(arr, N):
    # Code here
    ans = 0
    temp = arr.copy()
    h = {}
 
    temp.sort()
 
    for i in range(n):
        h[arr[i]] = i
         
    init = 0
     
    for i in range(n):
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
            h[init] = h[temp[i]]
            h[temp[i]] = i
             
    return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(minSwaps(arr, n))

# } Driver Code Ends