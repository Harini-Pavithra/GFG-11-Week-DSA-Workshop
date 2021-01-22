Circular Linked List Delete at Position 

Given a linked list of size n, you have to delete the node at position pos of the linked list and return the new head. The position of initial node is 1.
The tail of the circular linked list is connected to the head using next pointer.

Example 1:

Input:
LinkedList: 1->2->3->4->5
(the first and last node are connected,
i.e. 5 --> 1)
position: 4
Output: 1 2 3 5
Example 2:

Input:
LinkedList: 2->5->7->8->99->100
(the first and last node are connected,
i.e. 5 --> 1)
position: 6
Output: 2 5 7 8 99
Your Task:
The task is to complete the function deleteAtPosition() which takes head reference and pos as argument and returns reference to the new head node, which is then used to display the list. The printing is done automatically by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
2 <= number of nodes <= 103
1 <= pos <= n

Solution

#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteTail(head):

    # if head.next.next==head:
    #     head.next=head
    #     return head.next

    t=head

    while t.next!=head:
        pv=t
        t=t.next

    pv.next=pv.next.next

    return head

def deleteHead(head):
    c=head
    while c.next!=head:
        c=c.next

    t=head
    head=head.next
    c.next=head
    return head

def getLength(head):
    if not head:
        return 0

    c=1
    t=head
    while t.next!=head:
        t=t.next
        c+=1
    return c

def deleteAtPosition(head,pos):
    if pos==1:
        return deleteHead(head)

    if pos==getLength(head):
        return deleteTail(head)

    curr=head
    pvs=head

    c=1

    while c<pos:
        c+=1
        pvs=curr
        curr=curr.next

    nxt=curr.next
    curr.next=None

    pvs.next=nxt

    return head



#{ 
#  Driver Code Starts
# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next

    
    print(t.data,end=' ')


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        resHead=deleteAtPosition(ll.head,pos)
        displayList(resHead)
        print()
# } Driver Code Ends