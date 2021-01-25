Clone a linked list with next and random pointer 

You are given a special linked list with N nodes where each node has a next pointer pointing to its next node. You are also given M random pointers , where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.

ArbitLinked List1

Example 1:

Input:
N = 4, M = 2
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output: 1
Explanation: In this test case, there
re 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbit pointer
set, rest two nodes have arbit pointer
as NULL. Second line tells us the value
of four nodes. The third line gives the
information about arbitrary pointers.
The first node arbit pointer is set to
node 2.  The second node arbit pointer
is set to node 4.
Example 2:

Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output: 1
Explanation: In the given testcase ,
applying the method as stated in the
above example, the output will be 1.
Your Task:
The task is to complete the function copyList() which takes one argument the head of the linked list to be cloned and should return the head of the cloned linked list.
NOTE : If their is any node whose arbitrary pointer is not given then its by default null.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 100
1 <= M <= N
1 <= a, b <= 100

Solution:

#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    def copyList(self, head):

        d=dict()
        if not head:
            return
        
        
        ch=Node(head.data)
        chh=ch
        
        d[head]=ch
        
        h=head.next
        
        while h:
            nn=Node(h.data)
            chh.next=nn
            d[h]=nn
            
            h=h.next
            chh=nn
        
        h=head
        
        chh=ch
        
        while h:
            if h.arb:
                chh.arb=d[h.arb]
            h=h.next
            chh=chh.next
            
            
        return ch


#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    headp = head
    resp = res
    
    d = {}
    
    while head and res:
        if head==res:
            return
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        if head not in d:
            d[head] = res
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    head = headp
    res = resp
    while head:
        if head == res:
            return 
        if head.arb:
            if head.arb not in d:
                return
            if d[head.arb] != res.arb:
                return
        head=head.next
        res=res.next
        
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        __n,__m = list(map(int, input().strip().split()))
        __nodes = list(map(int, input().strip().split()))
        __aarb = list(map(int, input().strip().split()))
        __ll=LinkedList()
        __ll2=LinkedList()
        __ll.head=Node(__nodes[0])
        __ll2.head=Node(__nodes[0])
        __tail=__ll.head
        __tail2=__ll2.head
        
        for x in __nodes[1:]:
            __tail=insert(__tail,x)
            __tail2=insert(__tail2,x)
        
        for i in range(0,len(__aarb),2):
            setarb(__ll.head,__aarb[i],__aarb[i+1])
            setarb(__ll2.head,__aarb[i],__aarb[i+1])
        
        obj = Solution()
        __res=obj.copyList(__ll.head)
        if validation(__ll.head,__res) and validation(__ll2.head,__res):
            print(1)
        else:
            print(0)
# } Driver Code Ends