Queue Push & Pop 

Given an array arr[] of size N, enqueue the elements of the array into a queue and then dequeue them.

Example 1:

Input:
N= 5 
arr[]= 1 2 3 4 5 
Output: 
1 2 3 4 5
Example 2:

Input:
N=7
arr[]= 1 6 43 1 2 0 5
Output:
1 6 43 1 2 0 5
Your Task:
You don't need to read any input. Your task is to complete the functions push() and _pop(). The function push() takes the array and its size as the input parameters and returns the queue formed, and the function _pop(), takes the queue as the input parameter and prints the elements of the queue.

 

Expected time complexity: O(n)

Expected space complexity: O(n)

 

Constraints:
1 <= Ai <= 107

Solution:

#User function Template for python3

def push(arr,n): 
    
    #return a queue with all elements of arr inserted in it
    return arr
    
    
    
def _pop(q):
    
    #dequeue elements and print them
    for i in q:
        print(i,end=" ")
        
def deque():
    return None



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque


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
        arr = list(map(int,input().strip().split()))
        q=deque()
        q=push(arr,n)
        _pop(q)
        print()
# } Driver Code Ends