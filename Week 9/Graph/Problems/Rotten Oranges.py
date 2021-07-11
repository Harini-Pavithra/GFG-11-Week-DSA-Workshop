Rotten Oranges 

Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
 

Your Task:
You don't need to read or print anything, Your task is to complete the function orangesRotting() which takes grid as input parameter and returns the minimum time to rot all the fresh oranges. If not possible returns -1.
 

Expected Time Compelxity: O(n*m)
Expected Auxiliary Space: O(1)
 

Constraints:
1 ≤ n, m ≤ 500

Solution



class Solution:
    
    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        ct = 0 
        res = -1 
        
        #queue to store cells which have rotten oranges.
        q = Queue()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        #traversing over all the cells of the matrix.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                #if grid value is more than 0, we increment the counter.
                if grid[i][j]>0:
                    ct+=1
                    
                #if grid value is 2, we push the cell indexes into queue.
                if(grid[i][j]==2):
                    q.put([i,j])
        
        while not q.empty():
            
            #incrementing result counter.
            res+=1 
            size = q.qsize()
            for k in range(size):
                
                #popping the front element of queue and storing cell indexes.
                cur = q.get()
                ct -= 1
                
                #traversing the adjacent vertices.
                for i in range(4):
                    x = cur[0] + dx[i]
                    y = cur[1] + dy[i]
                    
                    #if cell indexes are within matrix bounds and grid value
                    #is not 1, we continue the loop else we store 2 in current
                    #cell and push the cell indexes in the queue.
                    if x>=len(grid) or x<0 or y>=len(grid[0]) or y<0 or grid[x][y]!=1:
                        continue
                    grid[x][y] = 2
                    q.put([x,y])
        
        #returning the minimum time.
        if ct:
            return -1
        else:
            return max(0,res)
            
            
            
#{ 
#  Driver Code Starts


from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends