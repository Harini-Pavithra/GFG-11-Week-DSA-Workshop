Search in a row-column sorted Matrix 

Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. Find whether element x is present in the matrix or not.

Example 1:

Input:
n = 3, m = 3, x = 62
matrix[][] = {{ 3, 30, 38},
              {36, 43, 60},
              {40, 51, 69}}
Output: 0
Explanation:
62 is not present in the matrix, 
so output is 0.
Example 2:

Input:
n = 1, m = 6, x = 55
matrix[][] = {{18, 21, 27, 38, 55, 67}}
Output: 1
Explanation: 55 is present in the matrix.

Your Task:
You don't need to read input or print anything. Complete the function search() that takes n, m, x, and matrix[][] as input parameters and returns a boolean value. True if x is present in the matrix and false if it is not present.

Expected Time Complexity: O(N + M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N, M <= 1000
1 <= mat[][] <= 105
1 <= X <= 1000

Solution

#User function Template for python3

def search2(matrix, n, m, x): 
	# code here 
	for i in range(n):
        for j in range(m):
            if matrix[i][j] == 54:
                return True
    return 0
def search(matrix, n, m, x):
    i=0
    j=m-1
    # print(n,m,i,j)
    while(i<n and j>=0):
        # print("in loop")
        if matrix[i][j] == x:
            return True
        elif matrix[i][j]>x:
            # means element is in current row so decrease colomn
            # print("element is in current row so decrease colomn")
            j=j-1
        else:
            # means elememt is in next row so increase row
            # print("elememt is in next row so increase row")
            i=i+1
    return 0

	



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		size = input().strip().split()
		r = int(size[0])
		c = int(size[1])
		line = input().strip().split()
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				matrix[i][j] = int( line[i*c+j] )
		target = int(input())

		if (search(matrix,r,c,target)): 
			print(1) 
		else: 
			print(0) 


# } Driver Code Ends