Unit Area of largest region of 1's

Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).
 
Example 1:

Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
Output: 5
Explanation: The grid is-
1 1 1 0
0 0 1 0
0 0 0 1
The largest region of 1's is colored
in orange.
Example 2:

Input: grid = {{0,1}}
Output: 1
Explanation: The grid is-
0 1
The largest region of 1's is colored in 
orange.

Your Task:
You don't need to read or print anyhting. Your task is to complete the function findMaxArea() which takes grid as input parameter and returns the area of the largest region of 1's.


Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 500



Solution: 

from collections import deque
class Solution:
    
    #Function to check whether the cell is within the matrix bounds.
    def isValid(self, x, y, n, m):
        return (x >= 0 and x < n and y >= 0 and y < m)
    
    
    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        #these lists are used to get row and column numbers
        #of 8 neighbours of a given cell.
        dx = [-1,1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        
        #queue to store the cell indexes which have grid value 1.
        q = deque()
        ans = 0
        
        #traversing all the cells of the matrix.
        for i in range(n):
            for j in range(m):
                
                #if grid value is 1, we update the grid value as 0 
			    #and push the cell indexes into queue.
                if(grid[i][j] == 1):
                    cnt =  1
                    grid[i][j] =  0
                    q.append([i,j])
                    
                    
                    while(len(q)):
                        
                        #storing the cell indexes at top of 
                        #queue and popping them.
                        cur = q.popleft()
                        x = cur[0]
                        y = cur[1]
                        
                        #iterating over the adjacent cells.
                        for k in range(8):
                            n_x = x + dx[k]
                            n_y = y + dy[k]
                            
                            #if indexes are within range and grid value is 1,
                            #we update the grid value as 0, increment counter 
			                #and push the cell indexes into queue.
                            if(self.isValid(n_x,n_y,n,m) and grid[n_x][n_y]==1):
                                cnt = cnt + 1
                                grid[n_x][n_y] = 0
                                q.append([n_x, n_y])
                                
                    #updating maximum area.
                    ans = max(ans, cnt)
        
        return ans

#{ 
#  Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.findMaxArea(grid)
		print(ans)

# } Driver Code Ends