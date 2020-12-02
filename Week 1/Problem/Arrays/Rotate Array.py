Rotate Array 

Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

 

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
 

Example 2:

Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 
when rotated by 3 elements, it becomes 
8 10 12 14 16 18 20 2 4 6.
 

Your Task:
Complete the function rotateArr() which takes the array, D and N as input parameters and rotates the array by D elements. The array must be modified in-place without using extra space. 

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 107
1 <= D <= N
0 <= arr[i] <= 105

Solution:

#User function Template for python3
def gcd(D, N): 
    if N == 0: 
        return D; 
    else: 
        return gcd(N, D % N) 
        
def rotateArr(A,D,N):
    #Your code here
    D = D % N 
    g_c_d = gcd(D, N) 
    for i in range(g_c_d): 
          
        # move i-th values of blocks  
        temp = A[i] 
        j = i 
        while 1: 
            k = j + D 
            if k >= N: 
                k = k - N 
            if k == i: 
                break
            A[j] = A[k] 
            j = k 
        A[j] = temp 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        
        rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends