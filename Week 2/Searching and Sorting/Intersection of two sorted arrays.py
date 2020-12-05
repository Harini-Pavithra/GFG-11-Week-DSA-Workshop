Intersection of two sorted arrays

The intersection of two arrays contains the elements common to both the arrays. The intersection should not count duplicate elements.
Given two sorted arrays arr1[] and arr2[] of sizes N and M respectively. Find their intersection

 

Example 1:

Input: 
N = 4, arr1[] = {1, 2, 3, 4}  
M = 5, arr2 [] = {2, 4, 6, 7, 8}
Output: 2 4
Explanation: 2 and 4 are only common 
elements in both the arrays.
 

Example 2:

Input: 
N = 5, arr1[] = {1, 2, 2, 3, 4}
M = 6, arr2[] = {2, 2, 4, 6, 7, 8}
Output: 2 4
Explanation: 2 and 4 are the only 
common elements.
 

Example 3:

Input:
N = 2, arr1[] = {1, 2}
M = 2, arr2[] = {3, 4}
Output: -1
Explanation: No common elements.

 

Your Task:
You do not need to read input or print anything. Complete the function printIntersection() that takes arr1,arr2,  N and M as input parameters and return a list of integers containing the intersection of two arrays. If the intersection is empty then then list should contain -1.


Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).

 

Constraints:
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106

Solution:

#User function Template for python3

def printIntersection(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: array of intersection of two array or -1
    '''
    # code here
    L = sorted(set(a).intersection(set(b)))
    return L



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        l = printIntersection(a,b,n,m)
        print(*l)
# } Driver Code Ends 

