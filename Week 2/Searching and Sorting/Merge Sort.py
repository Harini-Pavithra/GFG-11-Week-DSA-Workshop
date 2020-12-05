Merge Sort

Merge Sort is a Divide and Conquer algorithm. It repeatedly divides the array into two halves and combines them in sorted manner. 

Given an array arr[], its starting position l and its ending position r. Merge Sort is achieved using the following algorithm. 

MergeSort(arr[], l,  r)
    If r > l
         1. Find the middle point to divide 
            the array into two halves:  
                 middle m = (l+r)/2
         2. Call mergeSort for first half:   
                 Call mergeSort(arr, l, m)
         3. Call mergeSort for second half:
                 Call mergeSort(arr, m+1, r)
         4. Merge the two halves sorted in 
            step 2 and 3:
                 Call merge(arr, l, m, r)
Implement the merge() function used in MergeSort().


Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output: 1 3 4 7 9

Example 2:

Input:
N = 10
arr[] = {10 9 8 7 6 5 4 3 2 1}
Output: 1 2 3 4 5 6 7 8 9 10

Your Task:
You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r. 
Assume that the range [l,m] and [m+1,r] are already sorted.


Expected Auxiliary Space: O(n)
Expected Time Complexity: O(n) for the merge() function only.


Constraints:
1 <= N <= 105
1 <= arr[i] <= 103

Solution:

#User function Template for python3

def merge(arr, l, m, r): 
    # code here
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    
    i = 0     
    j = 0      
    k = l      
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
        
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def mergeSort (arr, l, r):
    if l < r:
        m = l + (r - l)//2
        
        mergeSort (arr, l, m)
        mergeSort (arr, m+1, r)
        merge (arr, l, m, r)

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends