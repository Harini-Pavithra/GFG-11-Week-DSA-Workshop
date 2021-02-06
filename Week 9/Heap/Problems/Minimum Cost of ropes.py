Minimum Cost of ropes 

There are given N ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.

Example 1:

Input:
n = 4
arr[] = {4, 3, 2, 6}
Output: 
29
Explanation:
For example if we are given 4
ropes of lengths 4, 3, 2 and 6. We can
connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3.
Now we have three ropes of lengths 4, 6
and 5.
2) Now connect ropes of lengths 4 and 5.
Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all
ropes have connected.
Total cost for connecting all ropes is 5
+ 9 + 15 = 29. This is the optimized cost
for connecting ropes. Other ways of
connecting ropes would always have same
or more cost. For example, if we connect
4 and 6 first (we get three strings of 3,
2 and 10), then connect 10 and 3 (we get
two strings of 13 and 2). Finally we
connect 13 and 2. Total cost in this way
is 10 + 13 + 15 = 38.
Example 2:

Input:
n = 5
arr[] = {4, 2, 7, 6, 9}
Output: 
62 
Explanation:
First, connect ropes 4 and 2, which makes the 
array {6,7,6,9}. Next, add ropes 6 and 6, which 
results in {12,7,9}. Then, add 7 and 9, which 
makes the array {12,16}. And finally add these 
two which gives {28}. Hence, the total cost is 
6 + 12 + 16 + 28 = 62.
Your Task:
You don't need to read input or print anything. Your task isto complete the function minCost() which takes 2 arguments and returns the minimum cost.

Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n)

Constraints:
1 ≤ N ≤ 100000
1 ≤ arr[i] ≤ 106

Solution

#User function Template for python3
def minCost(a,n) :
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :return: Integer
    '''
    min_heap = [] # curr list containing our heap

    for num in a:
        heapq.heappush(min_heap, num) # insert all elements in heap

    total_cost = 0 # cost till now

    while(len(min_heap)>1): # while single rope has not been formed
        # get minimum two lengths from the heap
        val_1 = heapq.heappop(min_heap)
        val_2 = heapq.heappop(min_heap)

        # join these two ropes
        val = val_1+val_2
        # add to total cost
        total_cost+=val
        # now push this new length in heap again
        heapq.heappush(min_heap,val)

    # return the total cost.
    return total_cost



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
        print(minCost(a,n))
# } Driver Code Ends