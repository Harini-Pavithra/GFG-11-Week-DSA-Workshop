Topological sort 

Given a Directed Graph with V vertices and E edges, Find any Topological Sorting of that Graph.

Example 1:

Input:
https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Topological%20Sort.png
Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:
https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Topological%20sort-%20Example%202.png

Output:
1
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of a the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them.


Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).


Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2

Solution:

class Solution:
    
    # A recursive function used by topologicalSort
    def DFSUtil(self,adj,v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in adj[v]:
            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)
    
    def topoSort(self, V, adj):
        # Mark all the vertices as not visited
        visited = [False]*V
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        # Return contents of the stack
        return stack




#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends