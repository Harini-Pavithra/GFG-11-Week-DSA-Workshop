Binary Heap Operations

A binary heap is a Binary Tree with the following properties:
1) It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).

Example 1:

Input:
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
Output: 2 6 - 1
Explanation: In the first test case for
query 
insertKey(4) the heap will have  {4}  
insertKey(2) the heap will be {2 4}
extractMin() removes min element from 
             heap ie 2 and prints it
             now heap is {4} 
insertKey(6) inserts 6 to heap now heap
             is {4 6}
deleteKey(0) delete element at position 0
             of the heap,now heap is {6}
extractMin() remove min element from heap
             ie 6 and prints it  now the
             heap is empty
extractMin() since the heap is empty thus
             no min element exist so -1
             is printed.
Example 2:

Input:
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
Output: 8 -1
Your Task:
You are required to complete the 3 methods insertKey() which take one argument the value to be inserted, deleteKey() which takes one argument the position from where the element is to be deleted and extractMin() which returns the minimum element in the heap(-1 if the heap is empty)

Expected Time Complexity: O(Q*Log(size of Heap) ).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 104
1 <= x <= 104

Solution

#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''

def getParent(x):  # get parent node , if exits else -1
    return (x - 1) // 2


def leftChild(x):  # get left child if exists, else -1
    return (2 * x + 1) if (2 * x + 1) < curr_size else -1


def rightChild(x):  # get right child if exits, else -1
    return (2 * x + 2) if (2 * x + 2) < curr_size else -1


def heapify():
    '''
    : Function to maintain the min heap property of heap.
    '''
    curr_ind = curr_size - 1
    while getParent(curr_ind) != -1 and heap[getParent(curr_ind)] > heap[curr_ind]:
        heap[curr_ind], heap[getParent(curr_ind)] = heap[getParent(curr_ind)], heap[curr_ind]
        curr_ind = getParent(curr_ind)

    return


def heapifyDown(x):
    '''
    :param x: index from where heapify Down is to be implemented
    :return: None
    '''
    if x >= curr_size:  # if the removed index was leaf
        return
    if getParent(x) != -1 and heap[x] < heap[getParent(x)]:
        heap[x], heap[getParent(x)] = heap[getParent(x)], heap[x]
        heapifyDown(getParent(x))
    if leftChild(x)==-1 or (leftChild(x)!=-1 and heap[x]<heap[leftChild(x)]):
        if rightChild(x)==-1 or (rightChild(x)!=-1 and heap[x]<heap[rightChild(x)]):
            return  # property is maintained
    if rightChild(x)==-1:# swap with left child and recursively call
        heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
        heapifyDown(leftChild(x))
    elif leftChild(x) == -1:# swap with right child and recursively call
        heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
        heapifyDown(rightChild(x))
    else: # swap with the minimum of the two childs
        if heap[rightChild(x)]<heap[leftChild(x)]:
            heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
            heapifyDown(rightChild(x))
        else:
            heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
            heapifyDown(leftChild(x))
    return


def insertKey (x):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global curr_size
    heap[curr_size] = x  # insert value at current available index.
    curr_size += 1
    heapify()  # call this function to maintain heap property.


def deleteKey (x):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global curr_size

    if x >= curr_size:  # base case
        return
    # insert the value of last inserted element at the position to be removed
    heap[x] = heap[curr_size - 1]
    heap[curr_size - 1] = 0  # delete that value from its initial position.
    curr_size -= 1  # decrease the size of the current heap.

    heapifyDown(x)  # call this function to maintain heap property from index x.


def extractMin ():
    '''
    :return: return the minimum element from heap and remove it.
    '''
    if curr_size == 0:  # if heap is empty
        return -1

    val = heap[0]  # store value to be returned
    deleteKey(0)  # call this function to remove the minimum element from heap.
    return val  # return minimum value

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends