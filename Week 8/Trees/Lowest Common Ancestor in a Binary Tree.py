Lowest Common Ancestor in a Binary Tree 

Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them is present. 

Example 1:

Input:
n1 = 2 , n2 =  3
     1
   /  \
  2    3
Output: 1
Explanation:
LCA of 2 and 3 is 1.
Example 2:

Input:
n1 = 3 , n2 = 4
         5
        /
       2
     /  \
    3    4
Output: 2
Explanation: 
LCA of 3 and 4 is 2. 

Your Task:
You don't have to read input or print anything. Your task is to complete the function lca() that takes nodes, n1, and n2 as parameters and returns LCA node as output.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree.

Constraints:
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Solution:

#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
# If LCA exist, return reference to it. If
# If both n1 and n2 are not present, 
# rturn None. Else if left subtree contains any 
#  of them return pointer to left.
def lca(root, n1, n2):
    # base case
    if root is None:
        return None
        
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.data == n1 or root.data == n2:
        return root
        
    # Look for keys in left and right subtrees 
    left_lca = lca(root.left, n1, n2) 
    right_lca = lca(root.right, n1, n2)
    
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca:
        return root
        
    # Otherwise check if left subtree or right subtree is LCA 
    if left_lca is not None:
        return left_lca
    else:
        return right_lca






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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=lca(root,a,b)
        print(k.data)



# } Driver Code Ends