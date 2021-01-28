Reverse First K elements of Queue 

Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.
Example 1:

Input:
5 3
1 2 3 4 5

Output: 
3 2 1 4 5

Explanation: 
After reversing the given
input from the 3rd position the resultant
output will be 3 2 1 4 5.

Example 2:

Input:
4 4
4 3 2 1

Output: 
1 2 3 4

Explanation: 
After reversing the given
input from the 4th position the resultant
output will be 1 2 3 4.
Your Task:
Complete the provided function modifyQueue that takes queue and k as parameters and returns a modified queue. The printing is done automatically by the driver code.

Expected TIme Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= N <= 1000
1 <= K <= N

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

Solution:

#User function Template for python3
'''
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
'''
def modifyQueue(q,k):
    stack= [] # auxilary stack to be used for reversing
    ansqueue = [] # our answer queue

    # insert first k elements of q to stack
    for i in range(k):
        stack.append(q.pop(0))

    # now one by one pop elements from stack and put in queue
    # as stack uses lifo , this essentially reverse the k elements.
    while len(stack):
        ansqueue.insert(0,stack.pop(0)) # enqueue elements from stack

    while len(q):
        ansqueue.append(q.pop(0)) # append remaining elements from q

    return ansqueue



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
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*modifyQueue(queue,k))
# } Driver Code Ends