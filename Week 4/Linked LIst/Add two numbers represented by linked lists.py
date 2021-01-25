Add two numbers represented by linked lists

Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. The sum list is a linked list representation of the addition of two input numbers.

Example 1:

Input:
N = 2
valueN[] = {4,5}
M = 3
valueM[] = {3,4,5}
Output: 3 9 0  
Explanation: For the given two linked
list (4 5) and (3 4 5), after adding
the two linked list resultant linked
list will be (3 9 0).
Example 2:

Input:
N = 2
valueN[] = {6,3}
M = 1
valueM[] = {7}
Output: 7 0
Explanation: For the given two linked
list (6 3) and (7), after adding the
two linked list resultant linked list
will be (7 0).
Your Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the new list.        

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(Max(N,M))

Constraints:
1 <= N, M <= 5000

Solution

#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def reverse(head):
    # this function reverses the linked list
    prev = None
    current = head
    next = None
    
    while current is not None:
        next = current.next       # storing next node
        current.next = prev       # linking current node to previous
        prev = current            # updating prev
        current = next            # updating current
    
    return prev

def addTwoLists(first, second):
    first = reverse(first)        # reversing lists
    second = reverse(second)      # to simplify addition
    
    sumList = None
    carry = 0
    
    while first is not None or second is not None or carry>0:
        newVal = carry
        if first is not None:
            newVal += first.data
        if second is not None:
            newVal += second.data
        # newly value for sumList is sum of carry and respective
        # digits in the 2 lists
        
        carry = newVal//10        # updating carry
        newVal = newVal%10        # making sure newVal is < 10
        
        newNode = Node(newVal)
        newNode.next = sumList
        sumList = newNode
        
        if first:
            first = first.next     # moving to next node
        if second:
            second= second.next
    
    return sumList



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
