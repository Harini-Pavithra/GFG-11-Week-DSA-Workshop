Multiply the matrices 

When dealing with matrices, you may, sooner or later, run into the elusive task of matrix multiplication. Here, we will try to multiply two matrices and hope to understand the process.

Two matrices A[][] and B[][] can only be multiplied if number of columns in A is equal to number of rows in B. The dimensions of the resultant matrix will have A's row size and B's column size.

Given two matrices A and B having (n1 x m1) and (n2 x m2) dimensions respectively. Multiply A and B. 

Example 1:

Input:
n1 = 3, m1 = 2
A[][] = {{4, 8},
         {0, 2}
         {1, 6}}
n2 = 2, m2 = 2
B[][] = {{5, 2},
         {9, 4}}
Output: 92 40 18 8 59 26
Explanation:
Matrices are of size 3 x 2 and 2 x 2 which 
results in 3 x 2 matrix with elements as:
res[][] = {{92, 40},
           {18, 8}
           {59, 26}}
Example 2:

Input:
n1 = 1, m1 = 1
A[][] = {2}
n2 = 1, m2 = 1
B[][] = {3}
Output: 6
Explanation: Both matrices are of size 1 x 1 
which results in 1 x 1 matrix having element 6.
 

Your Task:
You dont need to read input or print anything. Complete the function multiplyMatrix() that takes A and B as input parameters and returns a matrix containing their product. If the multiplication is not possible return an empty matrix.

 

Expected Time Complexity: O(N1 * M1 * M2)
Expected Auxiliary Space: O(N1 * M2) for resultant matrix. 

 

Constraints:
1 <= n1, m1, n2, m2 <= 30
0 <= Ai, Bi <= 100

Solution 

#User function Template for python3

def multiplyMatrix(A,B):
    # code here 
    m=len(A)
    n = len(A[0])
    n2 = len(B)
    l = len(B[0])

    a= [[0 for x in range(l)]
           for y in range(m)]
    # print(m,n,n2,l,a)
    if n==n2:
        for i in range(0,m):
            for j in range(0,l):
                # print(i,j)
                a[i][j]=0
                for k in range(0,n):
                    a[i][j] = a[i][j] + A[i][k]*B[k][j]

    else:
        a=[]
        return a
    # print(a)
    return a



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1,m1 = map(int,input().strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                A[i][j]=line1[k]
                k+=1
       
        n2,m2 = map(int,input().strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n2):
            for j in range (m2):
                B[i][j]=line2[k]
                k+=1

        ans = multiplyMatrix(A,B)

        if(len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range (len(ans[0])):
                    print(ans[i][j],end=' ')
            print() 

# } Driver Code Ends