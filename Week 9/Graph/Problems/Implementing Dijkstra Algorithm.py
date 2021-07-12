 Implementing Dijkstra Algorithm

Given a weighted, undirected and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
Note: The Graph doesn't contain any negative weight cycle.

Example 1:

Input:

S = 0
Output:
0 9
Explanation:
Shortest distance of all nodes from
source is printed.
Example 2:

Input:
S = 2
Output:
4 3 0
Explanation:
For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The other distances are pretty straight-forward.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra()  which takes number of vertices V and an adjacency list adj as input parameters and returns a list of integers, where ith integer denotes the shortest distance of the ith node from Source node. Here adj[i] contains a list of lists containing two integers where the first integer j denotes that there is an edge between i and j and second integer w denotes that the weight between edge i and j is w.

 Expected Time Complexity: O(V2).
Expected Auxiliary Space: O(V2).

 Constraints:
1 ≤ V ≤ 1000
0 ≤ adj[i][j] ≤ 1000
0 ≤ S < V

Solution




MAX_VALUE = (1<<32)
class Solution:
    
    #Function to find the vertex with minimum distance value, from the set
    #of vertices not yet included in shortest path tree.
    def minDistance(self, dist, sptSet, V) :
        
        #initializing minimum value.
        mini = MAX_VALUE
        min_index = 0
        
        for v in range(V):
            if (sptSet[v] == False and dist[v] <= mini):
                mini = dist[v]
                min_index = v
        
        return min_index
    
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V,  adj, S) :

        #creating Adjacency matrix from Adjacency list.
        adj_mat = [[0 for i in range(V)] for i in range(V)]
        
        for i in range(V):
            for j in range(len(adj[i])):
                adj_mat[i][adj[i][j][0]] = adj[i][j][1]
        
        #dist[] is output list. dist[i] will hold the 
        #shortest distance from source to i.
        dist = [0 for i in range(V)]
        
        #sptSet[i] will true if vertex i is included in shortest
        #path tree or shortest distance from src to i is finalized.
        sptSet = [False for i in range(V)]
        
        #initializing all distances as INFINITE.
        for i in range(V) :
            dist[i] = MAX_VALUE
        
        #distance of source vertex from itself is always 0.
        dist[S] = 0
        
        #iterating over all vertices.
        for count in range(V-1):
            
            #picking the minimum distance vertex from the set of vertices
            #not yet processed and marking the picked vertex as processed.
            u = self.minDistance(dist, sptSet,V);
            sptSet[u] = True
            
            #updating dist[] value of adjacent vertices of the picked vertex.
            for v in range(V):
                
                #updating dist[v] only if it's not in sptSet, there is an
                #edge from u to v, and total weight of path from source to
                #v through u is smaller than current value of dist[v].
                if sptSet[v] == False and adj_mat[u][v] !=0 and dist[u] !=  MAX_VALUE and dist[u]+adj_mat[u][v] < dist[v] :
                    dist[v] = dist[u] + adj_mat[u][v]
        
        #returning the list.           
        return dist
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends