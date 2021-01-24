Maximum of minimum for every window size 

Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Example 1:

Input:
N = 7
arr[] = {10,20,30,50,10,70,30}
Output: 70 30 20 10 10 10 10 
Explanation: First element in output
indicates maximum of minimums of all
windows of size 1. Minimums of windows
of size 1 are {10}, {20}, {30}, {50},
{10}, {70} and {30}. Maximum of these
minimums is 70. 
Second element in output indicates
maximum of minimums of all windows of
size 2. Minimums of windows of size 2
are {10}, {20}, {30}, {10}, {10}, and
{30}. Maximum of these minimums is 30 
Third element in output indicates
maximum of minimums of all windows of
size 3. Minimums of windows of size 3
are {10}, {20}, {10}, {10} and {10}.
Maximum of these minimums is 20. 
Similarly other elements of output are
computed.
Example 2:

Input:
N = 3
arr[] = {10,20,30}
Output: 30 20 10
Explanation: First element in output
indicates maximum of minimums of all
windows of size 1.Minimums of windows
of size 1 are {10} , {20} , {30}.
Maximum of these minimums are 30 and
similarly other outputs can be computed
Your Task:
The task is to complete the function maxOfMin() which takes the array arr[] and its size N as inputs and finds the maximum of minimum of every window size and returns an array containing the result. 

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 106

Solution:

#User function Template for python3
'''
Function Arguments :
      @param  : arr(given array), N (size of array)
      @return : required array.
'''

def maxOfMin(a,n):
    stack = []  # Used to find previous and next smaller

    #Lists to store previous and next smaller
    left = [-1 for i in range(n)] # initialized with -1
    right = [n for i in range(n)] # initialized with n

    '''
        Fill elements of left[] using logic discussed on 
        https://www.geeksforgeeks.org/next-greater-element/
    '''
    for i in range(n):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            left[i] = stack[-1]
        stack.append(i)

    # empty the stack for use in right.
    stack = []

    # fill elements of right using same logic
    for i in range(n-1,-1,-1):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            right[i] = stack[-1]
        stack.append(i)

    # create and initialize ans array
    ans= [0 for i in range(n+1)]

    '''Fill answer array by comparing minimums of all 
     lengths computed using left[] and right[] '''
    for i in range(n):
        # length of the interval
        length = right[i]-left[i]-1
        ans[length] = max(ans[length],a[i])

    '''
        Some entries in ans[] may not be filled yet. Fill  
        them by taking values from right side of ans[] .
    '''
    for i in range(n-1,-1,-1):
        ans[i] = max(ans[i],ans[i+1])

    # print ans from len 1 to n
    return ans[1:]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        res = maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends