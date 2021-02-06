Find median in a stream 

Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

Example 1:

Input:
N = 4
X[] = 5,15,1,3
Output:
5
10
5
4
Explanation:Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5) 
15 goes to stream --> median 10 (5,15) 
1 goes to stream --> median 5 (5,15,1) 
3 goes to stream --> median 4 (5,15,1 3) 
 

Example 2:

Input:
N = 3
X[] = 5,10,15
Output:
5
7.5
10
Explanation:Flow in stream : 5, 10, 15
5 goes to stream --> median 5 (5) 
10 goes to stream --> median 7.5 (5,10) 
15 goes to stream --> median 10 (5,10,15) 
Your Task:
You are required to complete 3 methods insertHeap() which takes 1 argument, balanceHeaps() and getMedian() and returns the current median.
Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n)
 
Constraints:
1 <= N <= 106
1 <= x <= 106

Solution

#User function Template for python3
def balanceHeaps():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    Balance the two heaps size , such that difference is not more than one.
    '''
    if abs(len(min_heap)-len(max_heap)) <= 1:
        return # already balanced

    # take out one element from top of heap with greater size, and push in other heap
    if len(min_heap)>len(max_heap): # min_heap has more data
        value_top = heapq.heappop(min_heap)
        # push in max heap, using negative as it is implemented on min heap
        heapq.heappush(max_heap,-1*value_top) # value inserted in max heap
    else:
        # take from max heap and insert in min heap
        value_top = -1* heapq.heappop(max_heap) # negate it to get original value
        heapq.heappush(min_heap,value_top) # insert value in min heap

    return

def getMedian():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :return: return the median of the data received till now.
    '''
    # cases with odd number of elements in data
    if len(max_heap)>len(min_heap):
        # return the element from top of max_heap
        value = heapq.heappop(max_heap)
        heapq.heappush(max_heap,value) # push element back in max heap
        return (-1*value)
    elif len(min_heap)>len(max_heap):
        # return the top element from min heap
        value = heapq.heappop(min_heap)
        heapq.heappush(min_heap,value)
        return value
    else:
        # the number of elements is even in data, return the average of the two values
        val_min = heapq.heappop(min_heap)
        val_max = -1*heapq.heappop(max_heap)

        # push these values back in the heap
        heapq.heappush(min_heap,val_min)
        heapq.heappush(max_heap,-1*val_max)

        return ((val_max+val_min)//2) # return the average of the two

def insertHeaps(x):
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :param x: value to be inserted
    :return: None
    '''
    # if top of min heap is less than x, x belongs in upper half
    least_upperhalf = heapq.heappop(min_heap) if len(min_heap) else -1 # minimum element of upper half or -1 if empty
    # if popped, push in min_heap again
    if least_upperhalf!=-1:
        heapq.heappush(min_heap,least_upperhalf)

    if x >= least_upperhalf :
        heapq.heappush(min_heap,x) # insert in min_heap
    else:
        # x belongs in lower half
        # as this is a max_heap implemented on heapq, hence negative of x will be inserted to maintain
        # max heap property.
        heapq.heappush(max_heap,-1*x)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

min_heap = [] # our min heap to be used for upper half of data.
max_heap = [] # our max heap to be used for lower half of data.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        for i in range(n):
            insertHeaps(int(input()))
            # call this function to balance the two heaps, such that
            # their size does not differ by more than 1.
            balanceHeaps()
            # prints the median
            print(getMedian())

# } Driver Code Ends

