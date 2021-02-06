Nearly sorted 

Given an array of n elements, where each element is at most k away from its target position, you need to sort the array optimally.

Example 1:

Input:
n = 7, k = 3
arr[] = {6,5,3,2,8,10,9}
Output: 2 3 5 6 8 9 10
Explanation: The sorted array will be
2 3 5 6 8 9 10
Example 2:

Input:
n = 5, k = 2
arr[] = {4,3,1,2,5}
Output: 1 2 3 4 5 
Note: DO NOT use STL sort() function for this question.

Your Task:
You are required to complete the method nearlySorted() which takes 3 arguments and returns the sorted array.

Expected Time Complexity : O(nlogk)
Expected Auxilliary Space : O(n)

Constraints:
1 <= n <= 106
1 <= k <= n
1 <= arri <= 107

Solution

#User function Template for python3
def nearlySorted(a,n,k):
    '''
    :param a: given array
    :param n: size of a
    :param k: max absolute distance of value from its sorted position
    :return: sorted list
    '''

    min_heap = [] # our min heap to be used
    ans = [] # our resultant sorted array

    for num in a:
        if len(min_heap)<2*k : # if number of elements in heap is less than 2*k
            # we take 2*k as ,distance can be on either side
            # insert this element
            heapq.heappush(min_heap,num)
        else:
            # insert the root of the heap to ans, as it must be its position
            ans.append(heapq.heappop(min_heap))
            # now insert the current value in the heap
            heapq.heappush(min_heap,num)

    # if heap is non - empty, put all the elements taking from root of heap one by one in ans
    while(len(min_heap)):
        ans.append(heapq.heappop(min_heap))

    return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())