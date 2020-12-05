Median of Two sorted arrays

Given two sorted arrays of sizes N and M respectively. The task is to find the median of the two arrays when they get merged.

 

Example 1:

Input:
N = 5, M = 6 
arr[] = {1,2,3,4,5}
brr[] = {3,4,5,6,7,8}
Output: 4
Explanation: After merging two arrays, 
elements will be as 1 2 3 3 4 4 5 5 6 7 8
So, median is 4.
 

Example 2:

Input:
N = 2, M = 3 
arr[] = {1,2}
brr[] = {2,3,4}
Output: 2
Explanation: After merging two arrays, 
elements will be as 1 2 2 3 4. So, 
median is 2.
 

Your Task:
You do not need to read input or print anything. Complete findMedian() function which takes the two arrays and n and m as input parameters and returns their median. If there are total even elements, return floor of average of middle two elements.

 

Expected Time Complexity : O(log(max(m,n)))
Expected Auxilliary Space : O(1)

 

Constraints:
1 <= N, M <= 106
1 <= arr[i], brr[i] <= 107

Solution:

#User function Template for python3
import math
def findMedianSortedArrays(arr1, n1, arr2, n2):
    '''
    arr1: shorter array
    n1:   len of arr
    arr2: larger array
    n2:   len of array
    return: median
    '''
    #code here
    l = sorted(arr1+arr2)
    if (n1+n2)%2 == 0:
        a = l[((n1+n2)//2)-1]
        b = l[((n1+n2)//2) + 1 - 1]
        return math.floor(((a+b)/2))
    else:
        c = l[((n1+n2+1)//2)-1]
        return c



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends