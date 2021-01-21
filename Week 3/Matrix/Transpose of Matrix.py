Transpose of Matrix 

Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.

Example 1:

Input:
N = 4
mat[][] = {{1, 1, 1, 1},
           {2, 2, 2, 2}
           {3, 3, 3, 3}
           {4, 4, 4, 4}}
Output: 
{{1, 2, 3, 4},  
 {1, 2, 3, 4}  
 {1, 2, 3, 4}
 {1, 2, 3, 4}} 
Example 2:

Input:
N = 2
mat[][] = {{1, 2},
           {-9, -2}}
Output:
{{1, -9}, 
 {2, -2}}

Your Task:
You dont need to read input or print anything. Complete the function transpose() which takes matrix[][] and N as input parameter and finds the transpose of the input matrix. You need to do this in-place. That is you need to update the original matrix with the transpose. 

Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 100
-103 <= mat[i][j] <= 103

Solution

#User function Template for python3

def transpose(matrix, n):
    # code here 
    tmp = 0
    for i in range(n):
        for j in range(i+1,n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp




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
    
        transpose(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()
            

# } Driver Code Ends