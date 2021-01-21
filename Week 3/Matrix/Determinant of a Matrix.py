Determinant of a Matrix

Given a square matrix of size N x N. The task is to find the determinant of this matrix.

Example 1:

Input:
N = 4
matrix[][] = {{1, 0, 2, -1},
              {3, 0, 0, 5},
              {2, 1, 4, -3},
              {1, 0, 5, 0}}
Output: 30
Explanation:
Determinant of the given matrix is 30.
Example 2:

Input:
N = 3
matrix[][] = {{1, 2, 3},
              {4, 5, 6},
              {7, 10, 9}}
Output: 12
Explanation:
Determinant of the given matrix is 12.

Your Task:
You don't need to read input or print anything. Complete the function determinantOfMatrix() that takes matrix and its size n as input parameters and returns the determinant of the matrix.

Expected Time Complexity: O(N4)
Expected Auxiliary Space: O(N2)

Constraints:
1 <= N <= 8
-10 <= mat[i][j] <= 10

Solution

#User function Template for python3
import numpy as np

def determinantOfMatrix(matrix,n):
    # code here 
    det = np.linalg.det(matrix)
    det = round(det)
    return int(det)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        print(determinantOfMatrix(matrix,n))
# } Driver Code Ends