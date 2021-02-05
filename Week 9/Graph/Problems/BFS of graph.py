Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v and find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the graph.

Example 1:

Input:
BFS Image Link:  https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/BFS.png
Output: 0 1 2 3 4
Explanation: 
0 is connected to 1 , 2 , 3.
2 is connected to 4.
so starting from 0, it will go to 1 then 2
then 3.After this 2 to 4, thus bfs will be
0 1 2 3 4.

Example 2:

Input:
BFS-Example 2 Image Link : https://github.com/Harini-Pavithra/GFG-11-Week-DSA-Workshop/blob/main/Week%209/Graph/Problems/BFS-Example%202.png
Output: 0 1 2
Explanation:
0 is connected to 1 , 2.
so starting from 0, it will go to 1 then 2,
thus bfs will be 0 1 2 3 4. 

Your task:
You don’t need to read input or print anything. Your task is to complete the function bfsOfGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns  a list containing the BFS traversal of the graph starting from the 0th vertex from left to right.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 104

Solution:

#User function Template for python3

from queue import Queue
class Solution:
    def bfsOfGraph(self, V, adj):
        ans = []
        vis = [False for i in range(V)]
        q = Queue(maxsize = 0)
        q.put(0)
        vis[0] = True
        while(q.empty() == False):
            v = q.get()
            ans.append(v)
            for i in adj[v]:
                if(vis[i] == False):
                    vis[i] = True
                    q.put(i)
        return ans



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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
