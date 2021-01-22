Sorted insert for circular linked list 

Given a sorted circular linked list, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.

Example 1:

Input:
LinkedList = 1->2->4
(the first and last node is connected,
i.e. 4 --> 1)
data = 2
Output: 1 2 2 4
Example 2:

Input:
LinkedList = 1->4->7->9
(the first and last node is connected,
i.e. 9 --> 1)
data = 5
Output: 1 4 5 7 9
Your Task:
The task is to complete the function sortedInsert() which should insert the new node into the given circular linked list and return the head of the linkedlist.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 105

Solution

#User function Template for python3

def sortedInsert(head, data):
    '''
    head:  head of given sorted circular linked list
    data:  data to be inserted
    
    return: head of resultant circular linked list
    '''
    new_node=Node(data)
    
    current =head 

    # Case 1 of the above algo 
    if current is None: 
        new_node.next = new_node  
        head = new_node
        return head
      
    # Case 2 of the above algo 
    elif (current.data >= new_node.data): 
          
        # If value is smaller than head's value then we 
        # need to change next of last node 

        while current.next != head:
            current=current.next

        
        current.next=new_node
        new_node.next=head
        return new_node
    
    # Case 3 of the above algo 
    else: 
          
        # Locate the node before the point of insertion 
        while (current.next != head  and 
               current.next.data < new_node.data): 
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head




#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        data=int(input())

        cll=LinkedList()
        for e in arr:
            cll.push(e)
            
        reshead=sortedInsert(cll.head,data)
        printList(reshead)
        print()
        


# } Driver Code Ends