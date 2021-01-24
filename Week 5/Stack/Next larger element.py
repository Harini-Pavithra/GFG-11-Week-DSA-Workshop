Next larger element 

Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
Example 2:

Input: 
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to 
6 is 8, for 8 there is no larger elements 
hence it is -1, for 0 it is 1 , for 1 it 
is 3 and then for 3 there is no larger 
element on right and hence -1.
Your Task:
This is a function problem. You only need to complete the function nextLargerElement() that takes list of integers arr[ ] and N as input parameters and returns list of integers of length N denoting the next greater elements for all the corresponding elements in the input array.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ N ≤ 106
1 ≤ Ai ≤ 1018

Solution:

#User function Template for python3

'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):

    next_greater = [-1 for i in range(n)] # our answer list, initialized to -1.
    s = createStack()
    element = 0
    next = 0

    # push the first element to stack
    push(s, [arr[0],0])

    # iterate for rest of the elements
    for i in range(1, n, 1):
        next = arr[i]

        if isEmpty(s) == False:

            # if stack is not empty, then pop an element from stack
            elem = pop(s) # value, index pair popped from stack
            element = elem[0] # get the value stored in the pair
            curr_index = elem[1] # get the value stored in the pair

            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty '''
            while element < next:
                next_greater[curr_index] = next # assign value of nge to corresponding index
                if isEmpty(s) == True:
                    break
                elem = pop(s)
                element = elem[0]
                curr_index = elem[1]

            '''If element is greater than next, then push 
               the element back '''
            if element > next:
                push(s, [element,curr_index])

        '''push next to stack so that we can find 
           next greater for it '''
        push(s, [next,i])

    '''After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so let -1 be for them, as initialized. '''

    return next_greater
    



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
        res = nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends