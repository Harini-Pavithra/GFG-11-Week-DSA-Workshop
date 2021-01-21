Spirally traversing a matrix 

Given a matrix of size R*C. Traverse the matrix in spiral form.

Example 1:

Input:
R = 4, C = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
R = 3, C = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, R and C as input parameters and returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)

Constraints:
2 <= R, C <= 100
0 <= matrixi <= 100

Solution
Given a matrix of size R*C. Traverse the matrix in spiral form.

Example 1:

Input:
R = 4, C = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
R = 3, C = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, R and C as input parameters and returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)

Constraints:
2 <= R, C <= 100
0 <= matrixi <= 100

Solution

#User function Template for python3
def spirallyTraverse(matrix, r, c): 
    row = 0 
    col = 0
    output = []
    while (row < r and col < c) : 
          
        # Print first row
        for i in range(col, c) : 
            output.append(matrix[row][i])      
        row += 1
  
        # Print last column
        for i in range(row, r) : 
            output.append(matrix[i][c - 1]) 
        c -= 1
  
        # Print last row 
        if (row < r) : 
            for i in range(c - 1, (col - 1), -1) : 
                output.append(matrix[r - 1][i]) 
            r -= 1
          
        # Print first column 
        if (col < c) : 
            for i in range(r - 1, row - 1, -1) : 
                output.append(matrix[i][col]) 
              
            col += 1

    return output
    
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        ans = spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends