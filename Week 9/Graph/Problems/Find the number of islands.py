Find the number of islands 

Given a grid consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i,e in all 8 directions.
 

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:

Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands one is colored in blue 
and other in orange.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function numIslands() which takes grid as input parameter and returns the total number of islands.
 

Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 

Constraints:
1 <= n, m <= 500

Solution:

import collections
class Solution:
	def numIslands(self, grid):
	        try: 
	            m,n = len(grid), len(grid[0])
	        except: 
	            return 0
	        cnt = 0
	        ones = { (i,j) for i in range(m) for j in range(n) if grid[i][j]=='1' }
	        while ones:
	            queue = collections.deque([ ones.pop() ])
	            while queue:
	                i,j = queue.popleft()   # BFS
	             # i,j = queue.pop()       # DFS
	                for x,y in (i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1, j-1), (i+1, j+1), (i-1, j-1), (i-1, j+1) :
	                    if 0<=x<m and 0<=y<n and (x,y) in ones:
	                        ones.discard( (x,y) )
	                        queue.append( (x,y) )
	            cnt += 1
	        return cnt
	        
	        


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(input().split())
			grid.append(a)
		obj = Solution()
		ans = obj.numIslands(grid)
		print(ans)

# } Driver Code Ends