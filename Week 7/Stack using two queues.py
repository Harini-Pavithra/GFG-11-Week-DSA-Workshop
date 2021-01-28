Stack using two queues 

Implement a Stack using two queues q1 and q2.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the 
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4  
Example 2:

Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1
Your Task:

Since this is a function problem, you don't need to take inputs. You are required to complete the two methods push() which takes an integer 'x' as input denoting the element to be pushed into the stack and pop() which returns the integer poped out from the stack(-1 if the stack is empty).

Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100


Solution:

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_1.append(x)
    
def pop():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if len(queue_1) == 0:
        return -1
    elif len(queue_1)==1:
        return queue_1.pop(0)
    else:

        while(len(queue_1)!=1):
            pi = queue_1.pop(0)
            queue_2.append(pi)
        res = queue_1.pop(0)
        queue_2,queue_1=queue_1,queue_2
        # print(queue_1,queue_2)
        return res
    



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

queue_1 = [] # first queue
queue_2 = [] # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
# } Driver Code Ends