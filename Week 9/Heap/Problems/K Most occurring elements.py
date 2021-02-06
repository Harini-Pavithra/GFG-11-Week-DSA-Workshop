K Most occurring elements

Given an array arr[] of N integers in which elements may be repeating several times. Also, a positive number K is given and the task is to find sum of total frequencies of K most occurring elements

Note: The value of K is guaranteed to be less than or equal to the number of distinct elements in arr.

Example 1:

Input:
N = 8
arr[] = {3,1,4,4,5,2,6,1}
K = 2
Output: 4
Explanation: Since, 4 and 1 are 2 most
occurring elements in the array with
their frequencies as 2, 2. So total
frequency is 2 + 2 = 4.
Example 2:

Input:
N = 8
arr[] = {3,3,3,4,1,1,6,1}
K = 2
Output: 6
Explanation: Since, 3 and 1 are most
occurring elements in the array with
frequencies 3, 3 respectively. So,
total frequency is 6.
Your Task:
Complete the function kMostFrequent() whic returns the frequencies of K most occuring elements.

Constraints:
1 <= N <= 107
1 <= K <= N
1 <= arr[i] <= 106

Expected Time Complexity : O(N)
Expected Auxilliary Space: O(N)

Solution

#User function Template for python3

def kMostFrequent(a,n,k) :
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: Integer
    '''
    freq_map = defaultdict(int) # to store freq of numbers occurring
    for num in a:
        # if num is already in map
        if num in freq_map:
            # increment by 1
            freq_map[num]+=1
        else:
            # insert in map
            freq_map[num]=1

    min_heap = [] # curr list containing k largest frequencies from processed till now

    for key in freq_map:
        num = freq_map[key] # frequency of given value in array
        if len(min_heap)<k: # if the current size is less than k, add element in it
            heapq.heappush(min_heap,num)
        else:
            curr_min = heapq.heappop(min_heap) # curr min element in heap
            # push max out of current element and heap min in heap again
            heapq.heappush(min_heap,max(curr_min,num))

    return sum(min_heap) # return sum of the elements present in our min heap

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict
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
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = int(input())
        print(kMostFrequent(a,n,k))
# } Driver Code Ends