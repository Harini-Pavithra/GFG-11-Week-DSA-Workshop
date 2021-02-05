Detect cycle in an undirected graph

Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 

Example 1:

Input:   
https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Detect%20cycle%20in%20an%20undirected%20graph-Example%201.png
Output: 1
Explanation: 1->2->3->4->1 is a cycle.
Example 2:

Input: 
https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/Detect%20cycle%20in%20an%20undirected%20graph-Example%202.png
Output: 0
Explanation: No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not.
 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

Solution:

class Solution:
    def isCycleUtil(self, u, par, adj, vis):
        vis[u] = True
        for v in adj[u]:
            if(v == par):
                continue
            elif(vis[v]):
                return True
            else:
                if(self.isCycleUtil(v, u, adj, vis)):
                    return True
        return False
    def isCycle(self, V, adj):
        vis = [False for i in range(V)]
        for i in range(V):
            if(vis[i] == False):
                if(self.isCycleUtil(i, -1, adj, vis)):
                    return True
        return False
        
        
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends