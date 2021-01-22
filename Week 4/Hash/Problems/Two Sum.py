Two Sum 

Given an array of positive integers and an integer. Determine whether or not there exist two elements in A whose sum is exactly equal to that integer.

Example 1:

Input:
N = 6, X = 16
A[] = {1,4,45,6,10,8}
Output: Yes
Explanation: 10 and 6 are numbers
making a pair whose sum is equal to 16.
Example 2:

Input:
N = 5, X = 10
A[] = {1,2,4,3,6}
Output: Yes
Your Task :
You don't need to read input or print anything. Your task is to complete the boolean function keypair() which takes the array A[], the size of the array (N) and another number (X) as inputs and returns true if there exists a pair in A[] that sums up to X and returns false otherwise. (THe driver code will print "Yes" if the returned values is true, otherwise "No")

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105
1 ≤ X ≤ 2*105

Solution

#User function Template for python3

# A[] : the input array of positive integers
# N : size of the array arr[]
# X : the required sum
def keypair(A, N, X):
    # code here
    A.sort()
    i=0 # from starting
    j=N-1 #from end
    while(i<j):
        sum1 = A[i] + A[j]
        if sum1>X:
            j=j-1
            continue
        if sum1 == X:
            return True
        i=i+1
    return False
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sln=keypair(a,n,x)
    if(sln):
        print("Yes")
    else:
        print("No")
# } Driver Code Ends
