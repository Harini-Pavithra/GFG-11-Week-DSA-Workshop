Merge Sort on Doubly Linked List

Given Pointer/Reference to the head of a doubly linked list of N nodes, the task is to Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing order.

Example 1:

Input:
N = 8
value[] = {7,3,5,2,6,4,1,8}
Output:
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
Explanation: After sorting the given
linked list in both ways, resultant
matrix will be as given in the first
two line of output, where first line
is the output for non-decreasing
order and next line is for non-
increasing order.
Example 2:

Input:
N = 5
value[] = {9,15,0,-1,0}
Output:
-1 0 0 9 15
15 9 0 0 -1
Explanation: After sorting the given
linked list in both ways, the
resultant list will be -1 0 0 9 15
in non-decreasing order and 
15 9 0 0 -1 in non-increasing order.
Your Task:
The task is to complete the function sortDoubly() which sorts the doubly linked list. The printing is done automatically by the driver code.

Constraints:
1 <= N <= 105

Solution:

#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

def merge(first, second):
    # If first linked list is empty 
    if first is None: 
        return second  
      
    # If secon linked list is empty  
    if second is None: 
        return first 

    # Pick the smaller value 
    if first.data < second.data: 
        first.next = merge(first.next, second) 
        first.next.prev = first 
        first.prev = None   
        return first 
    else: 
        second.next = merge(first, second.next) 
        second.next.prev = second 
        second.prev = None
        return second 

# Function to do merge sort 
def sortDoubly(head): 
    if head is None:  
        return head 
    if head.next is None: 
        return head 
      
    second = split(head) 
      
    # Recur for left and righ halves 
    head = sortDoubly(head) 
    second = sortDoubly(second) 

    # Merge the two sorted halves 
    return merge(head, second) 

# Split the doubly linked list (DLL) into two DLLs 
# of half sizes 
def split(head): 
    fast = slow =  head 
    while(True): 
        if fast.next is None: 
            break
        if fast.next.next is None: 
            break
        fast = fast.next.next 
        slow = slow.next
          
    temp = slow.next
    slow.next = None
    return temp 
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


import sys
sys.setrecursionlimit(1000000)
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node
		
	def printList(self, node):
		while(node.next is not None):
			node = node.next
		while node.prev is not None:
		    node = node.prev
		while(node is not None):
		    print(node.data, end=" ")
		    node = node.next
		print()
		
		
		
		

        
def printList(node): 
        temp = node 
      
        while(node is not None): 
            print (node.data,end=" ")
            temp = node 
            node = node.next
        print()
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.prev 

		




if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        llist.head=sortDoubly(llist.head)
        printList(llist.head)
        print()


# } Driver Code Ends