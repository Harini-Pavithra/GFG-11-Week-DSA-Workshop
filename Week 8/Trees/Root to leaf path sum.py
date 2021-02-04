Root to leaf path sum 

Given a binary tree and an integer S, check whether there is root to leaf path with its sum as S.

Example 1:

Input:
Tree = 
            1
          /   \
        2      3
S = 2

Output: 0

Explanation:
There is no root to leaf path with sum 2.
Example 2:

Input:
Tree = 
            1
          /   \
        2      3
S = 4

Output: 1

Explanation:
The sum of path from leaf node 3 to root 1 is 4.

Your Task:  
You dont need to read input or print anything. Complete the function hasPathSum() which takes root node and target sum S as input parameter and returns true if path exists otherwise it returns false.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of tree)

Constraints:
1 ≤ N ≤ 10^4
1 ≤ S ≤ 10^6

Solution:

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def hasPathSum(node, s): 
      
    # Return true if we run out of tree and s = 0  
    if node is None: 
        return (s == 0) 
  
    else: 
        ans = 0 
          
        # Otherwise check both subtrees 
        subSum = s - node.data  
          
        # If we reach a leaf node and sum becomes 0, then  
        # return True  
        if(subSum == 0 and node.left == None and node.right == None): 
            return True 
  
        if node.left is not None: 
            ans = ans or hasPathSum(node.left, subSum) 
        if node.right is not None: 
            ans = ans or hasPathSum(node.right, subSum) 
  
        return ans


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
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root = buildTree(s)
        sum=int(input())
        if hasPathSum(root, sum)==True:
            print(1)
        else:
            print(0)
            
# } Driver Code Ends