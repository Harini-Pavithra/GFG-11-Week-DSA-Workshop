Rotate by 90 degree 

Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space. 

Example 1:

Input:
N = 3 
matrix[][] = {{1, 2, 3},
              {4, 5, 6}
              {7, 8, 9}}
Output: 
Rotated Matrix:
3 6 9
2 5 8
1 4 7
Example 2:

Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
Rotated Matrix:
2 4
1 3

Your Task:
You dont need to read input or print anything. Complete the function rotateby90() which takes the matrix as input parameter and rotates it by 90 degrees in anti-clockwise direction without using any extra space. You have to modify the input matrix in-place. 

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 100
1 <= matrix[][] <= 1000


Solution 

#User function Template for python3

def rotateby90(a, n): 
    # code here
    for i in range(0,n//2):
        for j in range(i,n-1-i):
            temp = a[i][j]

            a[i][j] = a[j][n-1-i]
            a[j][n - 1 - i] = a[n-1-i][n-1-j]
            a[n - 1 - i][n - 1 - j] = a[n-1-j][i]
            a[n-1-j][i] = temp

    return a
import copy
def rotateby90(a, n):
    temp = copy.deepcopy(a)
    for i in range(0,n):
        for j in range(0,n):
            a[i][j] = temp[j][n-i-1]




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
    
        rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends

