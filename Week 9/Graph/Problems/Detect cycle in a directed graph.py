Detect cycle in a directed graph 

Given a Directed Graph with V vertices and E edges, check whether it contains any cycle or not.


Example 1:

Input:
Image Link : https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Detect%20cycle%20in%20a%20directed%20graph%20.png


Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:
Image Link : https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Detect%20cycle%20in%20a%20directed%20graph%20-%20Example%202.png

Output: 0
Explanation: no cycle in the graph

Your task:
You don’t need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 105

Solution:

class Solution:
    
    def DFSUtil(self, adj, v, visited, recStack):

        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in adj[v]:
            if visited[neighbour] == False:
                if self.DFSUtil(adj,neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
        
    def isCyclic(self, V, adj):
        visited = [False]*V
        recStack = [False]*V
        for node in range(V):
            if visited[node] == False:
                if self.DFSUtil(adj,node,visited,recStack) == True:
                    return True
        return False
