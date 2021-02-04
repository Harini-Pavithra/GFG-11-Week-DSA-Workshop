Deletion in a Binary Tree

Given a Binary Tree of size N, your task is to complete the function deletionBT(), that should delete a given node from the tree by making sure that tree shrinks from the bottom (the deleted node is replaced by bottommost and rightmost node).
Example:

Eample Deletion in Bt


Your Task:
You don't have to take input. Complete the function deletionBT() that takes root node of the tree and given node value (Key) as input parameter and return the root of the modified tree.

Example 1:
 

Input:
Key=1
         1
       /   \
      4     7
     / \
    5   6 
Output:
5 4 6 7 

Explanation:
Modified Tree after deletion the 
node with key = 1
     7 
    /  
   4   
  /  \ 
 5    6 
The Inorder traversal of the modified 
tree is 5 4 6 7 


Constraints:
1<=N<=104

Solution:

#User function Template for python3

def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletionBT(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.data 
        deleteDeepest(root,temp) 
        key_node.data = x 
    return root

    
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
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
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        key = int(input())
        s=input()
        root=buildTree(s)
        deletionBT(root, key)
        inorder(root)
        print()
        
        

# } Driver Code Ends