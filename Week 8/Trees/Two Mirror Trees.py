Two Mirror Trees 

Given a Two Binary Trees, write a function that returns true if one is mirror of other, else returns false.
MirrorTree1            

Example 1:

Input:
T1:     1     T2:     1
      /   \         /   \
     2     3       3     2
Output: 1
Example 2:

Input:
T1:     10      T2:   10
       /  \          /  \
      20  30        20  30
     /  \          /  \
    40   60       40  60
Output: 0

Your Task:
You don't need to take input. Just complete the function areMirror() that takes root node of two tree as parameter and returns true, if one is the mirror of other else returns false. (The driver's code print 1 if the returned value is true, otherwise 0)
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes<= 10000
-1000 <= Data of a node<= 1000

Solution:

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def areMirror(a, b): 
      
    
    if a is None and b is None: 
        return True
      
    
    if a is None or b is None: 
        return False
      
    return (a.data == b.data and 
            areMirror(a.left, b.right) and 
            areMirror(a.right , b.left)) 


#{ 
#  Driver Code Starts

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
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        str1=input()
        str2=input()
        root1=buildTree(str1)
        root2=buildTree(str2)
        if areMirror(root1, root2)==True:
            print(1)
        else:
            print(0)
            
            

# } Driver Code Ends