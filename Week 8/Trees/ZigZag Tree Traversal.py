ZigZag Tree Traversal 

Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

Example 1:

Input:
        3
      /   \
     2     1
Output: 3 1 2
 

Example 2:

Input:
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 
Output: 7 7 9 8 8 6 9 10 
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function zigZagTraversal() which takes the root node of the Binary Tree as its input and returns a list containing the node values as they appear in the Zig-Zag Level-Order Traversal of the Tree.

 Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 104

Solution:

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# return a list containing the zig zag level order traversal of the given tree
def zigZagTraversal(root):
    l=[1,root]
    lvl=[]
    while l:
        n=l.pop(0)
        i=0
        j=0
        tl=[]
        lv=[]
        while i<n:
            r=l.pop(0)
            #print(r.data,end=' ')
            lv.append(r.data)
            if r.left:
                j+=1
                tl.append(r.left)
            if r.right:
                j+=1
                tl.append(r.right)
            i+=1
        #print('$',end=' ')
        if j>0:
            l.append(j)
        if lv:
            #print(lv)
            lvl.append(lv)
            
                
        for e in tl:
            l.append(e)
    res = []
    for i,e in enumerate(lvl):
        if i%2!=0:
            for f in e[::-1]:
                res.append (f)
        else:
            for f in e:
                res.append (f)
    
    return res




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = zigZagTraversal(root)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends