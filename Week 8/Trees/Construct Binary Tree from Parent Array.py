Construct Binary Tree from Parent Array 

Given an array of size N that can be used to represents a tree. The array indexes are values in tree nodes and array values give the parent node of that particular index (or node). The value of the root node index would always be -1 as there is no parent for root. Construct the standard linked representation of Binary Tree from this array representation.

Example 1:

Input:
N = 7
parent[] = {-1,0,0,1,1,3,5}
Output: 0 1 2 3 4 5 6
Explanation: the tree generated
will have a structure like 
          0
        /   \
       1     2
      / \
     3   4
    /
   5
 /
6
 

Example 2:

Input:
N = 3
parent[] = {2, 0, -1}
Output: 2 0 1
Explanation: the tree generated will
have a sturcture like
               2
             /   
            0      
          /   
         1     
Your Task:
You don't need to read input or print anything. The task is to complete the function createTree() which takes 2 arguments parent[] and N and returns the root node of the constructed tree.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 103

Solution:

#User function Template for python3


'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

def createNode(parent, i, created, root):
    # If this node is already created
    if created[i] is not None:
        return

    # Create a new node and set created[i]
    created[i] = Node(i)

    # If 'i' is root, change root pointer and return
    if parent[i] == -1:
        root[0] = created[i]  # root[0] denotes root of the tree
        return

    # If parent is not created, then create parent first
    if created[parent[i]] is None:
        createNode(parent, parent[i], created, root)

        # Find parent pointer
    p = created[parent[i]]

    # If this is first child of parent
    if p.left is None:
        p.left = created[i]
        # If second child
    else:
        p.right = created[i]

    # Creates tree from parent[0..n-1] and returns root of the


# created tree
def createTree(parent,n):
    n = len(parent)

    # Create and array created[] to keep track
    # of created nodes, initialize all entries as None
    created = [None for i in range(n + 1)]

    root = [None]
    for i in range(n):
        createNode(parent, i, created, root)

    return root[0]

    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import  defaultdict

#Contributed by : Nikhil Kumar Singh

'''
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
'''


# Python implementation to construct a Binary Tree from
# parent array

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function should print the level order of the tree in sorted format
def traverse_level_order(root):
    # Code here
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n==0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes,end=" ")
        while(n>0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n-=1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        traverse_level_order(createTree(a,n))
        print()
# } Driver Code Ends