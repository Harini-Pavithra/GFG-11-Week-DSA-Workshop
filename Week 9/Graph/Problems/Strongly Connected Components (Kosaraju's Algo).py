Strongly Connected Components (Kosaraju's Algo) 

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

Example 1:

Input:

Output:
3
Explanation:

We can clearly see that there are 3 Strongly
Connected Components in the Graph
Example 2:

Input:

Output:
1
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function kosaraju() which takes the number of vertices V and adjacency list of the graph as inputs and returns an integer denoting the number of strongly connected components in the given graph.
 
Expected Time Complexity: O(V+E).
Expected Auxiliary Space: O(V).
 
Constraints:
1 ≤ V ≤ 5000
0 ≤ E ≤ (V*(V-1))
0 ≤ u, v ≤ N-1
Sum of E over all testcases will not exceed 25*106

Solution

#User function Template for python3

class Solution:
    
    def DFSUtil(self,graph,v,visited):
        
        #marking the current node as visited.
        visited[v]= True
        
        #iterating over adjacent vertices and calling function 
        #recursively if any adjacent vertex is not visited.
        for i in graph[v]:
            if visited[i]==False:
                self.DFSUtil(graph,i,visited)


    def fillOrder(self,adj,v,visited, stack):
        
        #marking the current node as visited.
        visited[v]= True
        
        #iterating over adjacent vertices and calling function 
        #recursively if any adjacent vertex is not visited.
        for i in adj[v]:
            if visited[i]==False:
                self.fillOrder(adj, i, visited, stack)
                
        #pushing vertex into the stack.
        stack = stack.append(v)
    

    #Function that creates transpose of the adjacency list.
    def getTranspose(self, V, adj):
        g = [[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                g[j].append(i)
        return g

    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        ans=0
        stack = []
        
        #using boolean list to mark visited nodes and currently 
        #marking all the nodes as false.
        visited =[False]*V
        
        #filling vertices in stack according to their finishing times.
        for i in range(V):
            if visited[i]==False:
                self.fillOrder(adj, i, visited, stack)

        #creating transpose of adjacency list.
        gr = self.getTranspose(V,adj)
         
        #marking all the nodes as not visited again.
        visited =[False]*V

        #now processing all vertices in order defined by stack.
        while stack:
            
            #popping a vertex from stack.
            i = stack.pop()
            
            #if vertex is not visited, we call DFSUtil function 
            #and increment the counter.
            if visited[i]==False:
                self.DFSUtil(gr, i, visited)
                ans+=1 
        
        #returning the count.
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends