Level order traversal in spiral form

Complete the function to find spiral order traversal of a tree. For below tree, function should return 1, 2, 3, 4, 5, 6, 7.

Example 1:

Input:
      1
    /   \
   3     2
Output:1 3 2

Example 2:

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 
Your Task:
The task is to complete the function findSpiral() which takes root node as input parameter and returns the elements in spiral form of level order traversal as a list. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 105
0 <= Data of a node <= 105

Solution:

#User function Template for python3


'''
class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def getHeight(root):
    
    # base case
    if root is None:
        return 0
    
    # finding left height
    lh = getHeight(root.left)
    
    # finding the right height
    rh = getHeight(root.right)
    
    if lh>rh:
        return lh+1
    else:
        return rh+1

def printLevel(result,node, lvl, flg):
    
    # base case
    if node is None:
        return
    
    # when level is 1
    if lvl==1:
        result.append(node.data)
    
    # when level is greater than 1
    elif(lvl > 1):
        # traverse for left from right
        if flg:
            printLevel(result,node.left, lvl-1, flg)
            printLevel(result,node.right, lvl-1, flg)
        
        # right to left
        else:
            printLevel(result,node.right, lvl-1, flg)
            printLevel(result,node.left, lvl-1, flg)

def findSpiral(root):
    # Code here
    result = []
    if root is None:
        return result
    h = getHeight(root)
    ltr = False
    for i in range(1, h+1):
        printLevel(result,root, i, ltr)
        ltr = not ltr
    return result
        






#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        s=input()
        root=buildTree(s)
        result = findSpiral(root)
        for value in result:
            print(value,end = " ")
        print()
        
        

# } Driver Code Ends