 Kth largest element 

Given an array arr[] of N positive integers and a number K. The task is to find the kth largest element in the array.

Example 1:

Input:
N = 5, K = 3
arr[] = {3, 5, 4, 2, 9}
Output: 
4
Explanation: 
Third largest element
in the array is 4.
Example 2:

Input:
N = 5, K = 5
arr[] = {4, 3, 7, 6, 5} 
Output: 
3
Explanation: 
Fifth largest element
in the array is 3.
Your Task:
You are required to complete the method KthLargest() which takes 3 arguments and returns the Kth Largest element.

Constraints:
1 <= N <= 106
1 <= arr[i] <= 106
1 <= K <= N

Expected Time Complexity : O(NlogK)
Expected Auxilliary Space : O(K)

Solution

#User function Template for python3
def kthLargest(a,n,k):
    '''
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: Integer.
    '''
    k_largest_curr = [] # curr list containing k largest element from processed till now

    for num in a:
        if len(k_largest_curr)<k: # if the current size is less than k, add element in it
            heapq.heappush(k_largest_curr,num)
        else:
            curr_min = heapq.heappop(k_largest_curr) # curr minimum element in heap
            # push max out of current element and heap min in heap again
            heapq.heappush(k_largest_curr,max(curr_min,num))
    
    # return kth largest element, that is root of the heap
    return heapq.heappop(k_largest_curr)
    
    
    
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k= map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        print(kthLargest(a,n,k))
# } Driver Code Ends