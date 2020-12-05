Union of Two Sorted Arrays

Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size N and M respectively, find their union.


Example 1:

Input: 
N = 5, arr1[] = {1, 2, 3, 4, 5}  
M = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 2:

Input: 
N = 5, arr1[] = {2, 2, 3, 4, 5}  
M = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 3:

Input:
N = 5, arr1[] = {1, 1, 1, 1, 1}
M = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.

Your Task: 
You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size N and M as input parameters and returns a list containing the union of the two arrays. 
 

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(N+M).
 

Constraints:
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106

Solution:
#User function Template for python3
from collections import OrderedDict 
import math
def mergeArrays(a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    N = n+m
    L = [0] * (N) 
    k=0
    for i in range(0,n):
        L[k] = a[i]
        k +=1
    for j in range(0,m):
        L[k] = b[j]
        k +=1
    
    L.sort()
    
    return list(OrderedDict.fromkeys(L))
    #return L
       



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        li = mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends