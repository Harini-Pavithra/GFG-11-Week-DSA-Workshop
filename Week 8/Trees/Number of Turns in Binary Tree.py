Number of Turns in Binary Tree 

Given a binary tree and data value of two of its nodes. Find the number of turns needed to reach from one node to another in the given binary tree.

Example 1:

Input :      
Tree = 
           1
        /    \
       2       3
     /  \     /  \
    4    5   6    7                        
   /        / \                        
  8        9   10   

first node = 5
second node = 10

Output: 4

Explanation : 
Turns will be at 2, 1, 3, 6.

Example 2:

Input :      
Tree = 
           1
        /     \
       2        3
     /  \      /  \
    4    5    6    7                        
   /         / \                        
  8         9   10   

first node = 1
second node = 4  

Output : -1

Explanation: No turn is required since 
they are in a straight line.

Your Task:  
You don't need to read input or print anything. Complete the function NumberOFTurns() which takes root node and data value of 2 nodes as input parameters and returns number of turns required to navigate between them. If the two nodes are in a straight line, ie- the path does not involve any turns, return -1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of Tree)


Constraints:
1 ≤ N ≤ 10^3

Solution:

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

def findLCA(n,a,b):
    if n is None:
        return None
    
    if n.data==a or n.data==b:
        return n
    
    l = findLCA(n.left,a,b)
    r = findLCA(n.right,a,b)
    
    if l and r:
        return n
    
    if l:
        return l
    
    return r

def count(n,prev,target):
    if n is None:
        return -1
    
    if n.data == target:
        return 0
    
    val = count(n.left,'l',target)
    if val!=-1:
        return val + (int)(prev=='r')
    
    val = count(n.right,'r',target)
    if val!=-1:
        return val + (int)(prev=='l')
    
    return -1

def NumberOFTurns(root,n1,n2):
    LCA = findLCA(root,n1,n2)
    
    ret = 0
    
    if LCA.data == n1:
        ret = count(LCA,'x',n2)
    
    elif LCA.data == n2:
        ret = count(LCA,'x',n1)
    
    else:
        ret = count(LCA,'x',n1) + count(LCA,'x',n2) + 1
    
    if ret==0:
        return -1
    return ret



#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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



if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        n1,n2=list(map(int, input().strip().split()))    
        print(NumberOFTurns(root,n1,n2))
       
    

# } Driver Code Ends